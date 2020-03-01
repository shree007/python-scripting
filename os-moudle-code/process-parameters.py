import os
import pprint


def driver():
	# process parameters
	pprint.pprint(os.ctermid()) # return corressponding file name

	# return effective group id of cureent process
	pprint.pprint(os.getegid())

	# get effective user id of current process
	pprint.pprint(os.geteuid())

	# get real group id of current process
	pprint.pprint(os.getgid())

	# get real user id of current process
	pprint.pprint(os.getuid())

	# get logged in username
	pprint.pprint(os.system('whoami'))

	# get pid of group
	pprint.pprint(os.getpgid(os.getpid()))

	#


if __name__ == "__main__":
	driver()