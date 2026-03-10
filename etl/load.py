import json

def load_data(rows, path="data/output.json"):
    with open(path, 'w') as jsonfile:
        json.dump(rows, jsonfile, indent=2)