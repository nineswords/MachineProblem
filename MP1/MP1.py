import csv

csv_file_path = 'child-health-indicators-for-philippines-41.csv'

with open(csv_file_path, 'r') as file:
    csv_reader = csv.reader(file)

    # Skip the header row
    header = next(csv_reader)

    for row in csv_reader:
        print(row)
