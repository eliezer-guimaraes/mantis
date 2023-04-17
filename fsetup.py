import whois
import time
import socket
import nmap3
import requests

def ALERT():

	time.sleep(2)
	print("\n-----------------------------------------ALERT PANEL--------------------------------------------")
	print("\nHello, and welcome to the Alert Panel. Here we will make some requests in the domain provided.\nTherefore, I ask that you remain protected ;)")
	print("\n------------------------------------------------------------------------------------------------\n")

def BannerStart():
	
	print(" __  __ ___ __  _ _____ _ ____      ")
	print("|  \/  | . |  \| |_   _| |  __|     ")
	print("| |\/| |   | |\  | | | | |___ |  _   _   _")
	print("|_|  |_|_|_|_| |_| |_| |_|____| |_| |_| |_|")
	print("\nMantis V.1  -  Eliezer Guimarães (https://github.com/eliezer-guimaraes)")
	print("\033[7;36mI am not responsible for the misuse of the tool!\033[0;m")


def All():

	time.sleep(2)
	pointer_search = '\033[36m[::all::] \033[m> '

	time.sleep(0.8)
	print("Starting...")
	time.sleep(0.8)

	print("\nPlease, set the domain name below:")
	domain_name = str(input(pointer_search))

	#------------------------------------------------ORG
	time.sleep(1)
	org_info = whois.whois(domain_name).org

	print("\nOrganization name :  {}\n".format(org_info))

	#---------------------------------------------SERVERS
	time.sleep(1)
	name_servers = whois.whois(domain_name).name_servers

	print("\n\033[7;38m              SERVERS              \033[1;m\n")
	for i in name_servers:
		print("SERVER :   {}".format(i))
		time.sleep(0.15)

	#----------------------------------INTERNET PROTOCOLS
	time.sleep(1)
	
	nmap = nmap3.Nmap()
	results = nmap.nmap_dns_brute_script(domain_name)
	#print(results)
	#print(len(results))

	color_init_yellow = '\033[33m'
	color_end = '\033[0;0m'

	print("\n\033[7;38m                                IPs                               \033[1;m\n")
	list = range(0, int(len(results)))
	for i in list:
		#print(results[i])
		print("\033[1;33mhostname\033[m :   {},  \033[1;33mIP\033[m :   {}".format(results[i]['hostname'], results[i]['address']))
		time.sleep(0.1)

	#----------------------------------DATE INFORMATIONS
	time.sleep(1)
	u_date = whois.whois(domain_name).updated_date
	c_date = whois.whois(domain_name).creation_date
	e_date = whois.whois(domain_name).expiration_date

	print("\n\033[7;38m           DATE INFORMATIONS             \033[1;m\n")
	time.sleep(0.15)
	print("Updated date    :   {}".format(u_date))
	print("Creation date   :   {}".format(c_date))
	print("Expiration date :   {}".format(e_date))

	#-------------------------------------------PORTSCAN
	time.sleep(1)
	print("\n\033[7;38m                      PORT INFORMATION                      \033[1;m\n")
	range_port = [20, 21, 22, 23, 25, 43, 53, 69, 80, 110, 123, 318, 411, 412, 433, 989, 990, 1194, 1241, 2483, 2484,3124, 3306, 4333, 5500, 6665, 6669, 6679, 6697, 8080,]
	print("Default ports: {}".format(range_port))

	add = str(input("Do you want to add a new port? (yes/no): "))

	time.sleep(1)
	print("Please wait, this may take some time...")
	if add.lower() == 'yes':

		new_port = int(input("\nSet a new port: "))
		range_port.append(new_port)

		for p0rt in range_port:

			client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			client.settimeout(5)
			code = client.connect_ex((domain_name, p0rt))

			if code == 0:
				time.sleep(2)
				print("\nPORT : {},       SITUATION : \033[7;32m OPEN \033[m".format(p0rt))
			else:
				print("\nPORT : {},       SITUATION : \033[7;31m CLOSED \033[m".format(p0rt))
		else:
			pass
	elif add.lower() == 'no':

		for p0rt in range_port:

			client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			client.settimeout(5)
			code = client.connect_ex((domain_name, p0rt))

			if code == 0:
				time.sleep(2)
				print("\nPORT : {},       SITUATION : \033[7;32m OPEN \033[m".format(p0rt))
			else:
				print("\nPORT : {},       SITUATION : \033[7;31m CLOSED \033[m".format(p0rt))
		else:
			pass
	else:
		pass

