import json

def process_ndjson(file_path):
    data_objects = []
    
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines[:-1]:  # Skip the last line
            json_data = json.loads(line)
            data_objects.append(json_data)
    
    output_data = {"dataObjects": data_objects}
    
    with open("output.json", "w") as outfile:
        json.dump(output_data, outfile)

if __name__ == "__main__":
    ndjson_file_path = input("Enter the path to your NDJSON file: ")
    process_ndjson(ndjson_file_path)
