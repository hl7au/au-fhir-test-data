using Hl7.Fhir.Model;
using Hl7.Fhir.Specification;
using Hl7.Fhir.Specification.Source;
using System.Collections.Generic;
using System.Threading.Tasks;

namespace Sparked.Csv2FhirMapping
{
    public class InMemoryProvider : IAsyncResourceResolver, IResourceResolver
    {
        public InMemoryProvider(IEnumerable<IConformanceResource> resources)
        {
            foreach (var resource in resources)
                Add(resource);
        }

        public InMemoryProvider(IConformanceResource resource)
        {
            Add(resource);
        }

        public void Add(IConformanceResource resource)
        {
            _resources.Add(resource.Url, resource);
            if (resource is StructureDefinition sd)
            {
                _typeNameMap.Add(sd.Type, sd.Url);
            }
        }

        public IEnumerable<IConformanceResource> Resources => _resources.Values;
        Dictionary<string, IConformanceResource> _resources = new Dictionary<string, IConformanceResource>();
        Dictionary<string, string> _typeNameMap = new Dictionary<string, string>();

        public bool TypeNameMapper(string name, out string canonical)
        {
            if (_typeNameMap.ContainsKey(name))
            {
                canonical = _typeNameMap[name];
                return true;
            }
            return StructureDefinitionSummaryProvider.DefaultTypeNameMapper(name, out canonical);
        }
        public Resource ResolveByCanonicalUri(string uri)
        {
            if (_resources.ContainsKey(uri))
                return _resources[uri] as Resource;
            return null;
        }

        public Task<Resource> ResolveByCanonicalUriAsync(string uri)
        {
            if (_resources.ContainsKey(uri))
                return Task<Resource>.FromResult(_resources[uri] as Resource);
            return Task<Resource>.FromResult(null as Resource);
        }

        public Resource ResolveByUri(string uri)
        {
            if (_resources.ContainsKey(uri))
                return _resources[uri] as Resource;
            return null;
        }

        public Task<Resource> ResolveByUriAsync(string uri)
        {
            if (_resources.ContainsKey(uri))
                return Task<Resource>.FromResult(_resources[uri] as Resource);
            return Task<Resource>.FromResult(null as Resource);
        }
    }
}
