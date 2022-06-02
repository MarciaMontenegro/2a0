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


def RANDOMBITS(b):
    n=random.randint(0,(2**b)-1)
    m=(2**(b-1))+1
    n=n | m
    return n

def RANDOMGEN_PRIMOS(b):
    n=RANDOMBITS(b)
    while MILLER_RABIN(n,s) is False:
        n=n+2
    return n


s=10
def Pregunta1():
  
  k=int(input("Cuantas cifras:(3,4,5)?: "))
  
  if k==3:
    print("Primos de 3 cifras: ")
    for n in range(100,1000):
      if(MILLER_RABIN(n,s)==True):
        print(n)
  
  elif k==4:
    print("Primos de 4 cifras: ")
    for n in range(1000,10000):
      if(MILLER_RABIN(n,s)==True):
        print(n)
  
  elif k==5:
    print("Primos de 5 cifras: ")
    for n in range(10000,100000):
      if(MILLER_RABIN(n,s)==True):
        print(n)

  else:
    print("NUMERO INGRESADO NO VALIDO")
          

def Pregunta2():
  H=int(input("Cuantos bits(16,32,64)?: "));
  for i in range(10):
      print(RANDOMGEN_PRIMOS(H))

def Eleccion():
  print("OPCIONES:")
  print("1. Generar todos los primos de 3, 4 y 5 cifras")
  print("2. Implementar un programa que genere de manera aleatoria al menos 10 primos distintos de 16, 32 y 64 bits")
  E=int(input("QUE DESEAS HACER? "))
  if E == 1:
    Pregunta1()
  elif E==2:
    Pregunta2()
  else:
    print("Opcion no valida")


#ejecucion

Eleccion()
