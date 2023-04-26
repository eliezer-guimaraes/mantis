import whois
import time
import socket
import nmap3
import requests
import os

def ALERT():

	time.sleep(2)
	print("\n-----------------------------------------ALERT PANEL--------------------------------------------")
	print("\nHello, and welcome to the Alert Panel. Here we will make some requests in the domain provided.\nTherefore, I ask that you remain protected ;)")
	print("\n------------------------------------------------------------------------------------------------\n")

def BannerStart():

	print("\n \033[0;34m m         m\033[m                                         " )
	time.sleep(0.1)
	print(" \033[0;34m mmmm   mmmm\033[m     ")
	time.sleep(0.1)
	print(" \033[0;34m mmmmm mmmmm\033[m                 __  _")
	time.sleep(0.1)
	print("\033[0;34m mmm  mmm  mmm\033[m   ____ _____  / /_(_)____")
	time.sleep(0.1)
	print("\033[0;34m mmm   m   mmm\033[m  / __ `/ __ \/ __/ / ___/")
	time.sleep(0.1)
	print(" \033[0;34m mm       mm\033[m  / /_/ / / / / /_/ (__  )  _   _   _")
	time.sleep(0.1)
	print(" \033[0;34m  mm     mm\033[m   \__,_/_/ /_/\__/_/____/  /_/ /_/ /_/   \n ")
	time.sleep(0.1)

	print("\n Mantis V.1  -  Eliezer Guimarães (https://github.com/eliezer-guimaraes)")
	print(" \033[7;36mI am not responsible for the misuse of the tool!\033[0;m")

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
	print("  -back       Exit")
	print("  -list       Create a list with subdomains")
	print("  -server     It opens a server on the localmachine")
	print("  -html       HTML content about the provided domain\n")
	print("----------------------------------------------------------------------------")

def ExtraBanner():

	time.sleep(0.8)
	print("\n---------------------------------------------------------------------------")
	print("                       WELCOME TO THE EXTRA PANEL                          ")
	print("               Set 'extra -help' for see the extra tools!                      ")
	print("---------------------------------------------------------------------------\n")

def Extra():

	key_extra = True
	while key_extra == True:


		pointer = '\033[33m[::extra::] \033[m> '
		extra_opt = str(input(pointer))
		extra = extra_opt.replace('extra -', '')

		if extra.lower() == 'help':
			
			print("----------------------------------------------------------------------------")
			print("\nEXTRA TOOLS")
			print("\n>>> extra <options>")
			print("\n OPTIONS")
			print("  -back       Exit")
			print("  -list       Create a list with subdomains")
			print("  -server     It opens a server on the local machine")
			print("  -html       HTML content about the provided domain\n")
			print("----------------------------------------------------------------------------")

		elif extra.lower() == 'list':

			time.sleep(0.5)
			print("\nSet a URL with the word 'MANTIS' to make the switch...")
			print("EXAMPLE: https://www.website.com/products/id=MANTIS\n")

			url = str(input("Set the URL: "))
			save = str(input("Set the name of the save file (with .txt): "))
			choice = str(input("Do you want to use an especific wordlist? (y/n): "))

			if choice.lower() == 'y':
				
				wordlist_name = str(input("\nSet the path or the name to the wordlist: "))
				time.sleep(0.5)
				print("Please, this may take some time...\n")

				with open(wordlist_name, 'r') as arch:
					for line in arch:
						with open(save, 'a') as wordlist:
							wordlist.write(url.replace('MANTIS', line))
							print(url.replace('MANTIS', line))
					time.sleep(0.7)
					print("---------------------------------------------------------------------------")
					print("List creation completed!")

			elif choice.lower() == 'n':
				
				print("\nOkay, let's use the default wordlist!")
				time.sleep(0.5)
				print("Please, this may take some time...\n")

				with open('common.txt', 'r') as arch:
					for line in arch:
						with open(save, 'a') as wordlist:
							wordlist.write(url.replace('MANTIS', line))
							print(url.replace('MANTIS', line))
					time.sleep(0.7)
					print("---------------------------------------------------------------------------")
					print("List creation completed!")
			else:

				print("\nSo, let's use the default wordlist!")
				time.sleep(0.5)
				print("Please, this may take some time...\n")
				time.sleep(1.8)

				with open('common.txt', 'r') as arch:
					for line in arch:
						with open(save, 'a') as wordlist:
							wordlist.write(url.replace('MANTIS', line))
							print(url.replace('MANTIS', line))
					time.sleep(0.7)
					print("---------------------------------------------------------------------------")
					print("List creation completed!")
							
		elif extra.lower() == 'server':
			
			time.sleep(0.5)
			print("\nThis will cause your computer to become a local server on the desired port\n")
			
			port = str(input("Set a desired port: "))
			time.sleep(0.5)

			def SERVER(value):

				print("\033[7;32m OPEN SERVER ON PORT {} \033[m".format(value))
				os.system('python3 -m http.server {}'.format(value))

			SERVER(port)

		elif extra.lower() == 'html':
			
			time.sleep(0.8)
			print("All page content will be saved in a .txt file!")
			domain_name = str(input("Set the URL: "))
			save_file = str(input("Set the name of the save file: "))

			#-------------------REQUEST
			res = requests.get(domain_name)

			#-------------------HEADERS
			time.sleep(0.4)
			print("\n\033[7;38m                          HEADERS                           \033[1;m\n")
			print(res.headers)
			
			with open('{}-headers.txt'.format(save_file), 'a') as HEADERS:
				HEADERS.write('{}'.format(res.headers))

			#-------------------HTML
			time.sleep(0.4)
			print("\n\033[7;38m                            HTML                            \033[1;m\n")
			print(res.text)

			with open('{}-html.txt'.format(save_file), 'a') as HTML:
				HTML.write('{}'.format(res.text))


		elif extra.lower() == 'back':
			break

		elif extra.lower() == 'exit':
			print("Did you mean 'back'?\n")
		else:
			print("Please, set a available command!\n")

 
