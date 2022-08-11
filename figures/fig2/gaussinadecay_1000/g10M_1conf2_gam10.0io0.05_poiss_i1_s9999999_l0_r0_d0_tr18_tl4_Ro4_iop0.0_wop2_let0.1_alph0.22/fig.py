import numpy as np
import matplotlib.pyplot as plt
import pylab
#from matplotlib import colors
from matplotlib import rc
import matplotlib.colors as mcolors
import matplotlib.cm as cm

dat=np.loadtxt('fort.20')
dat2=np.loadtxt('fort.25')
dat3=np.loadtxt('fort.16')
dat4=np.loadtxt('fort.15')

plt.rcParams['axes.linewidth'] = 3.0
plt.rcParams['xtick.major.width'] = 3.5
plt.rcParams['ytick.major.width'] = 3.5
plt.rcParams['xtick.major.size'] = 20
plt.rcParams['ytick.major.size'] = 20
#rc('font', **{'family': 'sans-serif', 'serif': ['Computer Modern']})
#rc('text', usetex=True)

# Choose a colormap
colormap = cm.viridis
mus = [1,2,3,4,5,6]
colorparams = mus
normalize = mcolors.Normalize(vmin=np.min(colorparams), vmax=np.max(colorparams))

fig, ax = plt.subplots(nrows=2, ncols=2, sharex=True, sharey=True, figsize=(13, 15))
fig.text(0.5, 0.01, 'days', ha='center',fontsize=(30))
plt.subplots_adjust(left=0.1, right=0.95,top=0.95, bottom=0.13)
if 3 == 1:
    plt.title('Uniform',fontsize=20)
elif 3 == 2:
    plt.title('Exponential',fontsize=20)
elif 3 == 3:
    plt.title('Poisson',fontsize=20)


plt.subplot(221)
# plt.plot(dat[:,0],dat[:,2],color = colormap(normalize(1)),marker='',
# markevery=3,markersize=8,label='susceptible', linewidth=2)
plt.plot(dat[:,0],dat[:,1],color = colormap(normalize(2)),marker='',
markevery=3,markersize=8,label='latent', linewidth=2)
plt.plot(dat[:,0],dat[:,3],color = colormap(normalize(3)),marker='',
markevery=3,markersize=8,label='infected', linewidth=2)
plt.plot(dat[:,0],dat[:,4],color = colormap(normalize(4)),marker='',
markevery=3,markersize=8,label='recovered', linewidth=2)
plt.plot(dat[:,0],dat[:,5],color = colormap(normalize(5)),marker='',
markevery=3,markersize=8,label='deads', linewidth=2)
plt.plot(dat[:,0],dat[:,6],color = colormap(normalize(6)),marker='',
markevery=3,markersize=8,label='cum', linewidth=2)

plt.tick_params(labelsize='30',labeltop=False, labelright=False, labelbottom=False)
plt.legend(borderpad=0.1, shadow = True, loc='upper left', ncol=1,fontsize=(10))
plt.grid(True)

plt.subplot(222)
plt.bar(dat2[:,0],dat2[:,2],color = colormap(normalize(2)),
label='Daily cases', width=0.9)
plt.ylim(top = max(dat[:,1]) + max(dat[:,1])/10 , bottom = 0)
plt.tick_params(labelsize='30',labeltop=False, labelright=False, labelbottom=False)
plt.legend(borderpad=0.1, shadow = True, loc='best', ncol=1,fontsize=(20))
plt.ylim(top = max(dat2[:,1]) + max(dat2[:,1])/10 , bottom = 0)
plt.grid(True)

plt.subplot(223)
plt.bar(dat4[:,0],dat4[:,1],color = colormap(normalize(2)),
label='Daily cases', width=0.9)
plt.ylim(top = max(dat4[:,1]) + max(dat4[:,1])/10 , bottom = 0)
plt.tick_params(labelsize='30',labeltop=False, labelright=False, labelbottom=True)
plt.legend(borderpad=0.1, shadow = True, loc='best', ncol=1,fontsize=(20))
plt.ylim(top = max(dat4[:,1]) + max(dat4[:,1])/10 , bottom = 0)
plt.grid(True)


plt.subplot(224)
plt.plot(dat3[:,0],dat3[:,1],color = colormap(normalize(1)),label='W(t)', linewidth=2)
plt.plot(dat3[:,0],dat3[:,2],color = colormap(normalize(3)),label='C(t)', linewidth=2)
plt.plot(dat3[:,0],dat3[:,3],color = colormap(normalize(5)),label='H(t)', linewidth=2)
plt.tick_params(labelsize='30',labeltop=False, labelright=False, labelbottom=True)
plt.legend(borderpad=0.1, shadow = True, loc='best', ncol=1,fontsize=(15))
plt.grid(True)


plt.tight_layout()
figure_name = 'fig1.eps'	# name of the figure to be saved
plt.savefig(figure_name)

plt.show()
