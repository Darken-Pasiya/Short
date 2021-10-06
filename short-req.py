import os,sys

print("\033[32m [+] Installing Requirements...\033[0m")
print()

os.system("pip install --upgrade pip")
os.system("pkg upgrade && pkg update")
os.system("pkg install python -y ")
os.system("pkg install python2 -y")
os.system("pip install requests")
os.system("pip install pyshorteners")
os.system("pip install socket")
os.system("pip install json")
os.system("sleep 1")
os.system("clear")
print("")
print("")
print("\033[1;36m[+] Now Run :- \033[1;32mpython short.py \033[1;37m and press enter \033[0m")
print("")
