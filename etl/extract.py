import csv

def extract_data(path ="data/input.csv"):
    rows = []
    with open(path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for r in reader:
            rows.append(r)
    return rows
    