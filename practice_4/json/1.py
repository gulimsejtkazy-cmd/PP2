import json


with open("sample-data.json", "r") as file:# with → file will be closed automatically
<<<<<<< HEAD
    data = json.load(file)# JSON → Python dictionary
=======
    data = json.load(file) # JSON → Python dictionary
>>>>>>> dfe6ec9 (json)


print("Interface Status")
print("=" * 80)
print(f"{'DN':50} {'Description':20} {'Speed':8} {'MTU':6}")
print("-" * 80)


for item in data["imdata"]: #We bypass the "imdata" list in the data dictionary
<<<<<<< HEAD
=======

>>>>>>> dfe6ec9 (json)
    attr = item["l1PhysIf"]["attributes"]

    dn = attr["dn"]
    descr = attr["descr"]
    speed = attr["speed"]
    mtu = attr["mtu"]

    print(f"{dn:50} {descr:20} {speed:8} {mtu:6}")
