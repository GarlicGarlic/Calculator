print("\033[1;31m")
print("\033[0;30;49m\n")

import time
import sys
import math
import cmath

# for some reason I made 13 functions that all do the same thing

def fastLetter(words):
  for char in words:
    time.sleep(0.00000000001)
    sys.stdout.write(char)
    sys.stdout.flush()
    
def quickLettert5(words):
  for char in words:
    time.sleep(0.0005)
    sys.stdout.write(char)
    sys.stdout.flush()
    
def quickLetter1(words):
  for char in words:
    time.sleep(0.001)
    sys.stdout.write(char)
    sys.stdout.flush()
    
def quickLetter1t5(words):
  for char in words:
    time.sleep(0.0015)
    sys.stdout.write(char)
    sys.stdout.flush()
    
def quickLetter2(words):
  for char in words:
    time.sleep(0.002)
    sys.stdout.write(char)
    sys.stdout.flush()
    
def quickLetter2t5(words):
  for char in words:
    time.sleep(0.0025)
    sys.stdout.write(char)
    sys.stdout.flush()
    
def quickLetter3(words):
  for char in words:
    time.sleep(0.003)
    sys.stdout.write(char)
    sys.stdout.flush()
    
def quickLetter3t5(words):
  for char in words:
    time.sleep(0.0035)
    sys.stdout.write(char)
    sys.stdout.flush()
    
def quickLetter4(words):
  for char in words:
    time.sleep(0.004)
    sys.stdout.write(char)
    sys.stdout.flush()
    
def quickLetter6(words):
  for char in words:
    time.sleep(0.006)
    sys.stdout.write(char)
    sys.stdout.flush()
    
def quickLetter5(words):
  for char in words:
    time.sleep(0.005)
    sys.stdout.write(char)
    sys.stdout.flush()
    
def medLetter(words):
  for char in words:
    time.sleep(0.05)
    sys.stdout.write(char)
    sys.stdout.flush()
    
def midLetter(words):
  for char in words:
    time.sleep(0.025)
    sys.stdout.write(char)
    sys.stdout.flush()

# ascii art shown on startup
def calScreen():
  print("\033[0;37;1;33m\n")
  quickLettert5("                                        lllllll                                          lllllll                             tttt                                                 ")
  print("")
  quickLettert5("                                        l:::::l                                          l:::::l                          ttt:::t                                                 ")
  print("")
  quickLettert5("                                        l:::::l                                          l:::::l                          t:::::t                                                 ")
  print("")
  quickLetter1("                                        l:::::l                                          l:::::l                          t:::::t                                                 ")
  print("")
  quickLetter1("    cccccccccccccccc   aaaaaaaaaaaaa     l::::l      cccccccccccccccc uuuuuu    uuuuuu    l::::l    aaaaaaaaaaaaa   ttttttt:::::ttttttt        ooooooooooo    rrrrr   rrrrrrrrr   ")
  print("")
  quickLetter1("  cc:::::::::::::::c   a::::::::::::a    l::::l    cc:::::::::::::::c u::::u    u::::u    l::::l    a::::::::::::a  t:::::::::::::::::t      oo:::::::::::oo  r::::rrr:::::::::r  ")
  print("")
  quickLetter1t5(" c:::::::::::::::::c   aaaaaaaaa:::::a   l::::l   c:::::::::::::::::c u::::u    u::::u    l::::l    aaaaaaaaa:::::a t:::::::::::::::::t     o:::::::::::::::o r:::::::::::::::::r ")
  print("")
  quickLetter1t5("c:::::::cccccc:::::c            a::::a   l::::l  c:::::::cccccc:::::c u::::u    u::::u    l::::l             a::::a tttttt:::::::tttttt     o:::::ooooo:::::o rr::::::rrrrr::::::r")
  print("")
  quickLetter2("c::::::c     ccccccc     aaaaaaa:::::a   l::::l  c::::::c     ccccccc u::::u    u::::u    l::::l      aaaaaaa:::::a       t:::::t           o::::o     o::::o  r:::::r     r:::::r")
  print("")
  quickLetter2("c:::::c                aa::::::::::::a   l::::l  c:::::c              u::::u    u::::u    l::::l    aa::::::::::::a       t:::::t           o::::o     o::::o  r:::::r     rrrrrrr")
  print("")
  quickLetter2t5("c:::::c               a::::aaaa::::::a   l::::l  c:::::c              u::::u    u::::u    l::::l   a::::aaaa::::::a       t:::::t           o::::o     o::::o  r:::::r            ")
  print("")
  quickLetter3("c::::::c     ccccccc a::::a    a:::::a   l::::l  c::::::c     ccccccc u:::::uuuu:::::u    l::::l  a::::a    a:::::a       t:::::t    tttttt o::::o     o::::o  r:::::r            ")
  print("")
  quickLetter3t5("c:::::::cccccc:::::c a::::a    a:::::a  l::::::l c:::::::cccccc:::::c u:::::::::::::::uu l::::::l a::::a    a:::::a       t::::::tttt:::::t o:::::ooooo:::::o  r:::::r            ")
  print("")
  quickLetter4(" c:::::::::::::::::c a:::::aaaa::::::a  l::::::l  c:::::::::::::::::c  u:::::::::::::::u l::::::l a:::::aaaa::::::a       tt::::::::::::::t o:::::::::::::::o  r:::::r            ")
  print("")
  quickLetter5("  cc:::::::::::::::c  a::::::::::aa:::a l::::::l   cc:::::::::::::::c   uu::::::::uu:::u l::::::l  a::::::::::aa:::a        tt:::::::::::tt  oo:::::::::::oo   r:::::r            ")
  print("")
  quickLetter6("    cccccccccccccccc   aaaaaaaaaa  aaaa llllllll     cccccccccccccccc     uuuuuuuu  uuuu llllllll   aaaaaaaaaa  aaaa          ttttttttttt      ooooooooooo     rrrrrrr            ")
  print("\033[0;30;49m\n")

