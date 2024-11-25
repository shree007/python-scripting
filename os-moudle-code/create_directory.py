
import os

def create_directory(directory_name):
    os.makedirs(directory_name, exist_ok=True)
    if os.path.exists(directory_name):
        return (f"'{directory_name}'")
    return None

if __name__ == '__main__':
    try:
        directory_name=input("enter directory name: ").strip()
        if len(directory_name) != 0:
            print("Directory need to be created ",directory_name)
            create_directory(directory_name)
            result = create_directory(directory_name)
            if result:
                print("Directory has been created:  ", result)
            else:
                print("Directory can not be created: ", result)
    except Exception as e:
        print("Invalid directory name, check if it is already exists: ",directory_name)
