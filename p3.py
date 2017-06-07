import numpy as np
import matplotlib.pyplot as plt

def masa_jeans(n,mu,T):
    k  = 1.38e-23  #J K^-1
    G  = 6.674e-11 #N m^2/kg^2
    mH = 1.66e-24  #kg
    ro = mu*n*mH

    a = 5*k*T
    c = G*mu*mH
    d = (a/c)**1.5
    b = 3./(4*np.pi*ro)
    return b*d

def radio_jeans(n,mu,T):
    k  = 1.38e-23  #J K^-1
    G  = 6.674e-11 #N m^2/kg^2
    mH = 1.66e-24  #kg
    ro = mu*n*mH

    a = 15*k*T
    b = 4*np.pi*mu*mH*ro*G

    return a/b

def presion_p2()

def presion_p3(r,n,mu,mj):
    mH = 1.66e-24  #kg
    ro = mu*n*mH
    G  = 6.674e-11 #N m^2/kg^2

    a = G*mj*ro
    return a/r**2



m_j = masa_jeans(1.e10,2.,10)
R_j = radio_jeans(1e10,2,10)

P_p3 = presion_p3(R_j,1e10,2,m_j)
print P_p3
