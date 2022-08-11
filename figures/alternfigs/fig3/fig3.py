import numpy as np
import matplotlib.pyplot as plt
import pylab
#from matplotlib import colors
from matplotlib import rc
import matplotlib.colors as mcolors
import matplotlib.cm as cm

d30a1=np.loadtxt('data/al_conf50/fort.25')
d30a2=np.loadtxt('data/al_conf50/fort.16')

d30b1=np.loadtxt('data/al_conf51b/fort.25')
d30b2=np.loadtxt('data/al_conf51b/fort.16')

d30c1=np.loadtxt('data/al_conf52b/fort.25')
d30c2=np.loadtxt('data/al_conf52b/fort.16')

#d41=np.loadtxt('data/al_conf53/fort.25')
#d42=np.loadtxt('data/al_conf53/fort.16')

#####################################

d60a1=np.loadtxt('data/conf50/fort.25')
d60a2=np.loadtxt('data/conf50/fort.16')

d60b1=np.loadtxt('data/conf51a/fort.25')
d60b2=np.loadtxt('data/conf51a/fort.16')

d60c1=np.loadtxt('data/conf52a/fort.25')
d60c2=np.loadtxt('data/conf52a/fort.16')



#####################################
d60i90d120a1=np.loadtxt('data/conf70/fort.25')
d60i90d120a2=np.loadtxt('data/conf70/fort.16')

d60i90d120b1=np.loadtxt('data/conf71/fort.25')
d60i90d120b2=np.loadtxt('data/conf71/fort.16')

d60i90d120c1=np.loadtxt('data/conf72/fort.25')
d60i90d120c2=np.loadtxt('data/conf72/fort.16')

#####################################


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



color = 'tab:red'
yl = [r'$0.25$',r'$0.5$',r'$0.75$',r'$1$']
yn=[0.25,0.5,0.75,1]
x4=[0,100,200]
x5=[0,250,500]



fig, ((ax4,ax5,ax6),(ax7,ax8,ax9),(ax10,ax11,ax12)) = plt.subplots(nrows=3, ncols=3, sharex=False, sharey=False, figsize=(18, 18))
fig.text(0.508, 0.01, r'$\mathrm{days}$', ha='center',fontsize=(20))
plt.subplots_adjust(left=0.1, right=0.95,top=0.95, bottom=0.13)

################################################################################

ax4.bar(d30a1[:,0],d30a1[:,2],color = colormap(normalize(3)), width=0.9)
ax4.tick_params(labelsize='13',labeltop=False, labelright=False, labelbottom=False)
ax4.set_ylim(top = max(d30a1[:,1]) + max(d30a1[:,1])/10 , bottom = 0)
ax4.set_xlim(right = 200 , left = 0)
ax4.set_xticks(x4)
ax4.set_yticklabels(['$0$','$10$','$20$'])
ax4.set_yticks([0,10,20])
ax4.grid(False)
ax4w = ax4.twinx()
ax4w.plot(d30a2[:,0],d30a2[:,1],color = colormap3(normalize3(1)),label=r'$W(t)$', linewidth=2)
ax4w.plot(d30a2[:,0],d30a2[:,2],color = colormap3(normalize3(2)),label=r'$C(t)$', linewidth=1.5)
ax4w.plot(d30a2[:,0],d30a2[:,3],color = colormap3(normalize3(3)),label=r'$H(t)$', linewidth=1.5)
ax4w.bar(0,0,color = colormap(normalize(3)),label=r'$i(t)$', width=0.9)
ax4w.tick_params(axis='y', labelcolor=color)
ax4w.tick_params(labelsize='13',labeltop=False, labelright=False, labelbottom=False)
ax4w.legend(borderpad=0.3, shadow = True, loc='upper right', ncol=1,fontsize=(13))
ax4w.set_xlim(right = 200 , left = 0)
ax4w.grid(True)


