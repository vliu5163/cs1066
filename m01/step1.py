import urllib.request
import json

# AMD's CIK number
cik = "0000002488"

# SEC EDGAR API endpoint
url = f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json"

# Create a request with a User-Agent header
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}
req = urllib.request.Request(url, headers=headers)

# Fetch the data
response = urllib.request.urlopen(req)
data = json.loads(response.read())

# Save to amd_data.json
with open('amd_data.json', 'w') as f:
    json.dump(data, f, indent=2)

print("AMD data successfully saved to amd_data.json")
