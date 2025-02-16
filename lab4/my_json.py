import json


with open("sample-data.json", "r") as f:
    data = json.load(f)

print("Interface Status")
print("=" * 80)
print("{:<50} {:<20} {:<7} {:<5}".format("DN", "Description", "Speed", "MTU"))
print("{:<50} {:<20} {:<7} {:<5}".format("-" * 50, "-" * 20, "-" * 7, "-" * 5))


desired_ids = ["eth1/33", "eth1/34", "eth1/35"]

for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]

    if attributes["id"] in desired_ids:
        dn = attributes.get("dn", "")
        descr = attributes.get("descr", "")
        speed = attributes.get("speed", "")
        mtu = attributes.get("mtu", "")
        print("{:<50} {:<20} {:<7} {:<5}".format(dn, descr, speed, mtu))
