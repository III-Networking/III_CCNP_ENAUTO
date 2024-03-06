from netmiko import ConnectHandler

R1 = {'device_type': 'cisco_ios',
    'ip': '192.168.0.22',
    'username': 'iiipyuser1',
    'password': 'Py01Pass'}

net_connect = ConnectHandler(**R1)

output = net_connect.send_command("show run | sec tel")
net_connect.disconnect()

print (output)