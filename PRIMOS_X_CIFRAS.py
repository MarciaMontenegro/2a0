import random
def EXPMOD(a,x,n):
  c=a%n
  r=1
  while(x>0):
    if x%2!=0:
      r=(r*c)%n
    c=(c*c)%n
    x=x//2
  return r

def ES_COMPUESTO(a, n, t, u):
  xi = EXPMOD(a,u,n)
  if xi == 1 or xi == n-1:
    return False  
  for i in range(t):
    xi = EXPMOD(xi,2,n)
    if xi == n-1:
      return False  
  return True   

def MILLER_RABIN(n,s):
  t=0
  u=n-1
  while (u%2==0):
    u=u/2
    t=t+1
  for j in range(1,s):
    a=random.randint(2,n-1)
    if ES_COMPUESTO(a,n,t,u):
      return False
  return True

def GEN_PRIMOS(n):
    s = 5
    n=n+1-(n%2)
    while(MILLER_RABIN(n,s)==False):
        n=n+2
    return n



s=10
k=int(input("Cuantas cifras:(3,4,5) "))

if k==3:
  print("Primos de 3 cifras:")
  for n in range(100,1000):
    if(MILLER_RABIN(n,s)==True):
      print(n)

elif k==4:
  print("Primos de 4 cifras:")
  for n in range(1000,10000):
    if(MILLER_RABIN(n,s)==True):
      print(n)

elif k==5:
  print("Primos de 5 cifras:")
  for n in range(10000,100000):
    if(MILLER_RABIN(n,s)==True):
      print(n)
        

