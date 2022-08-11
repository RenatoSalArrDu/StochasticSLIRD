import numpy as np
import matplotlib.pyplot as plt
import pylab
#from matplotlib import colors
from matplotlib import rc
import matplotlib.colors as mcolors
import matplotlib.cm as cm

dat1=np.loadtxt('fort.21')
dat2=np.loadtxt('fort.20')
dat3=np.loadtxt('fort.16')
dat4=np.loadtxt('fort.15')
dat5=np.loadtxt('fort.105')

ntot=len(dat4[:,0])
cumsts = np.zeros(shape=(ntot,1))
cumsts[0] = dat4[0,1]

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
fig.text(0.5, 0.95, 'lognormal_2.0', ha='center',fontsize=(20))
plt.subplots_adjust(left=0.1, right=0.95,top=0.95, bottom=0.13)


plt.subplot(221)
plt.plot(dat4[:,0],cumsts[:,0],color = colormap(normalize(6)),marker='',
markevery=3,markersize=8,label='cumulative', linewidth=2)
plt.plot(dat5[:,0],dat5[:,1],color = colormap(normalize(1)),marker='',
markevery=3,markersize=8,label='q1', linewidth=2)
plt.plot(dat5[:,0],dat5[:,2],color = colormap(normalize(2)),marker='',
markevery=3,markersize=8,label='q3', linewidth=2)
plt.plot(dat4[:,0],dat4[:,8],color = colormap(normalize(8)),marker='',
markevery=3,markersize=8,label='min. cumulative', linewidth=2)
plt.plot(dat4[:,0],dat4[:,9],color = colormap(normalize(9)),marker='',
markevery=3,markersize=8,label='max. cumulative', linewidth=2)
plt.tick_params(labelsize='30',labeltop=False, labelright=False, labelbottom=False)
plt.legend(borderpad=0.1, shadow = True, loc='upper left', ncol=1,fontsize=(10))
plt.grid(True)


plt.subplot(222)
plt.bar(dat4[:,0],dat4[:,1],color = colormap(normalize(2)),
label='daily cases', width=0.9)
plt.tick_params(labelsize='30',labeltop=False, labelright=False, labelbottom=False)
plt.legend(borderpad=0.1, shadow = True, loc='upper left', ncol=1,fontsize=(15))
plt.grid(True)


plt.subplot(223)
plt.plot(dat3[:,0],dat3[:,1],color = colormap(normalize(3)),label='W(t)', linewidth=2)
plt.plot(dat3[:,0],dat3[:,1],color = colormap(normalize(6)), linewidth=2)
plt.tick_params(labelsize='30',labeltop=False, labelright=False, labelbottom=True)
plt.legend(borderpad=0.1, shadow = True, loc='best', ncol=1,fontsize=(15))
plt.grid(True)



plt.subplot(224)
plt.plot(dat3[:,0],dat3[:,1],color = colormap(normalize(3)),label='W(t)', linewidth=2)
plt.plot(dat3[:,0],dat3[:,1],color = colormap(normalize(6)), linewidth=2)
plt.tick_params(labelsize='30',labeltop=False, labelright=False, labelbottom=True)
plt.legend(borderpad=0.1, shadow = True, loc='best', ncol=1,fontsize=(15))
plt.grid(True)


plt.tight_layout()
figure_name = 'fig.eps'	# name of the figure to be saved
plt.savefig(figure_name)

plt.show()
