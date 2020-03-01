import os


def driver():
	print("current Directory:", os.getcwd())

	# change the directory
	os.chdir('/home/prakash')
	# current directory
	print(os.getcwd())





if __name__ == "__main__":
	driver()