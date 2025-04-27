import json
import requests

def fetch_mock_threat_feed(url):
    ''' Simulate fetching a threat feed (e.g., TAXII 2.1 API) '''
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch feed: {response.status_code}")

def parse_stix_objects(objects):
    ''' Parses a list of STIX 2.1 objects and extracts indicators '''
    indicators = []
    for obj in objects:
        if obj.get('type') == 'indicator':
            indicators.append({
                'type': obj.get('indicator_types', []),
                'pattern': obj.get('pattern', ''),
                'created': obj.get('created', '')
            })
    return indicators

if __name__ == "__main__":
    # Example public STIX/TAXII server (mock URL for now)
    url = "https://raw.githubusercontent.com/oasis-open/cti-stix-common-objects/master/example-bundle.json"
    
    try:
        data = fetch_mock_threat_feed(url)
        indicators = parse_stix_objects(data.get('objects', []))
        
        print(f"Fetched {len(indicators)} indicators:")
        for ind in indicators:
            print(f"- {ind['type']} | {ind['pattern']} | {ind['created']}")
    except Exception as e:
        print(f"Error: {e}")