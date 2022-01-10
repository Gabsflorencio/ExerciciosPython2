import numpy as np
import math

def f(y,n,x):
 
  return (y**n)-x

def df(y,n,x):
 
  return n*(y**(n-1))

def raiz_enesima(n,x,tol):
  y=1;
  while abs((x**(1/n))-y)>tol:
    y=y-(f(y,n,x)/df(y,n,x))
  print(y)

x=float(input('Valor para x: '))
n=float(input('Valor para n: '))
tol=float(input('Erro tolerável: '))

raiz_enesima(n,x,tol)