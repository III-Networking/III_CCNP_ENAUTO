import xmltodict
import xml.dom.minidom
from lxml.etree import fromstring
from ncclient import manager

m = manager.connect(host='192.168.0.22', port=830, username='iiipyuser1',
                    password='Py01Pass', device_params={'name': 'csr'})

Filter_X="/mdt-oper-data/mdt-subscriptions"
netconf_reply = m.get(filter=("xpath",Filter_X))

XD = xml.dom.minidom.parseString( str(netconf_reply))
print(XD.toprettyxml( indent = "  " ))