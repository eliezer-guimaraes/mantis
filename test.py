import requests
import time


def OK(domain_name):
	print("\n\033[7;38m                  SUBDOMAINS                   \033[1;m\n")
	opt_list = str(input("Do you want to use the default list? (yes/no): "))

	if opt_list.lower() == 'yes':
		
		opt_ssl = str(input("Do you want to try with SSL? (yes/no): "))

		if opt_ssl.lower() == 'yes':

			with open('common.txt', 'r') as wordlist:
				for line in wordlist:
					domain_req = requests.get("https://{}/{}".format(domain_name, line, end=''))
					if domain_req:
						print("\nFOUND : {}".format(domain_req))
					else:
						pass

		elif opt_ssl.lower() == 'no':

			with open('common.txt', 'r') as wordlist:
				for line in wordlist:
					domain_req = requests.get("http://{}/{}".format(domain_name, line, end=''))
					if domain_req:
						print("\nFOUND : {}".format(domain_req))
					else:
						pass
		else:
			print("Invalid command, trying with SSL...\n")

			with open('common.txt', 'r') as wordlist:
				for line in wordlist:

					domain_http_s = "https://{}/{}".format(domain_name, line, end='')
					domain_req = requests.get(domain_http_s)
					time.sleep(1)
					if domain_req:
						print("\nFOUND : {}".format(domain_req))
						print(domain_http_s)
					else:
						pass
	
	elif opt_list.lower() == 'no':

		list_path = str(input("\nSet the path or name to the desired list: "))
		opt_ssl = str(input("Do you want to try with SSL? (yes/no): "))

		if opt_ssl.lower() == 'yes':

			with open(list_path, 'r') as wordlist:
				for line in wordlist:
					domain_req = requests.get("https://{}/{}".format(domain_name, line, end=''))
					if domain_req:
						print("\nFOUND : {}".format(domain_req))
					else:
						pass

		elif opt_ssl.lower() == 'no':

			with open(list_path, 'r') as wordlist:
				for line in wordlist:
					domain_req = requests.get("http://{}/{}".format(domain_name, line, end=''))
					if domain_req:
						print("\nFOUND : {}".format(domain_req))
					else:
						pass
		else:
			print("Invalid command, trying with SSL...\n")

			with open(list_path, 'r') as wordlist:
				for line in wordlist:

					domain_http_s = "https://{}/{}".format(domain_name, line, end='')
					domain_req = requests.get(domain_http_s).content
					if domain_req:
						print("\nFOUND : {}".format(domain_req))
					else:
						pass

OK('www.geeksforgeeks.org')