def Search():

	time.sleep(2)
	pointer_search = '\033[36m[::search::] \033[m> '

	time.sleep(0.8)
	print("Starting...")
	time.sleep(0.8)

	print("\nPlease, set the domain name below:")
	domain_name = str(input(pointer_search))

	#------------------------------------------------ORG
	time.sleep(1)
	org_info = whois.whois(domain_name).org

	print("\nOrganization name :  {}\n".format(org_info))

	#---------------------------------------------SERVERS
	time.sleep(1)
	name_servers = whois.whois(domain_name).name_servers

	print("\n\033[7;38m              SERVERS              \033[1;m\n")
	for i in name_servers:
		print("SERVER :   {}".format(i))
		time.sleep(0.15)

	#----------------------------------INTERNET PROTOCOLS
	time.sleep(1)
	
	nmap = nmap3.Nmap()
	results = nmap.nmap_dns_brute_script(domain_name)
	#print(results)
	#print(len(results))

	color_init_yellow = '\033[33m'
	color_end = '\033[0;0m'

	print("\n\033[7;38m                                IPs                               \033[1;m\n")
	list = range(0, int(len(results)))
	for i in list:
		#print(results[i])
		print("\033[1;33mhostname\033[m :   {},  \033[1;33mIP\033[m :   {}".format(results[i]['hostname'], results[i]['address']))
		time.sleep(0.1)

	#----------------------------------DATE INFORMATIONS
	time.sleep(1)
	u_date = whois.whois(domain_name).updated_date
	c_date = whois.whois(domain_name).creation_date
	e_date = whois.whois(domain_name).expiration_date

	print("\n\033[7;38m           DATE INFORMATIONS             \033[1;m\n")
	time.sleep(0.15)
	print("Updated date    :   {}".format(u_date))
	print("Creation date   :   {}".format(c_date))
	print("Expiration date :   {}".format(e_date))

	#-------------------------------------------PORTSCAN
	time.sleep(1)
	print("\n\033[7;38m                     PORTS INFORMATIONS                     \033[1;m\n")
	range_port = [20, 21, 22, 23, 25, 43, 53, 69, 80, 110, 123, 318, 411, 412, 433, 989, 990, 1194, 1241, 2483, 2484,3124, 3306, 4333, 5500, 6665, 6669, 6679, 6697, 8080,]
	print("Default ports: {}".format(range_port))

	add = str(input("Do you want to add a new port? (yes/no): "))

	time.sleep(1)
	print("Please wait, this may take some time...")
	if add.lower() == 'yes':

		new_port = int(input("\nSet a new port: "))
		range_port.append(new_port)

		for p0rt in range_port:

			client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			client.settimeout(5)
			code = client.connect_ex((domain_name, p0rt))

			if code == 0:
				time.sleep(2)
				print("\nPORT : {},       SITUATION : \033[7;32m OPEN \033[m".format(p0rt))
			else:
				print("\nPORT : {},       SITUATION : \033[7;31m CLOSED \033[m".format(p0rt))
		else:
			pass
	elif add.lower() == 'no':

		for p0rt in range_port:

			client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			client.settimeout(5)
			code = client.connect_ex((domain_name, p0rt))

			if code == 0:
				time.sleep(2)
				print("\nPORT : {},       SITUATION : \033[7;32m OPEN \033[m".format(p0rt))
			else:
				print("\nPORT : {},       SITUATION : \033[7;31m CLOSED \033[m".format(p0rt))
		else:
			pass
	else:
		pass

def Ports():

	#-------------------------------------------PORTSCAN
	time.sleep(1)
	range_port = [20, 21, 22, 23, 25, 43, 53, 69, 80, 110, 123, 318, 411, 412, 433, 989, 990, 1194, 1241, 2483, 2484,3124, 3306, 4333, 5500, 6665, 6669, 6679, 6697, 8080,]
	print("Default ports: {}".format(range_port))

	domain_name = str(input("\033[36m[::domain::] \033[m> "))
	add = str(input("Do you want to add a new port? (yes/no): "))

	time.sleep(1)
	print("Please wait, this may take some time...")
	print("\n\033[7;38m                      PORT INFORMATION                      \033[1;m\n")

	if add.lower() == 'yes':

		new_port = int(input("\n\033[36m[::new_port::] \033[m> "))
		range_port.append(new_port)

		for p0rt in range_port:

			client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			client.settimeout(5)
			code = client.connect_ex((domain_name, p0rt))

			if code == 0:
				time.sleep(2)
				print("\nPORT : {},       SITUATION : \033[7;32m OPEN \033[m".format(p0rt))
			else:
				print("\nPORT : {},       SITUATION : \033[7;31m CLOSED \033[m".format(p0rt))
		else:
			pass
	elif add.lower() == 'no':

		for p0rt in range_port:

			client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			client.settimeout(5)
			code = client.connect_ex((domain_name, p0rt))

			if code == 0:
				time.sleep(2)
				print("\nPORT : {},       SITUATION : \033[7;32m OPEN \033[m".format(p0rt))
			else:
				print("\nPORT : {},       SITUATION : \033[7;31m CLOSED \033[m".format(p0rt))
		else:
			pass
	else:
		pass

def Port():

	#-------------------------------------------PORTSCAN
	time.sleep(1)
	
	pointer = '\033[36m[::port::] \033[m> '
	domain_name = str(input("\033[36m[::domain::] \033[m> "))

	set_port = int(input(pointer))
	set_port_interable = [set_port]
	time.sleep(1)
	
	print("\n\033[7;38m                      PORT INFORMATION                      \033[1;m\n")
	for p0rt in set_port_interable:

		client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		client.settimeout(5)
		code = client.connect_ex((domain_name, p0rt))

		if code == 0:
			time.sleep(2)
			print("\nPORT : {},       SITUATION : \033[7;32m OPEN \033[m".format(p0rt))
		else:
			print("\nPORT : {},       SITUATION : \033[7;31m CLOSED \033[m".format(p0rt))
	else:
		pass

def Help():

	print("----------------------------------------------------------------------------")
	print("\nMantis V.1 2023 -  Eliezer Guimarães (https://github.com/eliezer-guimaraes)")
	print("\n\033[7;33m ALERT! \033[m Hello, before you use the tool, make sure that you are protected!")
	print("\n>>> start <options>")
	print("\n OPTIONS")
	print("  -all        Run the program with all the tools")
	print("  -port       Do a simple port scanning with(or not) SSL")
	print("  -ports      Do a port scanning in multiple ports with(or not) SSL")
	print("  -search     Do a search in the provided domain name")
	print("  -extra      Show more tools in the program for your use, see below")
	print("\n EXTRA OPTIONS")
	print("  -list       Create a list with subdomains")
	print("  -enc        Encrypt")
	print("  -dec        Decrypt\n")
	print("----------------------------------------------------------------------------")