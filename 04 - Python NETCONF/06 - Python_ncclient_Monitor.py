from ncclient import manager

RouterR2 =  manager.connect(host="192.168.0.26",
                    port=830,
                    username="iiipyuser1",
                    password="Py01Pass",
                    hostkey_verify=False,
                    device_params={'name':'csr'})

print (RouterR2.get_config("running"))
RouterR2.close_session()