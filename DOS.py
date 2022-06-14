import sys
import os
import time
import socket
import random



ired="\033[0;91m"         # Red
igreen="\033[0;92m"       # Green
iblue="\033[0;94m"        # Blue

os.system("clear")

os.system("figlet DOS Attack")

print('''\nRihan DOS Tools''')

ip = raw_input("'IP Target : '")
port = input("Port       : ")

os.system("clear")

os.system("figlet Attack Starting")
print "[                    ] 0% "
time.sleep(5)
print "[=====               ] 25%"
time.sleep(5)
print "[==========          ] 50%"
time.sleep(5)
print "[===============     ] 75%"
time.sleep(5)
print "[====================] 100%"
time.sleep(3)


i = 1

while i<=500000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000:
	if i%1 == 0:
		print(str(i)+str(ired+''' Start send  Package '''))
		
	i = i + 1