import yaml

with open("yaml_sample.yaml") as data:
    yaml_sample = data.read()

yaml_dict = yaml.load(yaml_sample, Loader=yaml.FullLoader)

print(yaml_dict)

#changing interface name within python
'''yaml_dict["interface"]["name"] = "GigabitEthernet1"
print(yaml.dump(yaml_dict, default_flow_style=False))'''

#To write these changes back to your file
'''with open("yaml_sample.yaml", "w") as data:
    data.write(yaml.dump(yaml_dict, default_flow_style=False))'''