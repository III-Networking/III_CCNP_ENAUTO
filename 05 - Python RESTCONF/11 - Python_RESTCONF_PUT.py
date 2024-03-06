import requests
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://192.168.0.24:443/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet1"

payload = json.dumps({
  "ietf-interfaces:interface": {
    "name": "GigabitEthernet1",
    "description": "Desc-by-PythonREST",
    "type": "iana-if-type:ethernetCsmacd",
    "enabled": True,
    "ietf-ip:ipv4": {
      "address": [
        {
          "ip": "10.255.3.1",
          "netmask": "255.255.255.0"
        }
      ]
    }
  }
})
headers = {
  'Accept': 'application/yang-data+json',
  'Content-Type': 'application/yang-data+json',
  'Authorization': 'Basic aWlpcHl1c2VyMTpQeTAxUGFzcw=='
}

response = requests.request("PUT", url, headers=headers,verify=False, data=payload)

print(response.text)