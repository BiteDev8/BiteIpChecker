from colorama import Fore, Back, Style, init
import random
import pyfiglet
Titre = "BiteIpChecker"
ASCII_art_1 = pyfiglet.figlet_format(Titre)
print(ASCII_art_1)
init()
print(Fore.GREEN+"enter ip :")

def port():
	a="1234567890"
	b="3456787"
	first = ''.join((random.choice(b)for i in range(1)))
	second = ''.join((random.choice(b)for i in range(4)))
	result = first+second

	return result

def pay():
	p=["france","spanish","Algeria","Egypt","Morocco","Sudan","Belgium","France","Germany","Italy","Portugal","United Kingdom","Spain","Mexico","United States","China"]
	payss = ''.join((random.choice(p)for i in range(1)))
	resultt = payss
	return resultt
pays = pay()
x = input()
e = len(x)
z=0
while z < 1000 :
	z+=1
	print(Fore.RED+port())
if e <= 7 or e >= 16 :
	print(Fore.GREEN+"invalid ip")
else :
	print(Fore.GREEN+"port :",port())
	print("pays :",pays)
	
