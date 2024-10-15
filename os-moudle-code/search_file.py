import os

def get_file(directory_name,search_file):
    for dirpath, directory, filenames in os.walk(directory_name):
        if search_file in filenames:
            return os.path.join(dirpath,search_file)
    return None

if __name__ == '__main__':
    try:
        directory_name = input("Enter directory path").strip()
        search_file    = input("Enter file name").strip()
        if len(directory_name) != 0 and len(search_file) != 0:
            print(" directory name: " + directory_name + "  file name need to be search: " + search_file)
            result=get_file(directory_name,search_file)
            if result:
                print(f"'{search_file}' has been found in '{result}'")
            else:
                print("File not found")
    except Exception as e:
        print("Invalid directory name", e)