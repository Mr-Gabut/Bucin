import time
import os
import sys

def mengetik(c):
  c = c + '\n'
  for x in c:
    time.sleep(0.1)
    print(x, end='', flush=True)
def loading():
  load = '~'
  count = 0
  pros = "\rLoading "
  for x in range(10):
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
    mengetik("Aku Juga Sayang")
  elif(pi=='2'): 
    loading()
    mengetik("Mungkin Nanti kamu bakal sayang")
  else:
    time.sleep (3)
    print("Pilih yang bennar!")
pil()
