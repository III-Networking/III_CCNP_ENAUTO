import urllib3
import requests
import json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

Host_IP = "192.168.0.22"
UserName = "iiipyuser1"
PassWord = "Py01Pass"
Headers={'Accept': 'application/yang-data+json',
        'Content-Type': 'application/yang-data+json'}

URL = f"https://192.168.0.22:443/restconf/data/Cisco-IOS-XE-mdt-cfg:mdt-config-data"

RES = requests.get(URL,auth = (UserName, PassWord),verify = False, headers = Headers).json()

print (json.dumps(RES, indent=2))
