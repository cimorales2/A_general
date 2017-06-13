import numpy as np

def w_0(m,r_0,r_f):
    G = 6.67e-11 #m^3 kg^-1 s^-2
    a = r_f*2*G*m
    b = a/(r_0**4)
    return np.sqrt(b)

m_r = 2*1.99e+30    #kg
r_0 = 0.75*3.09e+16 #m
r_f = 100 * 149597870700 #m
w   = w_0(m_r,r_0,r_f)
print w,m_r,r_0,r_f
L_i = w*m_r*r_0**2
print L_i,w*r_0

I_e = 2./5. * m_r*r_0**2
I_d = 0.5*m_r*r_0**2
print I_e,I_d
print L_i/I_e,L_i/I_d

w_f = L_i/(m_r*r_f**2)
T = 2*np.pi/w_f
print T

G = 6.67e-11 #m^3 kg^-1 s^-2
T2 = np.sqrt((4*np.pi*np.pi*r_f**3)/(G*m_r))
print T2
print T2/T
