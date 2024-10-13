import yaml # install: python3 -m pip install --break-system-packages pyyaml

config = {
    'database': 'nosql',
    'application': 'golang',
    'frontend': 'react'
}

def read_yaml_file(yaml_file_name):
    with open(yaml_file_name, 'r') as file:
        content = yaml.safe_load(file)
    print("Content in file is %\n", content)

def write_yaml_file():
    with open('output_config.yaml', 'w') as file:
        yaml.dump(config, file)
    print("Yaml file has been written")

def validate_yaml_extension(filename):
    if not filename.endswith('.yaml'):
        filename += '.yaml'
    return filename

if __name__ == '__main__':
    try:
        yaml_file_name = input("enter yaml file name").strip()
        if len(yaml_file_name) != 0:
            yaml_file_name = validate_yaml_extension(yaml_file_name)
            print("File name ", yaml_file_name)
            read_yaml_file(yaml_file_name)
            write_yaml_file()
    except e:
        print("Invalid file name", e)