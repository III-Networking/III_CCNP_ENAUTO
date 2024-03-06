import json

with open("json_sample.json") as data:
    json_data = data.read()

json_dict = json.loads(json_data)

print(json_dict)

#modify the json data
'''json_dict["interface"]["description"] = "Backup Link"
print(json_dict)'''

#to save json object to a file
'''with open("json_sample.json", "w") as fh:
    json.dump(json_dict, fh, indent = 4)'''

#loading json file and printing the output
'''with open ("json_sample.json") as data:
    json_data = data.read()
print(json_data)'''