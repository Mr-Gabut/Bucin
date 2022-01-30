import time
import os
import sys

b="\033[0;34m"
g="\033[1;32m"
w="\033[1;37m"
r="\033[1;31m"
y="\033[1;33m"
cyan = "\033[0;36m"
lgray = "\033[0;37m"
dgray = "\033[1;30m"
ir = "\033[0;101m"
reset = "\033[0m"

time.sleep(2)
os.system('clear')
def mengetik(c):
  c = c + '\n'
  for x in c:
    time.sleep(0.2)
    print(x, end='', flush=True)
def loading():
  load = '~'
  count = 0
  pros = "\rLoading "
  for x in range(101):
    time.sleep(0.1)
    print(pros, load, x, "%", end="", flush=True)
    count += 1
    if count == 20:
      count = 0
      load += '~'
  time.sleep(2)
  print("\n", "\n")

def pil():
  nama=(input("[+] Nama kamu: "))
  print(nama, "sayang sama aku nggak?")
  time.sleep(2)
  print("[1]. Sayang")
  print("[2]. Enggak")
  pi=(input("[~] Pilih nomor 1/2 : "))
  if(pi=='1'): 
    loading()
    mengetik("Aku Juga Sayang Sama Kamu..")
  elif(pi=='2'): 
    loading()
    mengetik("Mungkin Nanti kamu bakal sayang")
  else:
    time.sleep (3)
    print("Pilih yang bennar!")
pil()
