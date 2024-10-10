import json

def read_data_from_json(json_file_name):
    with open(json_file_name, 'r') as file:
        data = json.load(file)
    print(data)

def validate_json_extension(filename):
    if not filename.endswith('.json'):
        filename += '.json'
    return filename

if __name__ == '__main__':
    try:
        json_file_name = input("Enter json file name").strip()
        if len(json_file_name) != 0:
            json_file_name = validate_json_extension(json_file_name)
            read_data_from_json(json_file_name)
    except e:
        print("Invalid file name", e)