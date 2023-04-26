#help
#about
#start --> 
#		-exit exit of course
#		-all  descrever como será o processo antes de fazer tudo
#		-port portscan
#		-ports portscan in multiple ports
#		-search search about the target
#		-extra -->
#                   -back exit
#					-list list creation
#					-server create a server on local machine
#					-html html content about the provided domain
#

import time
from fsetup import BannerStart
from fsetup import All
from fsetup import Search
from fsetup import Port
from fsetup import Ports
from fsetup import Help
from fsetup import Extra
from fsetup import ExtraBanner
from fsetup import ALERT

BannerStart()
time.sleep(1)

key = True
while key == True:
	
	time.sleep(0.5)
	
	pointer = '\n\033[36m[::start::] \033[m> '
	opt = str(input(pointer))
	opt_start = opt.replace('start -','')

	if opt_start.lower() == 'all':

		ALERT()
		All()

	elif opt_start.lower() == 'port':

		ALERT()
		Port()

	elif opt_start.lower() == 'ports':
		
		ALERT()
		Ports()

	elif opt_start.lower() == 'search':

		ALERT()
		Search()

	elif opt_start.lower() == 'extra':

		ExtraBanner()
		Extra()

	elif opt.lower() == 'help':
		
		Help()

	elif opt.lower() == 'banner':

		BannerStart()

	elif opt.lower() == 'exit':

		print("See you later!")
		time.sleep(1)
		break

	else:
		print("Please, set a available command!")
