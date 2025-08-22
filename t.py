import json

# Replace with your JSON file path
file_path = "/Users/yc.keng/Documents/misc/MabayaDataFlatten/yodobashi-7030-snapshot.json"

data = []
with open(file_path, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line:  # skip empty lines
            data.append(json.loads(line))

print(f"Loaded {len(data)} records")
print(data[:2])  # preview first 2

