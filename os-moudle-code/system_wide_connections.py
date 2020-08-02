import psutil
import pprint






def get_connections():
	pprint.pprint(psutil.net_connections())






if __name__ == "__main__":
	get_connections()