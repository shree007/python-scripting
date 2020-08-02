import socket



def nslookup(domain):
	print(socket.gethostbyname_ex(domain))

if __name__ == "__main__":
	print("enter the domain name")
	domain = input()
	nslookup(domain)