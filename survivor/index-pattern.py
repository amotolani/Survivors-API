"""
This script creates an index pattern on kibana that matches the elasticsearch logs index
"""
import requests
import json
import os

kibana_host = os.environ.get('KIBANA_HOST')
url = "http://{}:5601/api/saved_objects/index-pattern/survivorapi-logs".format(kibana_host)

payload = json.dumps({
  "attributes": {
    "title": "survivorapi-logs",
    "timeFieldName": "@timestamp"
  }
})
headers = {
  'kbn-xsrf': 'true',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)
