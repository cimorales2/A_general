#%% Imports
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import scipy.constants as constants
from uncertainties import *
import os
from scipy.optimize import curve_fit
# pregunta 5
#%% Funciones
def ec_de_la_clase(tau):    return (0.7104-0.1331*np.exp(-3.449*tau))

def T_T_eff(log_tau):   return [(((3/4)*(10**i+ec_de_la_clase(10**i)))**(1/4))
                                for i in log_tau]

def q(tau, T):  return [((4./3.)*((T[i]/T_eff_sol)**4)-(tau[i]))
                        for i in range(len(tau))]

def ec_de_la_clase2(tau):   return [(0.7104-0.1331*np.exp(-3.449*i))
                                    for i in tau]

# Constantes
sigma = 5.67*10**-5                 #Constate de Stefan-Boltzman en cgs
C = constants.speed_of_light * 100  #velocidad de la luz en cm/s
T_eff_sol = 5778 #kelvin

#%% Datos
archivo = open('data.txt','r')
data = archivo.readlines()
tau_0, T, log_p_g, log_p_e, log_k_p, x = ([] for i in range(6))
for i in range(len(data)):
    data[i] = data[i].split(' ')
    data[i][len(data[i])-1] = data[i][len(data[i])-1].strip('\n')
    tau_0.append(float(data[i][0]))
    T.append(float(data[i][1]))
    log_p_g.append(float(data[i][2]))
    log_p_e.append(float(data[i][3]))
    log_k_p.append(float(data[i][4]))
    x.append(float(data[i][5])*(10**5)) #En [cm]
tau = [10**i for i in tau_0] #quitandole el log
P_rad, k_0 = [], []
for i in range(len(log_p_e)):
    p_e = 10**log_p_e[i]
    k0_pe = 10**log_k_p[i]
    k_0.append(k0_pe * p_e)
    P_rad.append(np.log10(4*sigma*(T[i]**4)/(3*C)))
#%% Parte a
# Plots
fig, ((ax1, ax2), (ax3, ax4), (ax5, ax6), (ax7, ax8), (ax9, ax10)) = plt.subplots(5, 2, sharex='col',
                                                                                        sharey='row',figsize=(10, 8))
opciones = {'markersize':4, 'marker':'+', 'markeredgecolor':'black'}
ax1.plot(tau_0, T, 'r--', **opciones)
ax2.plot(x, T, 'r--', **opciones)
ax3.plot(tau_0, P_rad, 'y--', **opciones)
ax4.plot(x, P_rad, 'y--', **opciones)
ax5.plot(tau_0, log_p_g, 'b--', **opciones)
ax6.plot(x, log_p_g, 'b--', **opciones)
ax7.plot(tau_0, log_p_e, 'g--', **opciones)
ax8.plot(x, log_p_e, 'g--', **opciones)
ax9.plot(tau_0, k_0, 'm--', **opciones)
ax10.plot(x, k_0, 'm--', **opciones)
# Ajustes de los ejes
#ticks
ax1.set_yticks(np.arange(3000, 10000, 1000))
ax3.set_yticks(np.arange(0, 1.5, .2))
ax5.set_yticks(np.arange(3, 8, .5))
ax7.set_yticks(np.arange(-2, 5, 1))
ax9.set_yticks(np.arange(0, 15, 2))
#labels
opciones_de_labels = {'fontsize':14, 'rotation':0,
                    'horizontalalignment':'right',
                    'verticalalignment':'center'}
ax1.set_ylabel(r'$T^{\circ}$', **opciones_de_labels)
ax3.set_ylabel(r'$log(P_{rad})$', **opciones_de_labels)
ax5.set_ylabel(r'$log(P_{g})$', **opciones_de_labels)
ax7.set_ylabel(r'$log(P_{e})$', **opciones_de_labels)
ax9.set_ylabel(r'$\kappa_{0}$', **opciones_de_labels)
ax9.set_xlabel(r'$log(\tau_{0})$', fontsize=16)
ax10.set_xlabel('Altura geometrica [cm]', fontsize=16)
#guardado
plt.savefig('grafico_p5_01.pdf')
plt.show()
#%% Parte 2
xp = np.linspace(-4,1,100)
plt.plot(tau_0, [(i/T_eff_sol) for i in T],'r--', markersize=6, marker='+',
        markeredgecolor='black', label='Datos de la Tabla')
plt.plot(xp, T_T_eff(xp),'b--', label='Ecuacion mostrada en clases')
plt.xlabel(r'$log(\tau)$', fontsize=16)
plt.ylabel(r'$T\ /\ T_{eff}$', fontsize=16)
plt.legend()
plt.savefig('grafico_p5_02.pdf')
plt.show()
#%% otro grafico de la parte b
xp = np.linspace(-1,15,100)
plt.plot(xp, ec_de_la_clase2(xp),'b--', label='Ec. de hopf')
plt.plot(tau, q(tau,T), 'r--', marker = '+',
        markeredgecolor='black', markersize=7, label='Datos a partir de la tabla')
plt.ylabel(r'$q(\tau)$', fontsize=16)
plt.xlabel(r'$\tau$', fontsize=16)
plt.legend(loc=2)
plt.xlim(-.5,2.6)
plt.ylim(0.3,1.4)
plt.subplots_adjust(left=0.12, right=0.95, top=0.9, bottom=0.2)
plt.savefig('grafico_p5_04.pdf')
plt.show()
#%% Parte c
for i in range(len(tau_0)):
    if tau[i]+q(tau,T)[i]>=4/3:
            Teff_igual_T = i
            print('tau + q(tau): {:.3f}'.format(tau[i]+q(tau,T)[i]))
            print('indice de la lista: {}'.format(i))
            print('tau correspondiente: {:.3f}'.format(tau[i]))
            print('log(tau) correspondiente: {:.3f}'.format(tau_0[i]))
            break
