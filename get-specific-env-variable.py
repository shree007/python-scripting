import os
import pprint



def driver():
	# get env variable
	pprint.pprint(os.environ.get('JAVA_HOME'))

	# adding new env variable
	os.environ['zero'] = 'shree'
	pprint.pprint(os.environ['zero'])

	# modify env variable

	os.environ['zero']='prakash'
	pprint.pprint(os.environ['zero'])



if __name__ == "__main__":
	driver()