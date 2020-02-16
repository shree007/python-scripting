import os
import pprint

def driver():
	data=os.environ
	pprint.pprint(dict(data), width=1)


if __name__ == "__main__":
	driver()