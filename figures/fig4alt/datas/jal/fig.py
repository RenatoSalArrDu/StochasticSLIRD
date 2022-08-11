import numpy as np
import matplotlib.pyplot as plt
import pylab
from matplotlib import rc
import matplotlib.colors as mcolors
import matplotlib.cm as cm

dat1=np.loadtxt('fort.21')
dat2=np.loadtxt('fort.20')
dat3=np.loadtxt('fort.16')
dat4=np.loadtxt('fort.15')
dat5=np.loadtxt('fort.105')
dato=np.loadtxt('/home/pclopez/scham/epidemia/StochasticSLIRD//code/Mexico_covid-19_datas/datas20_08_21/jal.dat')
ntotst=len(dato[:,0])
cumst = np.zeros(shape=(ntotst,1))
cumst[0] = dato[0,1]

for j in range(0,ntotst-1):
    cumst[j+1] += cumst[j] + dato[j+1,1]

ntot=len(dat4[:,0])
cumsts = np.zeros(shape=(ntot,1))
cumsts[0] = dat4[0,1] + 12

for j in range(0,ntot-1):
    cumsts[j+1] += cumsts[j] + dat4[j+1,1]

plt.rcParams['axes.linewidth'] = 3.0
plt.rcParams['xtick.major.width'] = 3.5
plt.rcParams['ytick.major.width'] = 3.5
plt.rcParams['xtick.major.size'] = 20
plt.rcParams['ytick.major.size'] = 20
#rc('font', **{'family': 'sans-serif', 'serif': ['Computer Modern']})
#rc('text', usetex=True)

# Choose a colormap
colormap = cm.viridis
mus = [1,2,3,4,5,6,7,8,9]
colorparams = mus
normalize = mcolors.Normalize(vmin=np.min(colorparams), vmax=np.max(colorparams))

fig, ax = plt.subplots(nrows=2, ncols=2, sharex=True, sharey=True, figsize=(13, 15))
fig.text(0.5, 0.01, 'days', ha='center',fontsize=(30))
fig.text(0.5, 0.95, '', ha='center',fontsize=(20))
plt.subplots_adjust(left=0.1, right=0.95,top=0.95, bottom=0.13)


plt.subplot(221)
plt.plot(dat4[:,0]+27-1,cumsts[:,0],color = colormap(normalize(6)),label='cumulative', linewidth=2)
plt.plot(dat5[:,0]+27-1,dat5[:,1],color = colormap(normalize(1)),label='q1', linewidth=2)
plt.plot(dat5[:,0]+27-1,dat5[:,2],color = colormap(normalize(2)),label='q3', linewidth=2)
plt.plot(dato[:,0],cumst[:,0],color = 'k',label='cumultive data', linewidth=2)
plt.tick_params(labelsize='30',labeltop=False, labelright=False, labelbottom=False)
plt.legend(borderpad=0.1, shadow = True, loc='upper left', ncol=1,fontsize=(10))
plt.xlim(left=0, right=540 + 27-1)
plt.grid(True)


plt.subplot(222)
plt.bar(dat4[:,0]+27-1,dat4[:,1],color = colormap(normalize(2)),label='daily cases', width=0.9)
plt.bar(dato[:,0],dato[:,1],color = colormap(normalize(3)),label='jal', width=0.7)
plt.ylim(top = max(dato[:,1]) + max(dato[:,1])/10 , bottom = 0)
plt.tick_params(labelsize='30',labeltop=False, labelright=False, labelbottom=False)
plt.legend(borderpad=0.1, shadow = True, loc='upper left', ncol=1,fontsize=(15))
plt.xlim(left=0, right=540 + 27-1)
plt.grid(True)


plt.subplot(223)
plt.plot(dat3[:,0]+27-1,dat3[:,1],color = colormap(normalize(3)),label='W(t)', linewidth=2)
plt.plot(dat3[:,0],dat3[:,1],color = colormap(normalize(6)), linewidth=2)
plt.tick_params(labelsize='30',labeltop=False, labelright=False, labelbottom=True)
plt.legend(borderpad=0.1, shadow = True, loc='best', ncol=1,fontsize=(15))
plt.xlim(left=0, right=540 + 27-1)
plt.ylim(bottom=0, top=1)
#plt.yscale("symlog")
plt.grid(True)



plt.subplot(224)
plt.plot(dat3[:,0]+27-1,dat3[:,1],color = colormap(normalize(3)),label='W(t)', linewidth=2)
plt.plot(dat3[:,0],dat3[:,1],color = colormap(normalize(6)), linewidth=2)
plt.tick_params(labelsize='30',labeltop=False, labelright=False, labelbottom=True)
plt.legend(borderpad=0.1, shadow = True, loc='best', ncol=1,fontsize=(15))
plt.xlim(left=0, right=540 + 27-1)
plt.grid(True)


plt.tight_layout()
figure_name = 'figjal.eps'	# name of the figure to be saved
plt.savefig(figure_name)

plt.show()
