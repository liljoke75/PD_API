import requests
import json

response = requests.get(
  "https://hei.api.uni-foundation.eu/api/public/v1/country/LV/hei")
obj = json.loads(response.content)

schools = []

for school in obj['data']:
  schools.append(school['attributes']['label'])

schools.sort()
for school in schools:
  print(school)
