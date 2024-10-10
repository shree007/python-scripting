import os

def  createfile(filename):
    try:
        print("File " + filename + " is being created.... ")
        with open(filename, 'w') as file:
            file.write("Hello work")
        print("File "+ filename + " has been created...")
    except:
        print("File can't be created")

def readfile(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        print("content in file is",content)
    except:
        print("Invaild Read attempt")

def appendtext(filename):
    try:
        with open(filename, 'a') as file:
            file.write("workloading")
        print(" file has been appened")
    except:
        print("invalid")

def renamefile(filename):
    new_filename = input("Enter the file name")
    try:
        os.rename(filename, new_filename)
        print(filename + " has been renamed to " + new_filename)
    except:
        print("Error: Invaild filename")

def deletefile():
    filename = input("Enter the file name")
    try:
        os.remove(filename)
        print("File " + filename + " has been delete")
    except:
        print("Invalid file operations")

if __name__ == '__main__':
    try:
        print("enter the file name")
        filename = input()
        if len(filename) != 0:
            print("file name is", filename)
            createfile(filename)
            readfile(filename)
            appendtext(filename)
            renamefile(filename)
            deletefile()
    except:
        print("file name is invalid")
