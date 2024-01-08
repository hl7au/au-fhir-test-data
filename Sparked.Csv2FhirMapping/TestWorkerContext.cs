using Hl7.Fhir.MappingLanguage;
using Hl7.Fhir.Model;
using Hl7.Fhir.Serialization;
using Hl7.Fhir.Specification.Source;
using System;
using System.Collections.Generic;
using System.Linq;
using static Hl7.Fhir.MappingLanguage.StructureMapUtilitiesAnalyze;

namespace Sparked.Csv2FhirMapping
{
    public class TestWorker : IWorkerContext
    {
        IResourceResolver _source;
        List<StructureMap> _maps = new List<StructureMap>();
        public TestWorker(IResourceResolver source, string directoryToAllMaps = null)
        {
            _source = source;
            if (!string.IsNullOrEmpty(directoryToAllMaps))
            {
                foreach (var file in System.IO.Directory.GetFiles(directoryToAllMaps, "*.map"))
                {
                    var expression = System.IO.File.ReadAllText(file);
                    var parser = new StructureMapUtilitiesParse();
                    try
                    {
                    var sm = parser.parse(expression, null);
                    _maps.Add(sm);
                    }
                    catch(Exception ex)
                    {
                        System.Diagnostics.Trace.WriteLine($"Error scanning {file} {ex.Message}");
                    }
                }
            }
        }

        public ValueSet.ExpansionComponent expandVS(ValueSet vs, bool v1, bool v2)
        {
            throw new NotImplementedException();
        }

        public T fetchResource<T>(string url) where T : Resource
        {
            var result = _source.ResolveByCanonicalUri(url);
            if (result is T value)
                return value;
            var result2 = _source.ResolveByUri(url);
            if (result2 is T value2)
                return value2;
            return null;
        }

        public T fetchResourceWithException<T>(string url) where T : Resource
        {
            var result = _source.ResolveByCanonicalUri(url);
            if (result is T value)
                return value;
            var result2 = _source.ResolveByUri(url);
            if (result2 is T value2)
                return value2;
            throw new FHIRException();
        }

        public StructureDefinition fetchTypeDefinition(string code)
        {
            var uri = ModelInfo.CanonicalUriForFhirCoreType(code);
            var result = _source.ResolveByCanonicalUri(uri);
            if (result is StructureDefinition value)
                return value;
            var result2 = _source.ResolveByUri(uri);
            if (result2 is StructureDefinition value2)
                return value2;
            // return null;
            throw new NotImplementedException();
        }

        public string getOverrideVersionNs()
        {
            return null;
            // throw new NotImplementedException();
        }

        public StructureMap getTransform(string value)
        {
            return _maps.FirstOrDefault(m => m.Url == value);
        }

        public IEnumerable<StructureMap> listTransforms(string canonicalUrlTemplate)
        {
            return _maps;
        }

        public string oid2Uri(string code)
        {
            throw new NotImplementedException();
        }

        public ValidationResult validateCode(TerminologyServiceOptions terminologyServiceOptions, string system, string code, string display)
        {
            return new ValidationResult() { Display = display };
        }
    }
}