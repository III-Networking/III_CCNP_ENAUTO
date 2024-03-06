from netmiko import ConnectHandler

cisco_csr1000 = {
    'device_type': 'cisco_ios',
    'host':   '192.168.0.22',
    'username': 'iiipyuser1',
    'password': 'Py01Pass',
    'port' : 22,
    'secret': '',
}

net_connect = ConnectHandler(**cisco_csr1000)

config_commands = [ 'int lo0',
                    'ip add 10.1.10.1 255.255.255.255',
                    'desc configuredByNetmiko' ]
output = net_connect.send_config_set(config_commands)
print(output)