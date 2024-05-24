
import csv
import json

def csv_to_json(csv_file_path, json_file_path):
    '''Convert CSV file to JSON file.'''
    data = []
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    with open(json_file_path, 'w') as jsonfile:
        json.dump(data, jsonfile, indent=4)
    print(f"JSON file saved to {json_file_path}")

if __name__ == "__main__":
    csv_file_path = "input.csv"  # Path to the input CSV file
    json_file_path = "output.json"  # Path to save the output JSON file
    csv_to_json(csv_file_path, json_file_path)
