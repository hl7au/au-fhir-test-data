using Hl7.Fhir.ElementModel;
using Hl7.Fhir.Model;
using Hl7.Fhir.Specification;
using Hl7.Fhir.Specification.Source;
using Hl7.Fhir.Support;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace Sparked.Csv2FhirMapping
{
    public class CsvReader
    {
        public List<string> Columns { get; private set; } = new List<string>();
        public string rawHeader;
        TextReader _reader;
        string _canonicalUrl;
        string _typeName;

        public CsvReader(TextReader reader, string canonicalUrl = null, string typeName = null)
        {
            _reader = reader;
            _canonicalUrl = canonicalUrl;
            _typeName = typeName;
        }

        public IEnumerable<string> ParseHeader()
        {
            IEnumerable<string> header = ReadLine();
            Columns.AddRange(header);
            return Columns;
        }

        private IEnumerable<string> ReadLine()
        {
            List<string> fields = new List<string>();
            string currentLine = _reader.ReadLine();
            if (currentLine == null)
                return null;

            // Check for quoted content
            var indexStartQuote = currentLine.IndexOf('"');
            while (indexStartQuote != -1)
            {
                // locate the end quote
                var indexEndQuote = currentLine.IndexOf('"', indexStartQuote + 1);
                var lastLength = currentLine.Length;
                while (indexEndQuote == -1)
                {
                    System.Diagnostics.Trace.WriteLine("Needed another line");
                    var nextLine = _reader.ReadLine();
                    currentLine += "\r\n" + nextLine;
                    if (nextLine == null)
                        break;
                    indexEndQuote = currentLine.IndexOf('"', lastLength);
                    lastLength = currentLine.Length;
                }
                indexStartQuote = currentLine.IndexOf('"', indexEndQuote + 1);
            }

            if (string.IsNullOrEmpty(rawHeader))
                rawHeader = currentLine;

            // Have the full line now in currentLine (including any spanned rows)
            var tokens = new[] { ',', '"' };
            int index = currentLine.IndexOfAny(tokens);
            int startIndex = 0;
            while (index != -1)
            {
                if (currentLine[index] == ',')
                {
                    fields.Add(currentLine.Substring(startIndex, index - startIndex).Trim());
                    startIndex = index + 1;
                    index = currentLine.IndexOfAny(tokens, index + 1);
                }
                else
                {
                    // this is a quoted entry, so check for the end marker
                    startIndex = index + 1;
                    int endQuote = currentLine.IndexOf('"', startIndex);
                    while (currentLine.Length > endQuote + 2 && currentLine[endQuote + 1] == '"')
                    {
                        endQuote = currentLine.IndexOf('"', endQuote + 2);
                    }
                    fields.Add(currentLine.Substring(startIndex, endQuote - startIndex).Replace("\"\"", "\""));
                    startIndex = endQuote + 2;
                    if (startIndex > currentLine.Length)
                        break;
                    index = currentLine.IndexOfAny(tokens, startIndex);
                }
                if (index == -1)
                {
                    // last node, just add the rest in
                    fields.Add(currentLine.Substring(startIndex).Trim());
                }
            }

            return fields;
        }

        public ITypedElement GetNextEntry()
        {
            var fields = ReadLine();
            if (fields == null)
                return null;
            if (fields.Count() > 0 && Columns.Count == 0)
            {
                // Dummy in fieldX as the names
                Columns.AddRange(fields.Select((f, i) => $"field{i}"));
            }

            var tes = fields.Select((f, i) => SourceNode.Valued(Columns[i], f));
            //var sn = SourceNode.Node("Entry", tes.ToArray());
            //if (_provider == null)
            //{
            //    var source = new InMemoryProvider(GenerateStructureDefinition());
            //    _provider = new StructureDefinitionSummaryProvider(new CachedResolver(new MultiResolver(source, ZipSource.CreateValidationSource())), source.TypeNameMapper);
            //}
            //// return sn.ToTypedElement();
            //return sn.ToTypedElement(_provider, "Entry");
            var sn = SourceNode.Node(_typeName, tes.ToArray());
            return sn.ToTypedElement(Provider, _typeName);
        }

        InMemoryProvider _source;

        public InMemoryProvider Source
        {
            get
            {
                if (_source == null && Columns.Count > 0)
                {
                    _source = new InMemoryProvider(GenerateStructureDefinition());
                }
                return _source;
            }
        }

        IStructureDefinitionSummaryProvider _provider;

        public IStructureDefinitionSummaryProvider Provider
        { 
            get {
                if (_provider == null && Columns.Count > 0)
                {
                    _provider = new StructureDefinitionSummaryProvider(
                        new CachedResolver(new MultiResolver(Source, ZipSource.CreateValidationSource())), 
                        Source.TypeNameMapper);
                }
                return _provider; 
            } 
        }

        public StructureDefinition GenerateStructureDefinition()
        {
            var result = new StructureDefinition()
            {
                Description = new Markdown(),
                Url = _canonicalUrl,
                Title = _typeName,
                Name = _typeName,
                Status = PublicationStatus.Draft,
                Date = DateTime.Today.ToFhirDate(),
                Publisher = "Code Generated - CSV Reader",
                Kind = StructureDefinition.StructureDefinitionKind.Logical,
                Abstract = false,
                Type = _typeName,
                Derivation = StructureDefinition.TypeDerivationRule.Specialization,
                BaseDefinition = "http://hl7.org/fhir/StructureDefinition/Element",
                Snapshot = new StructureDefinition.SnapshotComponent()
            };
            result.Snapshot.Element.Add(new ElementDefinition()
            {
                Path = _typeName,
                Label = _typeName,
                Min = 0,
                Max = "*"
            });
            result.Snapshot.Element.AddRange(Columns.Select(c => new ElementDefinition()
            {
                Path = $"{_typeName}.{c}",
                Label = c,
                Min = 0,
                Max = "1",
                Type = new[] { new ElementDefinition.TypeRefComponent() { Code = "string" } }.ToList()
            }));
            return result;
        }
    }
}
