import requests
import json

url = "https://192.168.0.24:443/restconf/data/ietf-interfaces:interfaces-state/"

payload = {}
headers = {
  'Content-Type': 'application/yang-data+json',
  'Accept': 'application/yang-data+json',
  'Authorization': 'Basic aWlpcHl1c2VyMTpQeTAxUGFzcw=='
}

response = requests.request("GET", url, headers=headers,verify=False, data=payload)

print(response.text)

#postman ios-xe rest apis
#https://www.postman.com/ciscodevnet/workspace/cisco-devnet-s-public-workspace/overview
