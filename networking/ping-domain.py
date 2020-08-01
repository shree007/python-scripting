import os

def verbose_ping(domain):
	executabel_stmt = "ping "+ domain
	os.system(executabel_stmt)



if __name__ == "__main__":
	print("please enter the domain name")
	domain= input()
	verbose_ping(domain)