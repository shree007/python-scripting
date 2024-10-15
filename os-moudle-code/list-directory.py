import os

def get_files(directory_name):
    return os.listdir(directory_name)

if __name__ == '__main__':
    try:
        directory_name = input("Enter directory name: ").strip()
        if len(directory_name) != 0:
            list_of_files = get_files(directory_name)
            if len(list_of_files) != 0:
                print(list_of_files)
            else:
                print("Directory is empty")
        else:
            print("Empty Directory")
    except Exception as e:
        print("Invalid Directory", e)
