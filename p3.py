import numpy as np
import matplotlib.pyplot as plt

def masa_jeans(n,mu,T):
    k  = 1.38e-23  #J K^-1
    G  = 6.674e-11 #N m^2/kg^2
    mH = 1.66e-27  #kg
    ro = mu*n*mH

    a = 5*k*T
    c = G*mu*mH
    d = (a/c)**(3./2.)
    b = 3./(4*np.pi*ro)
    return b*d

def radio_jeans(n,mu,T):
    k  = 1.38e-23  #J K^-1
    G  = 6.674e-11 #N m^2/kg^2
    mH = 1.66e-27  #kg
    ro = mu*n*mH

    a = 15*k*T
    b = 4*np.pi*mu*mH*ro*G

    return (a/b)**0.5

def dPdr_p2(n,T,Rj):
    k  = 1.38e-23  #J K^-1
    P = n*k*T
    print P
    return P/Rj


def dPdr_p3(r,n,mu,mj):
    mH = 1.66e-27  #kg
    ro = mu*n*mH
    G  = 6.674e-11 #N m^2/kg^2

    a = G*mj*ro
    return a/(r**2)



m_j = masa_jeans(1e10,2.,10)
R_j = radio_jeans(1e10,2,10)
print m_j,R_j

P_p2 = dPdr_p2(1e10,10,R_j)
P_p3 = dPdr_p3(R_j,1e10,2,m_j)
print P_p2,P_p3
