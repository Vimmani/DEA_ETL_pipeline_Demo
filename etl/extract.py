import csv

def extract_data(path ="data/input.csv"):
    rows = []
    with open(path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for r in reader:
            rows.append(r)

    ## These changes are done to test the Feature Extract Step branch
    ## These second changes are done to test the Feature Extract Step branch
    return rows
    