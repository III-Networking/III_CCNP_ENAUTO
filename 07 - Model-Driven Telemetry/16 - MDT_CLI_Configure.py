from netmiko import ConnectHandler

with open ("MDT_Subscription_IOSXE.txt",'r') as f:
    Configs = f.readlines()
print (Configs)

R1 = {'device_type': 'cisco_ios',
    'ip': '192.168.0.22',
    'username': 'iiipyuser1',
    'password': 'Py01Pass'}

net_connect = ConnectHandler(**R1)

output = net_connect.send_config_set(Configs)
net_connect.disconnect()

print (output)