z=0
y=0
x=0
o=0
n1=0
n3=0
on=1
stop=0
calScreen()

def letterCal(o):    # yea I have no clue how this works
  
  if not o==0:
    n1=o
    n1=float(n1)
    midLetter("Please choose a function (+, -, x, /, ^ or !) (working on triangles, percentages and even more letters)")
    print("\033[0;36m\n")
    f=input("")
    print("\033[0;30;49m\n")
    n3=0
    if "!" in f:
      n1=int(n1)
      n3=int(n3)
      n3=n1
      while n1 > 1:
        n2=n1-1
        n3=n3*n2
        n1=n2
        stop = 1
        
    if "=" in f:
      n3=o
      stop=1
      
    if stop == 0:
      medLetter("Please choose a number or letters")
      print("\033[0;36m\n")
      n2=input("")
      print("\033[0;30;49m\n")
      if "x" in n2 and "y" in n2 and "z" in n2:
        x=float(x)
        y=float(y)
        z=float(z)
        n2=x*y*z
        n2=str(n2)
      if "x" in n2 and "y" in n2:
        x=float(x)
        y=float(y)
        n2=x*y
        n2=str(n2)
      if "y" in n2 and "z" in n2:
        y=float(y)
        z=float(z)
        n2=y*z
        n2=str(n2)
      if "z" in n2 and "x" in n2:
        z=float(z)
        x=float(x)
        n2=z*x
        n2=str(n2)
      if "x" in n2:
        n2=x
      if "y" in n2:
        n2=y
      if "z" in n2:
        n2=z
      n2=float(n2)
      if f == "+":
        n3=n1+n2
      if f == "/" or f == "÷":
        n3=n1/n2
      if f == "-":
        n3=n1-n2
      if f == "x" or f == "*":
        n3=n1*n2
      if f == "**" or f == "^":
        n3=n1**n2
      if f == "%":
        n3=n1*n2/100
        
      medLetter("Here's your answer:")
      print("")
      sys.stdout.write("\033[1;32m\n")
      n3=str(n3)
      fastLetter(n3)
      n3=float(n3)
      print("\033[0;30;49m\n")
      
  if o==0:
    if letter=="z":
      n1="z"
      
    medLetter("Please choose a number")
    print("\033[0;36m\n")
    n2=input("")
    sys.stdout.write("\033[0;30;49m\n")
    n3=n2
    o=n2
    sys.stdout.write("\033[1;32m\n")
    medLetter(n1 + " =")
    print("")
    print(n3)
    print("\033[0;30;49m\n")
    
