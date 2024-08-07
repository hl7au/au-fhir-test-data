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

        if (args.Length >= 3)
        {
            var argString = System.Environment.CommandLine.Substring(System.Environment.ProcessPath.Length);
            Console.WriteLine(appName + argString);

            var resourceType = args[0];

            //var inputFolder = @"..\generated";
            var inputFolder = args[1];
            if (!Directory.Exists(Path.GetFullPath(inputFolder)))
            {
                inputFolder = @"..\..\..\" + inputFolder;
                if (!Directory.Exists(Path.GetFullPath(inputFolder)))
                {
                    Console.WriteLine("Input folder not found: " + Path.GetFullPath(args[1]));
                    return;
                }
            }

            var serverUrl = args[2]; 

            string authScheme = null;
            string authParameter = null;
            if (args.Length >= 3)
            {
                authScheme = args[3];
                authParameter = args[4];
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
                int failed = 0;
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

                var files = Directory.GetFiles(inputFolder, resourceType + "-*.json");

                foreach (var file in files)
                {
                    count++;
                    using (var fileStream = File.OpenRead(file))
                    {

                        Console.WriteLine("File " + file + " read as " + resourceType);
                        try
                        {
                            var resource = JsonSerializer.Deserialize<Resource>(fileStream, serializerOptions);
                            resourceId = resource.Id;
                            updatedResource = client.Update<Resource>(resource);
                        }
                        catch (Exception ex)
                        {
                            failed++;
                            Console.WriteLine(resourceType + " " + resourceId + " failed");
                            Console.WriteLine(ex.ToString());
                        }
                    }
                }
                Console.WriteLine($"Total resources: {count}, created: {created}, updated: {updated}, failed: {failed}");
            }
        }
        else
        {
            Console.WriteLine("Usage: " + appName + " <resource-type> <input-folder> <fhir-server> <auth-scheme> <auth-parameter>");
            Console.WriteLine("E.g. : " + appName + " Patient ..\\generated https://fhir.hl7.org.au/aucore/fhir/DEFAULT Basic <token>");
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