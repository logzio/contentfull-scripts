import json

def update_fields(data):
    if isinstance(data, dict):
        for key, value in data.items():
            if key == "fullName" or key == "username":
                data[key] = "logz_prebuilt_content"
            else:
                update_fields(value)
    elif isinstance(data, list):
        for item in data:
            update_fields(item)

def process_ndjson(file_path):
    data_objects = []

    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines[:-1]:  # Skip the last line
            json_data = json.loads(line)
            update_fields(json_data)  # Update fields in each JSON object
            data_objects.append(json_data)

    output_data = {"dataObjects": data_objects}

    with open("output.json", "w") as outfile:
        json.dump(output_data, outfile, indent=2)

if __name__ == "__main__":
    ndjson_file_path = input("Enter the path to your NDJSON file: ")
    process_ndjson(ndjson_file_path)

