import os

if __name__ == '__main__':
    try:
        file_path=input("enter file name: ").strip()
        current_permission = os.stat(file_path).st_mode
        print("Current permission is: ",current_permission)
        if os.path.isfile(file_path):
            os.chmod(file_path,755) 
            print("file permission has been changed: ", os.stat(file_path).st_mode)
    except Exception as e:
        print("Invalid file name, check if it is already exists: ",e)