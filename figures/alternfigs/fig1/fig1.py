import numpy as np
import matplotlib.pyplot as plt
import pylab
#from matplotlib import colors
from matplotlib import rc
import matplotlib.colors as mcolors
import matplotlib.cm as cm


p1=np.loadtxt('new/rt_avf_5000conf1punctual_2.0_i10_s999990_l0_r0_d0_tr18_tl4_Ro4_iop0.0_wop2_let0.1_alph0.22/fort.21')
p2=np.loadtxt('new/rt_avf_5000conf1punctual_2.0_i10_s999990_l0_r0_d0_tr18_tl4_Ro4_iop0.0_wop2_let0.1_alph0.22/fort.26')
p3=np.loadtxt('new/rt_avf_5000conf1punctual_2.0_i10_s999990_l0_r0_d0_tr18_tl4_Ro4_iop0.0_wop2_let0.1_alph0.22/fort.16')

p500K1=np.loadtxt('new/himn/punctual/500K/fort.15') #LSIRD-C variables
p500K2=np.loadtxt('new/himn/punctual/500K/fort.105') #weight fun:w,cf,hf
p1M1=np.loadtxt('new/himn/punctual/1M/fort.15') #LSIRD-C variables
p1M2=np.loadtxt('new/himn/punctual/1M/fort.105') #weight fun:w,cf,hf
p5M1=np.loadtxt('new/himn/punctual/5M/fort.15') #LSIRD-C variables
p5M2=np.loadtxt('new/himn/punctual/5M/fort.105') #weight fun:w,cf,hf
p10M1=np.loadtxt('new/himn/punctual/10M/fort.15') #LSIRD-C variables
p10M2=np.loadtxt('new/himn/punctual/10M/fort.105') #weight fun:w,cf,hf


plt.rcParams['axes.linewidth'] = 2.0
plt.rcParams['xtick.major.width'] = 2.0
plt.rcParams['ytick.major.width'] = 2.0
plt.rcParams['xtick.major.size'] = 5
plt.rcParams['ytick.major.size'] = 5
rc('font', **{'family': 'sans-serif', 'serif': ['Computer Modern']})
rc('text', usetex=True)



# Choose a colormaps
colormap = cm.viridis
mus = [1,2,3,4,5,6,7,8,9]
colorparams = mus
normalize = mcolors.Normalize(vmin=np.min(colorparams), vmax=np.max(colorparams))

colormap2 = cm.cividis
mus2 = [1,2,3,4,5,6,7,8,9]
colorparams2 = mus2
normalize2 = mcolors.Normalize(vmin=np.min(colorparams2), vmax=np.max(colorparams2))

colormap3 = cm.tab10
mus3 = [1,2,3,4,5,6,7,8,9]
colorparams3 = mus3
normalize3 = mcolors.Normalize(vmin=np.min(colorparams3), vmax=np.max(colorparams3))



fig = plt.figure(figsize=(18, 18))
fig.text(0.51, 0.01, r'$\mathrm{days}$', ha='center',fontsize=(30))
gs =  fig.add_gridspec(2,2)

ax1 = fig.add_subplot(gs[0, 0])
ax2 = fig.add_subplot(gs[1, 0])
ax3 = fig.add_subplot(gs[0:,1:])

color = 'tab:red'
yl = [r'$0.25$',r'$0.5$',r'$0.75$',r'$1.0$']
yn=[0.25,0.5,0.75,1.0]
x4=[0,100,200]
x5=[0,250,500]


###############################################################################
ax1.plot(p1[:,0],p1[:,1] ,color = colormap(normalize(1)), label=r'$L(t)$', linewidth=1.5)
ax1.plot(p1[:,0],p1[:,3] ,color = colormap(normalize(3)), label=r'$I(t)$', linewidth=1.5)
ax1.plot(p1[:,0],p1[:,4] ,color = colormap(normalize(5)), label=r'$R(t)$', linewidth=1.5)
ax1.plot(p1[:,0],p1[:,5] ,color = colormap(normalize(7)), label=r'$D(t)$', linewidth=1.5)
ax1.plot(p1[:,0],p1[:,6] ,color = colormap(normalize(9)), label=r'$c(t)$', linewidth=1.5)
ax1.set_yticklabels(['$0$','$200K$','$400K$','$600K$','$800K$'])
ax1.set_yticks([0,200000,400000,600000,800000])
ax1.set_ylim(top = 850000, bottom = 0)
ax1.set_xticklabels(['$0$','$75$','$150$'])
ax1.set_xticks([0,75,150])
ax1.set_xlim(right = 180, left = 0)
ax1.tick_params(labelsize='18',labeltop=False, labelright=False, labelbottom=False)
ax1.legend(borderpad=0.1, shadow = True, loc='best', ncol=1,fontsize=(13))
ax1.grid(True)

