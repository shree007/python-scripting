import os


def driver():
	dir_name="test"
	# check directory is there or not
	listdir=os.listdir()
	if dir_name in listdir:
		os.rmdir(dir_name)



if __name__ == "__main__":
	driver()