ax5.bar(d30b1[:,0],d30b1[:,2],color = colormap(normalize(3)), width=0.9)
ax5.tick_params(labelsize='13',labeltop=False, labelright=False, labelbottom=False)
ax5.set_ylim(top = max(d30b1[:,1]) + max(d30b1[:,1])/10 , bottom = 0)
ax5.set_xlim(right = 500 , left = 0)
ax5.set_xticks(x5)
ax5.set_yticklabels(['$0$','$10$','$20$'])
ax5.set_yticks([0,10,20])
ax5.grid(False)
ax5w = ax5.twinx()
ax5w.plot(d30b2[:,0],d30b2[:,1],color = colormap3(normalize3(1)),label=r'$W(t)$', linewidth=1.8)
ax5w.plot(d30b2[:,0],d30b2[:,2],color = colormap3(normalize3(2)),label=r'$C(t)$', linewidth=1.5)
ax5w.plot(d30b2[:,0],d30b2[:,3],color = colormap3(normalize3(3)),label=r'$H(t)$', linewidth=1.5)
ax5w.bar(0,0,color = colormap(normalize(3)),label=r'$i(t)$', width=0.9)
ax5w.tick_params(axis='y', labelcolor=color)
ax5w.tick_params(labelsize='13',labeltop=False, labelright=False, labelbottom=False)
#ax5w.legend(borderpad=0.3, shadow = True, loc='upper left', ncol=1,fontsize=(13))
ax5w.set_xlim(right = 500 , left = 0)
ax5w.grid(True)


ax6.bar(d30c1[:,0],d30c1[:,2],color = colormap(normalize(3)), width=0.9)
ax6.tick_params(labelsize='13',labeltop=False, labelright=False, labelbottom=False)
ax6.set_ylim(top = max(d30c1[:,1]) + max(d30c1[:,1])/5 , bottom = 0)
ax6.set_xlim(right = 300 , left = 0)
ax6.set_xticks(x5)
ax6.set_yticklabels(['$0$','$3C$','$6C$'])
ax6.set_yticks([0,300,600])
ax6.grid(False)
ax6w = ax6.twinx()
ax6w.plot(d30c2[:,0],d30c2[:,1],color = colormap3(normalize3(1)),label=r'W(t)', linewidth=1.8)
ax6w.plot(d30c2[:,0],d30c2[:,2],color = colormap3(normalize3(2)),label=r'C(t)', linewidth=1.5)
ax6w.plot(d30c2[:,0],d30c2[:,3],color = colormap3(normalize3(3)),label=r'H(t)', linewidth=1.5)
ax6w.bar(0,0,color = colormap(normalize(3)),label=r'$i(t)$', width=0.9)
ax6w.tick_params(axis='y', labelcolor=color)
ax6w.tick_params(labelsize='13',labeltop=False, labelright=True, labelbottom=False)
#ax6w.legend(borderpad=0.3, shadow = True, loc='upper left', ncol=1,fontsize=(13))
ax6w.set_xlim(right = 500 , left = 0)
ax6w.grid(True)


############################################################################


ax7.bar(d60a1[:,0],d60a1[:,2],color = colormap(normalize(3)), width=0.9)
ax7.tick_params(labelsize='13',labeltop=False, labelright=False, labelbottom=False)
ax7.set_ylim(top = max(d60a1[:,1]) + max(d60a1[:,1])/10 , bottom = 0)
ax7.set_xlim(right = 200 , left = 0)
ax7.set_xticks(x4)
ax7.set_yticklabels(['$0$','$1C$','$2C$','$3C$' ])
ax7.set_yticks([0,100,200,300])
ax7.grid(False)
ax7w = ax7.twinx()
ax7w.plot(d60a2[:,0],d60a2[:,1],color = colormap3(normalize3(1)),label=r'$W(t)$', linewidth=1.8)
ax7w.plot(d60a2[:,0],d60a2[:,2],color = colormap3(normalize3(2)),label=r'$C(t)$', linewidth=1.5)
ax7w.plot(d60a2[:,0],d60a2[:,3],color = colormap3(normalize3(3)),label=r'$H(t)$', linewidth=1.5)
ax7w.bar(0,0,color = colormap(normalize(3)),label=r'$i(t)$', width=0.9)
ax7w.tick_params(axis='y', labelcolor=color)
ax7w.tick_params(labelsize='13',labeltop=False, labelright=False, labelbottom=False)
#ax7w.legend(borderpad=0.3, shadow = True, loc='upper left', ncol=1,fontsize=(13))
ax7w.set_xlim(right = 200 , left = 0)
ax7w.grid(True)


