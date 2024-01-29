using System;
using System.IO;
using Task = System.Threading.Tasks.Task;

using Hl7.Fhir.Model;
using Hl7.Fhir.Serialization;
using Hl7.Fhir.MappingLanguage;
using Hl7.Fhir.ElementModel;
using System.Diagnostics;
using Hl7.Fhir.ElementModel.Types;

namespace Sparked.Csv2FhirMapping
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            //Console.WriteLine(string.Join(" ", args));
            var appName = System.AppDomain.CurrentDomain.FriendlyName;

            if (args.Length >= 3)
            {
                var argString = System.Environment.CommandLine.Substring(System.Environment.ProcessPath.Length);
                Console.WriteLine(appName + argString);

                var program = new Program();

                //var mapFile = @"Maps\CSV2Patient.map";
                var mapFile = @"Maps\" + args[2];
                if (!Directory.Exists(Path.GetDirectoryName(mapFile)))
                    mapFile = @"..\..\..\" + mapFile;

                var mapFileInfo = new FileInfo(mapFile);
                Debug.WriteLine("Map file " + (mapFileInfo.Exists ? "exists" : "not found") + ": " + mapFileInfo.FullName);

                //var csvFile = @"TestData\Patient - test IHIs.csv";
                var csvFile = @"TestData\" + args[1];

                if (!Directory.Exists(Path.GetDirectoryName(csvFile)))
                    csvFile = @"..\..\..\" + csvFile;

                var csvFileInfo = new FileInfo(csvFile);
                Debug.WriteLine("CSV file " + (csvFileInfo.Exists ? "exists" : "not found") + ": " + csvFileInfo.FullName);

                var resourceType = args[0];

                program.TransformCsv2Patient(mapFile, csvFile, resourceType);
            }
            else
            {
                Console.WriteLine("Usage: " + appName + " <resource-type> <csv-filename> <mapping-filename>");
                Console.WriteLine("E.g. : " + appName + " Patient \"AU Core Sample Data - Patient.csv\" CSV2Patient.map");
            }
        }

        public void TransformCsv2Patient(string mapFile, string csvFile, string resourceType)
        {
            if (string.IsNullOrEmpty(mapFile)) throw new ArgumentNullException("mapFile");
            if (string.IsNullOrEmpty(mapFile)) throw new ArgumentNullException("csvFile");

            var mapText = File.ReadAllText(mapFile);
            var parser = new StructureMapUtilitiesParse();
            var structureMap = parser.parse(mapText, resourceType);
            var csvType = resourceType + "CSV";

            using (var stream = File.OpenRead(csvFile))
            {
                using (var sr = new StreamReader(stream))
                {
                    CsvReader reader = new CsvReader(sr, "http://example.org/StructureDefinition/" + csvType, csvType);
                    reader.ParseHeader();

                    var worker = new TestWorker(reader.Source);
                    var engine = new StructureMapUtilitiesExecute(worker, null, reader.Provider);

                    Console.WriteLine($">{reader.rawHeader}<");
                    var node = reader.GetNextEntry();
                    int count = 0;
                    while (node != null)
                    {
                        count++;
                        Console.WriteLine(node.ToJson());
                        var target = engine.GenerateEmptyTargetOutputStructure(structureMap);
                        engine.transform(null, node, structureMap, target);

                        var output = target.ToPoco<Resource>();

                        var outContent = new FhirJsonSerializer(new SerializerSettings() { Pretty = true }).SerializeToString(output);
                        System.Diagnostics.Trace.WriteLine(outContent);


                        var folder = Path.GetDirectoryName(csvFile);
                        var outFile = Path.Combine(folder, resourceType + "-" + output.Id + ".json");

                        File.WriteAllText(outFile, outContent);

                        node = reader.GetNextEntry();
                    }
                    Console.WriteLine($"Total Rows: {count}");
                }
            }
        }
    }
}