import json

# Read data from sample-data.json
with open("sample-data.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Print table title
print("Interface Status")
print("=" * 80)

# Print table headers
print(f"{'DN':<50} {'Description':<20} {'Speed':<8} {'MTU':<8}")
print(f"{'-' * 50} {'-' * 20} {'-' * 8} {'-' * 8}")

# Loop through all interfaces
for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]

    dn = attributes["dn"]
    description = attributes["descr"]
    speed = attributes["speed"]
    mtu = attributes["mtu"]

    print(f"{dn:<50} {description:<20} {speed:<8} {mtu:<8}")