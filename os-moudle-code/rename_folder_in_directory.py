import os

def rename_folder(directory_name,original_folder_name,new_folder_name):
    for dirpath, directory, filenames in os.walk(directory_name):
        complete_path = os.path.join(dirpath,original_folder_name)
        if os.path.exists(complete_path):
            new_path = os.path.join(dirpath,new_folder_name)
            os.rename(complete_path,new_path)
            return True
    return False


if __name__ == '__main__':
    try:
        directory_name=input("enter directory name: ").strip()
        original_folder_name=input("enter folder name: ").strip()
        new_folder_name=input("enter folder name which you want to change").strip()
        if len(directory_name) != 0 and os.path.isdir(directory_name):
            result = rename_folder(directory_name,original_folder_name,new_folder_name)
            if result:
                print("Directory has been created:  ",result)
            else:
                print("Given path is not directory: ", result)
    except Exception as e:
        print("Invalid directory name, check if it is already exists: ",e)