###############################################################################

ax2.bar(p2[:,0],p2[:,2],color = colormap(normalize(3)),label=r'$i(t)$', width=0.9)
ax2.set_yticklabels(['$0$','$10K$','$20K$'])
ax2.set_yticks([0,10000,20000])
ax2.set_xticklabels(['$0$','$75$','$150$'])
ax2.set_xticks([0,75,150])
ax2.set_xlim(right = 180, left = 0)
ax2.tick_params(labelsize='18',labeltop=False, labelright=False, labelbottom=True)
ax2.axvline(x=84.3,color='k', linestyle = '--' )
ax2.grid(False)
axw2 = ax2.twinx()
axw2.set_yticklabels(yl)
axw2.set_yticks(yn)
axw2.tick_params(axis='y', labelcolor=color, direction="in", pad=-40)
axw2.plot(p3[:,0] , p3[:,1] ,color = color, label=r'$H(t)$', linewidth=1.5)
axw2.bar(0,0,color = colormap(normalize(3)),label=r'$i(t)$', width=0.9)
axw2.tick_params(labelsize='18',labeltop=False, labelright=True, labelbottom=False)
axw2.legend(borderpad=0.1, shadow = True, loc='lower left', ncol=1,fontsize=(13))
axw2.grid(True)

######### small embedded frame

left, bottom, width, height = [0.315, 0.3, 0.15, 0.19]
ax2s = fig.add_axes([left, bottom, width, height])
ax2s.bar(p2[:,0],p2[:,2],color = colormap(normalize(3)), width=0.9)
ax2s.set_ylim(top = 100 , bottom = 0)
y2s=[50,100]
ax2s.set_yticks(y2s)
ax2s.set_xlim(right = 40 , left = 0)
ax2s.tick_params(labelsize='15',labeltop=False, labelright=False, labelbottom=True)
ax2s.grid(True)

###############################################################################

ax3.bar(p500K1[:,0],p500K1[:,1]/500000,color = colormap2(normalize2(1)), label=r'$500K$', width=0.9)
ax3.bar(p1M1[:,0],p1M1[:,1]/1000000,color = colormap2(normalize2(3)),label=r'$1M$', width=0.8)
ax3.bar(p5M1[:,0],p5M1[:,1]/5000000,color = colormap2(normalize2(5)), label=r'$5M$', width=0.7)
ax3.bar(p10M1[:,0],p10M1[:,1]/10000000,color = colormap2(normalize2(7)), label=r'$10M$', width=0.6)
ax3.tick_params(labelsize='18',labeltop=False, labelright=False, labelbottom=True)
ax3.set_xticklabels(['$0$','$75$','$150$'])
ax3.set_xticks([0,75,150])
ax3.set_xlim(right = 180, left = 0)
ax3.legend(borderpad=0.1, shadow = True, loc='best', ncol=1,fontsize=(15))
ax3.set_yticklabels(['$0.01$','$0.02$'])
ax3.set_yticks([0.01,0.02])
ax3.set_ylim(top = 0.03 , bottom = 0)
ax3.axvline(x=81,color='k', linestyle='--')
ax3.axvline(x=86,color='k', linestyle='--')
ax3.axvline(x=98,color='k', linestyle='--')
ax3.axvline(x=103,color='k', linestyle='--')
ax3.tick_params(axis='y', direction="in", pad=-40)
ax3.grid(True)


plt.tight_layout()
figure_name = 'fig1.eps'	# name of the figure to be saved
plt.savefig(figure_name)

plt.show()
