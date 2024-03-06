from netmiko import ConnectHandler

cisco_Router = {
    'device_type': 'cisco_ios',
    'host':   '192.168.0.22',
    'username': 'iiipyuser1',
    'password': 'Py01Pass',
    'port' : 22,
    'secret': '',
}

net_connect = ConnectHandler(**cisco_Router)

output = net_connect.send_command('show ip int brief')
print(output)