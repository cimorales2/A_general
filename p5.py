import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt("data.txt")

s = 5.67e-5 #erg cm^-2 s^-1 K^-4
c = 29979245800*100 #cm/s
Prad = np.log10(4.*s*data[:,1]**4/(3.*c))
k0 = 10**(data[:,4]+data[:,5])

t_0 = data[:,0]
x   = data[:,5] * 1e+5

fig, ((ax1,ax2), (ax3,ax4), (ax5,ax6), (ax7,ax8), (ax9,ax10)) = plt.subplots(5,2,sharex='col',sharey='row',figsize=(10,8))

ax1.plot(x,data[:,1],'.-')
ax2.plot(t_0,data[:,1],'.-')
ax3.plot(x,data[:,2],'.-')
ax4.plot(t_0,data[:,2],'.-')
ax5.plot(x,data[:,3],'.-')
ax6.plot(t_0,data[:,3],'.-')
ax7.plot(x,Prad,'.-')
ax8.plot(t_0,Prad,'.-')
ax9.plot(x,k0,'.-')
ax10.plot(t_0,k0,'.-')

ax1.set_ylabel(r'$T$',fontsize=14)
ax3.set_ylabel(r'$log P_g$',fontsize=14)
ax5.set_ylabel(r'$log P_e$',fontsize=14)
ax7.set_ylabel(r'$log P_{rad}$',fontsize=14)
ax9.set_ylabel(r'$\kappa_0$',fontsize=16)


ax10.set_xlabel(r'$log(\tau_0)$',fontsize=14)
ax9.set_xlabel(r'Altura geometrica [cm]')

plt.savefig('all_plots.pdf')
