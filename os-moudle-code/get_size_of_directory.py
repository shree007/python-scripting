import os
import humanize

def get_directory_size(directory_name):
    total_size = 0 
    for dirpath, subdirectory,filenames in os.walk(directory_name):
        for file in filenames:
            complete_path = os.path.join(dirpath,file)
            total_size += os.path.getsize(complete_path)
    if total_size == 0:
        print("Directory is empty")
    print("Directory size is: ",humanize.naturalsize(total_size))

if __name__ == '__main__':
    try:
        directory_name = input("Enter directory path: ").strip()
        if len(directory_name) != 0 and os.path.isdir(directory_name):
            get_directory_size(directory_name)
        else:
            print("Either Directory is empty or not exists")
    except Exception as e:
        print("Invalid Directory and File extentions",e)