while on == 1:
  medLetter("Please choose a number or letter")
  print("\033[0;36m\n")
  n1=input("")
  sys.stdout.write("\033[0;30;49m\n")
  if not "x" in n1 and not "y" in n1 and not "z" in n1 and not "sin" in n1 and not "cos" in n1 and not "tan" in n1 and not "quad" in n1:
    n1=float(n1)
    midLetter("Please choose a function (+, -, x, /, ^ or !)")
    print("\033[0;36m\n")
    f=input("")
    sys.stdout.write("\033[0;30;49m\n")
    n3=0
    stop=0
    if "!" in f:
      n1=int(n1)
      n3=int(n3)
      n3=n1
      while n1 > 1:
        n2=n1-1
        n3=n3*n2
        n1=n2
        stop=1
        
    if stop==0:
      medLetter("Please choose a number or letters")
      print("\033[0;36m\n")
      n2=input("")
      sys.stdout.write("\033[0;30;49m\n")
      if "x" in n2 and "y" in n2 and "z" in n2:
        x=float(x)
        y=float(y)
        z=float(z)
        n2=x*y*z
        n2=str(n2)
      if "x" in n2 and "y" in n2:
        x=float(x)
        y=float(y)
        n2=x*y
        n2=str(n2)
      if "y" in n2 and "z" in n2:
        y=float(y)
        z=float(z)
        n2=y*z
        n2=str(n2)
      if "z" in n2 and "x" in n2:
        z=float(z)
        x=float(x)
        n2=z*x
        n2=str(n2)
      if "x" in n2:
        n2=x
      if "y" in n2:
        n2=y
      if "z" in n2:
        n2=z
      n2=float(n2)
      if f == "+":
        n3=n1+n2
      if f == "/" or f == "÷":
        n3=n1/n2
      if f == "-":
        n3=n1-n2
      if f == "x" or f == "*":
        n3=n1*n2
      if f == "**" or f == "^":
        n3=n1**n2
      if f == "%":
        n3=n1*n2/100
        
      medLetter("Here's your answer:")
      print("")
      sys.stdout.write("\033[1;32m\n")
      n3=str(n3)
      fastLetter(n3)
      n3=float(n3)
      print("\033[0;30;49m\n")
      
  if n1=="x":
    if not x==0:
      n1=x
      n1=float(n1)
      midLetter("Please choose a function (+, -, x, /, ^ or !)")
      print("\033[0;36m\n")
      f=input("")
      sys.stdout.write("\033[0;30;49m\n")
      n3=0
      if "!" in f:
        n1=int(n1)
        n3=int(n3)
        n3=n1
        while n1 > 1:
          n2=n1-1
          n3=n3*n2
          n1=n2
          
        stop = 1
        
      if "=" in f:
        n3=x
        stop=1
        
      if stop == 0:
        medLetter("Please choose a number or letters")
        print("\033[0;36m\n")
        n2=input("")
        print("\033[0;30;49m\n")
        if "x" in n2 and "y" in n2 and "z" in n2:
          x=float(x)
          y=float(y)
          z=float(z)
          n2=x*y*z
          n2=str(n2)
        if "x" in n2 and "y" in n2:
          x=float(x)
          y=float(y)
          n2=x*y
          n2=str(n2)
        if "y" in n2 and "z" in n2:
          y=float(y)
          z=float(z)
          n2=y*z
          n2=str(n2)
        if "z" in n2 and "x" in n2:
          z=float(z)
          x=float(x)
          n2=z*x
          n2=str(n2)
        if "x" in n2:
          n2=x
        if "y" in n2:
          n2=y
        if "z" in n2:
          n2=z
        n2=float(n2)
        if f == "+":
          n3=n1+n2
        if f == "/" or f == "÷":
          n3=n1/n2
        if f == "-":
          n3=n1-n2
        if f == "x" or f == "*":
          n3=n1*n2
        if f == "**" or f == "^":
          n3=n1**n2
        if f == "%":
          n3=n1*n2/100
          
        medLetter("Here's your answer:")
        print("")
        sys.stdout.write("\033[1;32m\n")
        n3=str(n3)
        fastLetter(n3)
        n3=float(n3)
        print("\033[0;30;49m\n")
        
    if x==0:
      medLetter("Please choose a number")
      print("\033[0;36m\n")
      n2=input("")
      sys.stdout.write("\033[0;30;49m\n")
      n3=n2
      x=n2
      sys.stdout.write("\033[1;32m\n")
      medLetter(n1 + " =")
      print("")
      print(n3)
      print("\033[0;30;49m\n")
      
  if n1=="y":
    if not y==0:
      n1=y
      n1=float(n1)
      midLetter("Please choose a function (+, -, x, /, ^ or !)")
      print("\033[0;36m\n")
      f=input("")
      sys.stdout.write("\033[0;30;49m\n")
      n3=0
      if "!" in f:
        n1=int(n1)
        n3=int(n3)
        n3=n1
        while n1 > 1:
          n2=n1-1
          n3=n3*n2
          n1=n2
          stop = 1
          
      if "=" in f:
        n3=y
        stop=1
      if stop == 0:
        medLetter("Please choose a number or letters")
        print("\033[0;36m\n")
        n2=input("")
        print("\033[0;30;49m\n")
        if "x" in n2 and "y" in n2 and "z" in n2:
          x=float(x)
          y=float(y)
          z=float(z)
          n2=x*y*z
          n2=str(n2)
        if "x" in n2 and "y" in n2:
          x=float(x)
          y=float(y)
          n2=x*y
          n2=str(n2)
        if "y" in n2 and "z" in n2:
          y=float(y)
          z=float(z)
          n2=y*z
          n2=str(n2)
        if "z" in n2 and "x" in n2:
          z=float(z)
          x=float(x)
          n2=z*x
          n2=str(n2)
        if "x" in n2:
          n2=x
        if "y" in n2:
          n2=y
        if "z" in n2:
          n2=z
        n2=float(n2)
        if f == "+":
          n3=n1+n2
        if f == "/" or f == "÷":
          n3=n1/n2
        if f == "-":
          n3=n1-n2
        if f == "x" or f == "*":
          n3=n1*n2
        if f == "**" or f == "^":
          n3=n1**n2
        if f == "%":
          n3=n1*n2/100
        medLetter("Here's your answer:")
        print("")
        sys.stdout.write("\033[1;32m\n")
        n3=str(n3)
        fastLetter(n3)
        n3=float(n3)
        print("\033[0;30;49m\n")
    if y==0:
      medLetter("Please choose a number")
      print("\033[0;36m\n")
      n2=input("")
      sys.stdout.write("\033[0;30;49m\n")
      n3=n2
      y=n2
      sys.stdout.write("\033[1;32m\n")
      medLetter(n1 + " =")
      print("")
      print(n3)
      print("\033[0;30;49m\n")
  if n1=="z":
    letter="z"
    letterCal(z)
  if n1=="sin":
    medLetter("Please choose a number or letter")
    print("\033[0;36m\n")
    n2=input("")
    sys.stdout.write("\033[0;30;49m\n")
    if "x" in n2:
      n2=x
    if "y" in n2:
      n2=y
    if "z" in n2:
      n2=z
    n2=float(n2)
    n3=math.sin(math.radians(n2))
    medLetter("Here's your answer:")
    print("\033[1;32m\n")
    n3=str(n3)
    fastLetter(n3)
    n3=float(n3)
    print("\033[0;30;49m\n")
  if n1=="cos":
    medLetter("Please choose a number or letter")
    print("\033[0;36m\n")
    n2=input("")
    sys.stdout.write("\033[0;30;49m\n")
    if "x" in n2:
      n2=x
    if "y" in n2:
      n2=y
    if "z" in n2:
      n2=z
    n2=float(n2)
    n3=math.cos(math.radians(n2))
    medLetter("Here's your answer:")
    print("\033[1;32m\n")
    n3=str(n3)
    fastLetter(n3)
    n3=float(n3)
    print("\033[0;30;49m\n")
  if n1=="tan":
    medLetter("Please choose a number or letter")
    print("\033[0;36m\n")
    n2=input("")
    sys.stdout.write("\033[0;30;49m\n")
    if "x" in n2:
      n2=x
    if "y" in n2:
      n2=y
    if "z" in n2:
      n2=z
    n2=float(n2)
    n3=math.tan(math.radians(n2))
    medLetter("Here's your answer:")
    print("\033[1;32m\n")
    n3=str(n3)
    fastLetter(n3)
    n3=float(n3)
    print("\033[0;30;49m\n")
  if n1=="sin-1":
    medLetter("Please choose a number or letter")
    print("\033[0;36m\n")
    n2=input("")
    sys.stdout.write("\033[0;30;49m\n")
    if "x" in n2:
      n2=x
    if "y" in n2:
      n2=y
    if "z" in n2:
      n2=z
    n2=float(n2)
    n3=math.asin(n2)
    medLetter("Here's your answer:")
    print("\033[1;32m\n")
    n3=math.degrees(n3)
    n3=str(n3)
    fastLetter(n3)
    n3=float(n3)
    print("\033[0;30;49m\n")
  if n1=="cos-1":
    medLetter("Please choose a number or letter")
    print("\033[0;36m\n")
    n2=input("")
    sys.stdout.write("\033[0;30;49m\n")
    if "x" in n2:
      n2=x
    if "y" in n2:
      n2=y
    if "z" in n2:
      n2=z
    n2=float(n2)
    n3=math.acos(n2)
    medLetter("Here's your answer:")
    print("\033[1;32m\n")
    n3=math.degrees(n3)
    n3=str(n3)
    fastLetter(n3)
    n3=float(n3)
    print("\033[0;30;49m\n")
  if n1=="tan-1":
    medLetter("Please choose a number or letter")
    print("\033[0;36m\n")
    n2=input("")
    sys.stdout.write("\033[0;30;49m\n")
    if "x" in n2:
      n2=x
    if "y" in n2:
      n2=y
    if "z" in n2:
      n2=z
    n2=float(n2)
    n3=math.atan(n2)
    medLetter("Here's your answer:")
    print("\033[1;32m\n")
    n3=math.degrees(n3)
    n3=str(n3)
    fastLetter(n3)
    n3=float(n3)
    print("\033[0;30;49m\n")
  if n1=="quad" or n1=="quadratic":
    medLetter("Please enter the ammount of a")
    print("\033[0;36m\n")
    a1=int(input(""))
    sys.stdout.write("\033[0;30;49m\n")
    medLetter("Please enter the ammount of b")
    print("\033[0;36m\n")
    b1=int(input(""))
    sys.stdout.write("\033[0;30;49m\n")
    medLetter("Please enter the ammount of c")
    print("\033[0;36m\n")
    c1=int(input(""))
    sys.stdout.write("\033[0;30;49m\n")
    d = (b1**2) - (4*a1*c1)
    # n3a = complex((-b1-(d**(1/2)))/(2*a1))
    # n3b = complex((-b1+(d**(1/2)))/(2*a1))
    f = d**(1/2)
    print(str(f))
    medLetter("Here's your answer:")
    print("\033[1;32m\n")
    # n3a=str(n3a)
    # n3b=str(n3b)
    print("x = ")
    # fastLetter(n3a)
    # ################print(n3a)
    print("")
    print("x = ")
    # fastLetter(n3b)
    # ################print(n3b)
    # n3a=float(n3a)
    # n3b=float(n3b)
    print("\033[0;30;49m\n")
  if stop == 1:
    medLetter("Here's your answer:")
    print("")
    sys.stdout.write("\033[1;32m\n")
    n3=str(n3)
    fastLetter(n3)
    n3=float(n3)
    print("\033[0;30;49m\n")
    stop=0