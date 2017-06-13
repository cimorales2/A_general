import numpy as np
import matplotlib.pyplot as plt

def E(i):
    a = float(i**2)
    if i==0:return 0
    return -13.6/a
def g(i):
    return 2.*(i**2.)

def U(T,j,m):
    k = 8.62e-5 #eV K^-1
    a = k*T
    suma = 0
    for i in np.arange(1,m+1,1):
        b = g(i)
        c = E(j)-E(i)
        d = np.exp(-c/a)
        print d
        e = b*d
        suma+=e
    print "jump"
    return suma

def r(i):
    a = 0.5e-8 #cm
    return a*(i**2)

def Saha(u1,u2,ne,xi,T):
    me = 9.11e-31
    h = 6.63e-34
    kb = 8.62e-5 #eV K^-1
    a = 2.*u2/(ne*u1)
    b = (2.*np.pi*me*kb*T/(h**2))**(3./2.)
    c = -xi/(kb*T)
    d = np.exp(c)
    return a*b*d


T = 1.56e+7
n = 9.08e+25
U_I  = U(T,1,1)
U_II = U(T,2,1)
print U_I, U_II
print E(1)-E(2)
print r(1),r(2),r(3)
S = Saha(U_I,U_II,n,13.6,T)
S2 = 1./S
print 1/(S2 + 1)
