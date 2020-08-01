import socket
import dns.resolver



def run_basic(domain_name):
	for rdata in dns.resolver.resolve(domain_name, 'CNAME'):
		print(rdata.target)

	resolver = dns.resolver.Resolver()
	resolver.nameservers=[socket.gethostbyname('ns1.'+domain)]
	for rdata in resolver.query(domain_name, 'CNAME') :
		print(rdata.target)




if __name__ == "__main__":
	print("enter the domain")
	domain_name = input()
	run_basic(domain_name)