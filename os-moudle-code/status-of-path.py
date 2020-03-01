import os



def driver():
	path="simple.py"
	print(os.stat(path))


if __name__ == "__main__":
	driver()