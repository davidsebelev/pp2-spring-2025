import json


with open('sample-data.json') as file:
    data = json.load(file)


print("Interface Status")
print("=" * 79)
print("{:<50} {:<20} {:<8} {:<6}".format("DN", "Description", "Speed", "MTU"))
print("-" * 79)


for item in data['imdata']:
    attributes = item['l1PhysIf']['attributes']  


    dn = attributes.get('dn', '')
    descr = attributes.get('descr', '')  
    speed = attributes.get('speed', '')
    mtu = attributes.get('mtu', '')


    print("{:<50} {:<20} {:<8} {:<6}".format(dn, descr, speed, mtu))