ax8.bar(d60b1[:,0],d60b1[:,2],color = colormap(normalize(3)), width=0.9)
ax8.tick_params(labelsize='13',labeltop=False, labelright=False, labelbottom=False)
ax8.set_ylim(top = max(d60b1[:,1]) + max(d60b1[:,1])/10 , bottom = 0)
ax8.set_xlim(right = 500 , left = 0)
ax8.set_xticks(x5)
ax8.set_yticklabels(['$0$','$1C$','$2C$','$3C$' ])
ax8.set_yticks([0,100,200,300])
ax8.grid(False)
ax8w = ax8.twinx()
ax8w.plot(d60b2[:,0],d60b2[:,1],color = colormap3(normalize3(1)),label=r'$W(t)$', linewidth=1.8)
ax8w.plot(d60b2[:,0],d60b2[:,2],color = colormap3(normalize3(2)),label=r'$C(t)$', linewidth=1.5)
ax8w.plot(d60b2[:,0],d60b2[:,3],color = colormap3(normalize3(3)),label=r'$H(t)$', linewidth=1.5)
ax8w.bar(0,0,color = colormap(normalize(3)),label=r'$i(t)$', width=0.9)
ax8w.tick_params(axis='y', labelcolor=color)
ax8w.tick_params(labelsize='13',labeltop=False, labelright=False, labelbottom=False)
#ax8w.legend(borderpad=0.3, shadow = True, loc='upper left', ncol=1,fontsize=(13))
ax8w.set_xlim(right = 500 , left = 0)
ax8w.grid(True)


ax9.bar(d60c1[:,0],d60c1[:,2],color = colormap(normalize(3)), width=0.9)
ax9.tick_params(labelsize='13',labeltop=False, labelright=False, labelbottom=False)
ax9.set_ylim(top = max(d60c1[:,1]) + max(d60c1[:,1])/10 , bottom = 0)
ax9.set_xlim(right = 500 , left = 0)
ax9.set_xticks(x5)
ax9.set_yticklabels(['$0$','$5C$','$1K$'])
ax9.set_yticks([0,500,1000])
ax9.grid(False)
ax9w = ax9.twinx()
ax9w.plot(d60c2[:,0],d60c2[:,1],color = colormap3(normalize3(1)),label=r'$W(t)$', linewidth=1.8)
ax9w.plot(d60c2[:,0],d60c2[:,2],color = colormap3(normalize3(2)),label=r'$C(t)$', linewidth=1.5)
ax9w.plot(d60c2[:,0],d60c2[:,3],color = colormap3(normalize3(3)),label=r'$H(t)$', linewidth=1.5)
ax9w.bar(0,0,color = colormap(normalize(3)),label=r'$i(t)$', width=0.9)
ax9w.tick_params(axis='y', labelcolor=color)
ax9w.tick_params(labelsize='13',labeltop=False, labelright=True, labelbottom=False)
#ax9w.legend(borderpad=0.3, shadow = True, loc='upper left', ncol=1,fontsize=(13))
ax9w.set_xlim(right = 500 , left = 0)
ax9w.grid(True)


############################################################################


ax10.bar(d60i90d120a1[:,0],d60i90d120a1[:,2],color = colormap(normalize(3)), width=0.9)
ax10.tick_params(labelsize='13',labeltop=False, labelright=False, labelbottom=True)
ax10.set_ylim(top = max(d60i90d120a1[:,1]) + max(d60i90d120a1[:,1])/10 , bottom = 0)
ax10.set_xlim(right = 200 , left = 0)
ax10.set_xticks(x4)
ax10.set_yticklabels(['$0$','$1K$','$2K$'])
ax10.set_yticks([0,1000,2000])
ax10.grid(False)
ax10w = ax10.twinx()
ax10w.plot(d60i90d120a2[:,0],d60i90d120a2[:,1],color = colormap3(normalize3(1)),label=r'$W(t)$', linewidth=1.8)
ax10w.plot(d60i90d120a2[:,0],d60i90d120a2[:,2],color = colormap3(normalize3(2)),label=r'$C(t)$', linewidth=1.5)
ax10w.plot(d60i90d120a2[:,0],d60i90d120a2[:,3],color = colormap3(normalize3(3)),label=r'$H(t)$', linewidth=1.5)
ax10w.bar(0,0,color = colormap(normalize(3)),label=r'$i(t)$', width=0.9)
ax10w.tick_params(axis='y', labelcolor=color)
ax10w.tick_params(labelsize='13',labeltop=False, labelright=False, labelbottom=True)
#ax10w.legend(borderpad=0.3, shadow = True, loc='upper left', ncol=1,fontsize=(13))
ax10w.set_xlim(right = 200 , left = 0)
ax10w.grid(True)


