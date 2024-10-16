import os
import pprint

def find_files(directory_name,extention_name):
    list_of_files = []
    for dirpath, subdirectory, filenames in os.walk(directory_name):
        for file in filenames:
            if file.endswith(extention_name):
                complete_path = os.path.join(dirpath,file)
                list_of_files.append(complete_path)
    if len(list_of_files) != 0:
        pprint.pprint(list_of_files)
    else:
        print("No file found with exception: ",extention_name)

if __name__ == '__main__':
    try:
        directory_name = input("Enter directory path: ").strip()
        extention_name = input("Enter file extension: ").strip()
        if len(directory_name) != 0 and len(extention_name) != 0:
            find_files(directory_name,extention_name)
        else:
            print("Either Directory or File extention is empty")

    except Exception as e:
        print("Invalid Directory and File extentions",e)