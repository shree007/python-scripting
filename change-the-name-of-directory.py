import os


def driver():
	dir_name="test-one" # this folder will be created 
	change_name="test-two" # this folder will be renamed with dir_name
	create_dir(dir_name)

	#check directory created or not
	listname=os.listdir('.')
	print(listname)

	if dir_name in listname:
		os.rename(dir_name, change_name)
		print("after creation", os.listdir())

# creation of folder
def create_dir(dir_name):
	os.mkdir(dir_name)


#main method
if __name__ == "__main__":
	driver()