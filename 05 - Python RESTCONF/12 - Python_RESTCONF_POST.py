import requests
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://192.168.0.24:443/restconf/data/ietf-interfaces:interfaces"

payload = json.dumps({
  "ietf-interfaces:interface": {
    "name": "Loopback50",
    "description": "Configured by Python/RESTCONF",
    "type": "iana-if-type:softwareLoopback",
    "enabled": True,
    "ietf-ip:ipv4": {
      "address": [
        {
          "ip": "172.28.50.1",
          "netmask": "255.255.255.255"
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

response = requests.request("POST", url, headers=headers,verify=False, data=payload)

print(response.text)
