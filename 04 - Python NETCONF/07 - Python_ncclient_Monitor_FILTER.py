from ncclient import manager

RouterR2 =  manager.connect(host="192.168.0.26",
                    port=830,
                    username="iiipyuser1",
                    password="Py01Pass",
                    hostkey_verify=False,
                    device_params={'name':'csr'})

FILTER = '''
<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <native
        xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface><GigabitEthernet><name>2</name></GigabitEthernet></interface>
    </native>
</filter>
'''

print (RouterR2.get_config("running", FILTER))
RouterR2.close_session()