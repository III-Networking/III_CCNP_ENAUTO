import xmltodict

with open("xml_sample.xml") as data:
    xml_example = data.read()

xml_dict = xmltodict.parse(xml_example)

print(xml_dict)

#print(xmltodict.unparse(xml_dict, pretty=True))

#to modify an element
'''xml_dict["interface"]["ipv4"]["address"]["ip"] = "192.168.55.3"'''
#run the uinparse again and check

#write changes to the xml file
'''with open("xml_sample.xml", "w") as data:
    data.write(xmltodict.unparse(xml_dict, pretty=True))'''