ax11.bar(d60i90d120b1[:,0],d60i90d120b1[:,2],color = colormap(normalize(3)), width=0.9)
ax11.tick_params(labelsize='13',labeltop=False, labelright=False, labelbottom=True)
ax11.set_ylim(top = max(d60i90d120b1[:,1]) + max(d60i90d120b1[:,1])/10 , bottom = 0)
ax11.set_xlim(right = 500 , left = 0)
ax11.set_xticks(x5)
ax11.set_yticklabels(['$0$','$5C$','$1K$'])
ax11.set_yticks([0,500,1000])
ax11.grid(False)
ax11w = ax11.twinx()
ax11w.plot(d60i90d120b2[:,0],d60i90d120b2[:,1],color = colormap3(normalize3(1)),label=r'$W(t)$', linewidth=1.8)
ax11w.plot(d60i90d120b2[:,0],d60i90d120b2[:,2],color = colormap3(normalize3(2)),label=r'$C(t)$', linewidth=1.5)
ax11w.plot(d60i90d120b2[:,0],d60i90d120b2[:,3],color = colormap3(normalize3(3)),label=r'$H(t)$', linewidth=1.5)
ax11w.bar(0,0,color = colormap(normalize(3)),label=r'$i(t)$', width=0.9)
ax11w.tick_params(axis='y', labelcolor=color)
ax11w.tick_params(labelsize='13',labeltop=False, labelright=False, labelbottom=True)
#ax11w.legend(borderpad=0.3, shadow = True, loc='upper left', ncol=1,fontsize=(13))
ax11w.set_xlim(right = 500 , left = 0)
ax11w.grid(True)


ax12.bar(d60i90d120c1[:,0],d60i90d120c1[:,2],color = colormap(normalize(3)), width=0.9)
ax12.tick_params(labelsize='13',labeltop=False, labelright=False, labelbottom=True)
ax12.set_ylim(top = max(d60i90d120c1[:,1]) + max(d60i90d120c1[:,1])/10 , bottom = 0)
ax12.set_xlim(right = 500 , left = 0)
ax12.set_xticks(x5)
ax12.set_yticklabels(['$0$','$5C$','$1K$'])
ax12.set_yticks([0,500,1000])
ax12.grid(False)
ax12w = ax12.twinx()
ax12w.plot(d60i90d120c2[:,0],d60i90d120c2[:,1],color = colormap3(normalize3(1)),label=r'$W(t)$', linewidth=1.8)
ax12w.plot(d60i90d120c2[:,0],d60i90d120c2[:,2],color = colormap3(normalize3(2)),label=r'$C(t)$', linewidth=1.5)
ax12w.plot(d60i90d120c2[:,0],d60i90d120c2[:,3],color = colormap3(normalize3(3)),label=r'$H(t)$', linewidth=1.5)
ax12w.bar(0,0,color = colormap(normalize(3)),label=r'$i(t)$', width=0.9)
ax12w.tick_params(axis='y', labelcolor=color)
ax12w.tick_params(labelsize='13',labeltop=False, labelright=True, labelbottom=True)
#ax12w.legend(borderpad=0.3, shadow = True, loc='upper left', ncol=1,fontsize=(13))
ax12w.set_xlim(right = 500 , left = 0)
ax12w.grid(True)

plt.tight_layout()
figure_name = 'fig3.eps'	# name of the figure to be saved
plt.savefig(figure_name)

plt.show()
