import os

if __name__ == '__main__':
    try:
        file_path=input("enter file name: ").strip()
        if os.path.isfile(file_path):
           print("File infomration: ", os.stat(file_path))
        print("Current Directory is: ", os.getcwd())
        print("System logged in by: ",os.getlogin())
    except Exception as e:
        print("Invalid file name, check if it is already exists: ",e)

