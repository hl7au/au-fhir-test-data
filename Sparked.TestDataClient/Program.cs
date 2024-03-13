using Hl7.Fhir.Model;
using Hl7.Fhir.Rest;
using Hl7.Fhir.Serialization;
using System.IO;
using System.Net.Http.Headers;
using System.Text.Json;

internal class Program
{
    private static void Main(string[] args)
    {
        var appName = System.AppDomain.CurrentDomain.FriendlyName;

        if (args.Length >= 2)
        {
            var argString = System.Environment.CommandLine.Substring(System.Environment.ProcessPath.Length);
            Console.WriteLine(appName + argString);

            var resourceType = args[0];

            var serverUrl = args[1]; 

            string authScheme = null;
            string authParameter = null;
            if (args.Length >= 2)
            {
                authScheme = args[2];
                authParameter = args[3];
            }

            var settings = new FhirClientSettings
            {
                Timeout = 120000,
                PreferredFormat = ResourceFormat.Json,
                VerifyFhirVersion = true,
                ReturnPreference = ReturnPreference.Minimal
            };

            var handler = new AuthorizationMessageHandler();
            if (!string.IsNullOrEmpty(authScheme))
                handler.Authorization = new AuthenticationHeaderValue(authScheme, authParameter);

            using (var client = new FhirClient(serverUrl, settings, handler).WithStrictSerializer())
            {
                int count = 0;
                int created = 0;
                int updated = 0;
                var resourceId = "";
                Resource updatedResource = null;

                handler.OnAfterResponse += (sender, e) =>
                {
                    Console.WriteLine(e.RawResponse.RequestMessage.Method + " " + e.RawResponse.RequestMessage.RequestUri);
                    Console.WriteLine(((int)e.RawResponse.StatusCode).ToString() + " " + e.RawResponse.StatusCode);

                    if (e.RawResponse.RequestMessage.Method == HttpMethod.Post || e.RawResponse.RequestMessage.Method == HttpMethod.Put)
                    {
                        if (e.RawResponse.StatusCode == System.Net.HttpStatusCode.Created)
                            created++;
                        else if (e.RawResponse.StatusCode == System.Net.HttpStatusCode.OK)
                        {
                            if (e.RawResponse.Headers.Date == e.RawResponse.Content.Headers.LastModified)
                            {
                                updated++;
                                Console.WriteLine(resourceType + " " + resourceId + " updated");
                            }
                            else
                                Console.WriteLine(resourceType + " " + resourceId + " unchanged");
                        }
                    }

                    Console.WriteLine("Content-Location: " + e.RawResponse.Content.Headers.ContentLocation);
                    Console.WriteLine("Last-Modified: " + e.RawResponse.Content.Headers.LastModified);
                    Console.WriteLine("Date: " + e.RawResponse.Headers.Date);
                    Console.WriteLine("ETag: " + e.RawResponse.Headers.ETag);
                    //var list = e.RawResponse.Headers.ToList();
                };

                var serializerOptions = new JsonSerializerOptions().ForFhir(ModelInfo.ModelInspector);

                var inputFolder = @"..\generated";
                if (!Directory.Exists(Path.GetFullPath(inputFolder)))
                    inputFolder = @"..\..\..\" + inputFolder;


                var files = Directory.GetFiles(inputFolder, resourceType + "-*.json");

                foreach (var file in files)
                {
                    count++;
                    using (var fileStream = File.OpenRead(file))
                    {

                        Console.WriteLine("File " + file + " read as " + resourceType);

                        switch (resourceType)
                        {
                            case "Patient":
                                var patient = JsonSerializer.Deserialize<Patient>(fileStream, serializerOptions);
                                updatedResource = client.Update<Patient>(patient);
                                break;

                            case "Practitioner":
                                var practitioner = JsonSerializer.Deserialize<Practitioner>(fileStream, serializerOptions);
                                resourceId = practitioner.Id;
                                updatedResource = client.Update<Practitioner>(practitioner);
                                break;

                            case "PractitionerRole":
                                var practitionerRole = JsonSerializer.Deserialize<PractitionerRole>(fileStream, serializerOptions);
                                resourceId = practitionerRole.Id;
                                updatedResource = client.Update<PractitionerRole>(practitionerRole);
                                break;

                            case "Organization":
                                var organization = JsonSerializer.Deserialize<Organization>(fileStream, serializerOptions);
                                resourceId = organization.Id;
                                updatedResource = client.Update<Organization>(organization);
                                break;

                            case "Location":
                                var location = JsonSerializer.Deserialize<Location>(fileStream, serializerOptions);
                                resourceId = location.Id;
                                updatedResource = client.Update<Location>(location);
                                break;

                            case "Encounter":
                                var encounter = JsonSerializer.Deserialize<Encounter>(fileStream, serializerOptions);
                                resourceId = encounter.Id;
                                updatedResource = client.Update<Encounter>(encounter);
                                break;

                            case "Condition":
                                var condition = JsonSerializer.Deserialize<Condition>(fileStream, serializerOptions);
                                resourceId = condition.Id;
                                updatedResource = client.Update<Condition>(condition);
                                break;

                            case "AllergyIntolerance":
                                var allergyIntolerance = JsonSerializer.Deserialize<AllergyIntolerance>(fileStream, serializerOptions);
                                resourceId = allergyIntolerance.Id;
                                updatedResource = client.Update<AllergyIntolerance>(allergyIntolerance);
                                break;

                            case "Immunization":
                                var immunization = JsonSerializer.Deserialize<Immunization>(fileStream, serializerOptions);
                                resourceId = immunization.Id;
                                updatedResource = client.Update<Immunization>(immunization);
                                break;

                            case "Observation":
                                var observation = JsonSerializer.Deserialize<Observation>(fileStream, serializerOptions);
                                resourceId = observation.Id;
                                updatedResource = client.Update<Observation>(observation);
                                break;

                            case "Provenance":
                                var provenance = JsonSerializer.Deserialize<Provenance>(fileStream, serializerOptions);
                                resourceId = provenance.Id;
                                updatedResource = client.Update<Provenance>(provenance);
                                break;

                            default:
                                throw new ArgumentException("resourceType " + resourceType + " not supported");
                        }
                    }
                }
                Console.WriteLine($"Total resources: {count}, created: {created}, updated: {updated}");
            }
        }
        else
        {
            Console.WriteLine("Usage: " + appName + " <resource-type> <fhir-server> <auth-scheme> <auth-parameter>");
            Console.WriteLine("E.g. : " + appName + " Patient https://hl7auconnectathon.salessbx.smiledigitalhealth.com/fhir-request Basic YnJldHQuZXNsZXI6bvhVaHJyTmI2dnF2Wm8=");
        }
    }

    public class AuthorizationMessageHandler : HttpClientEventHandler
    {
        public System.Net.Http.Headers.AuthenticationHeaderValue Authorization { get; set; }
        protected async override Task<HttpResponseMessage> SendAsync(HttpRequestMessage request, CancellationToken cancellationToken)
        {
            if (Authorization != null)
                request.Headers.Authorization = Authorization;
            return await base.SendAsync(request, cancellationToken);
        }
    }
}