import os
import pprint



def driver():
	pprint.pprint(os.environ.get('JAVA_HOME'))


if __name__ == "__main__":
	driver()