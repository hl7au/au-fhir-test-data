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
                handler.OnAfterResponse += (sender, e) =>
                {
                    Console.WriteLine(e.RawResponse.RequestMessage.Method + " " + e.RawResponse.RequestMessage.RequestUri);
                    Console.WriteLine(((int)e.RawResponse.StatusCode).ToString() + " " + e.RawResponse.StatusCode);
                    Console.WriteLine("Content-Location: " + e.RawResponse.Content.Headers.ContentLocation);
                    Console.WriteLine("Last-Modified: " + e.RawResponse.Content.Headers.LastModified);
                    Console.WriteLine("ETag: " + e.RawResponse.Headers.ETag);
                    //var list = e.RawResponse.Headers.ToList();
                };

                var serializerOptions = new JsonSerializerOptions().ForFhir(ModelInfo.ModelInspector);

                var inputFolder = @"..\generated";
                if (!Directory.Exists(Path.GetFullPath(inputFolder)))
                    inputFolder = @"..\..\..\" + inputFolder;


                var files = Directory.GetFiles(inputFolder, resourceType + "*.json");

                foreach (var file in files)
                {
                    using (var fileStream = File.OpenRead(file))
                    {

                        Console.WriteLine("File " + file + " read as " + resourceType);

                        switch (resourceType)
                        {
                            case "Patient":
                                var patient = JsonSerializer.Deserialize<Patient>(fileStream, serializerOptions);
                                var updatedResource = client.Update<Patient>(patient);
                                break;

                            default:
                                throw new ArgumentException("resourceType " + resourceType + " not supported");
                        }

                        //Console.WriteLine(resourceType + " " + resource.Id + " updated ");
                    }
                }
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