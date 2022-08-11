import numpy as np
import matplotlib.pyplot as plt
import pylab
#from matplotlib import colors
from matplotlib import rc
import matplotlib.colors as mcolors
import matplotlib.cm as cm


gm5io1=np.loadtxt('gaussinadecay_1000/g10M_1conf2_gam5.0io0.01_poiss_i1_s9999999_l0_r0_d0_tr18_tl4_Ro4_iop0.0_wop2_let0.1_alph0.22/fort.25')
gm5io1w=np.loadtxt('gaussinadecay_1000/g10M_1conf2_gam5.0io0.01_poiss_i1_s9999999_l0_r0_d0_tr18_tl4_Ro4_iop0.0_wop2_let0.1_alph0.22/fort.16')

gm5io5=np.loadtxt('gaussinadecay_1000/g10M_1conf2_gam5.0io0.05_poiss_i1_s9999999_l0_r0_d0_tr18_tl4_Ro4_iop0.0_wop2_let0.1_alph0.22/fort.25')
gm5io5w=np.loadtxt('gaussinadecay_1000/g10M_1conf2_gam5.0io0.05_poiss_i1_s9999999_l0_r0_d0_tr18_tl4_Ro4_iop0.0_wop2_let0.1_alph0.22/fort.16')

gm5io10=np.loadtxt('gaussinadecay_1000/g10M_1conf2_gam5.0io0.1_poiss_i1_s9999999_l0_r0_d0_tr18_tl4_Ro4_iop0.0_wop2_let0.1_alph0.22/fort.25')
gm5io10w=np.loadtxt('gaussinadecay_1000/g10M_1conf2_gam5.0io0.1_poiss_i1_s9999999_l0_r0_d0_tr18_tl4_Ro4_iop0.0_wop2_let0.1_alph0.22/fort.16')


gm10io1=np.loadtxt('gaussinadecay_1000/g10M_1conf2_gam10.0io0.01_poiss_i1_s9999999_l0_r0_d0_tr18_tl4_Ro4_iop0.0_wop2_let0.1_alph0.22/fort.25')
gm10io1w=np.loadtxt('gaussinadecay_1000/g10M_1conf2_gam10.0io0.01_poiss_i1_s9999999_l0_r0_d0_tr18_tl4_Ro4_iop0.0_wop2_let0.1_alph0.22/fort.16')

gm10io5=np.loadtxt('gaussinadecay_1000/g10M_1conf2_gam10.0io0.05_poiss_i1_s9999999_l0_r0_d0_tr18_tl4_Ro4_iop0.0_wop2_let0.1_alph0.22/fort.25')
gm10io5w=np.loadtxt('gaussinadecay_1000/g10M_1conf2_gam10.0io0.05_poiss_i1_s9999999_l0_r0_d0_tr18_tl4_Ro4_iop0.0_wop2_let0.1_alph0.22/fort.16')

gm10io10=np.loadtxt('gaussinadecay_1000/g10M_1conf2_gam10.0io0.1_poiss_i1_s9999999_l0_r0_d0_tr18_tl4_Ro4_iop0.0_wop2_let0.1_alph0.22/fort.25')
gm10io10w=np.loadtxt('gaussinadecay_1000/g10M_1conf2_gam10.0io0.1_poiss_i1_s9999999_l0_r0_d0_tr18_tl4_Ro4_iop0.0_wop2_let0.1_alph0.22/fort.16')

gm20io1=np.loadtxt('gaussinadecay_1000/g10M_1conf2_gam20.0io0.01_poiss_i1_s9999999_l0_r0_d0_tr18_tl4_Ro4_iop0.0_wop2_let0.1_alph0.22/fort.25')
gm20io1w=np.loadtxt('gaussinadecay_1000/g10M_1conf2_gam20.0io0.01_poiss_i1_s9999999_l0_r0_d0_tr18_tl4_Ro4_iop0.0_wop2_let0.1_alph0.22/fort.16')

gm20io5=np.loadtxt('gaussinadecay_1000/g10M_1conf2_gam20.0io0.05_poiss_i1_s9999999_l0_r0_d0_tr18_tl4_Ro4_iop0.0_wop2_let0.1_alph0.22/fort.25')
gm20io5w=np.loadtxt('gaussinadecay_1000/g10M_1conf2_gam20.0io0.05_poiss_i1_s9999999_l0_r0_d0_tr18_tl4_Ro4_iop0.0_wop2_let0.1_alph0.22/fort.16')

g50io1=np.loadtxt('gaussinadecay_1000/g10M_1conf2_gam50.0io0.01_poiss_i1_s9999999_l0_r0_d0_tr18_tl4_Ro4_iop0.0_wop2_let0.1_alph0.22/fort.20')
g50io1w=np.loadtxt('gaussinadecay_1000/g10M_1conf2_gam50.0io0.01_poiss_i1_s9999999_l0_r0_d0_tr18_tl4_Ro4_iop0.0_wop2_let0.1_alph0.22/fort.16')




plt.rcParams['axes.linewidth'] = 2.0
plt.rcParams['xtick.major.width'] = 2.0
plt.rcParams['ytick.major.width'] = 2.0
plt.rcParams['xtick.major.size'] = 5
plt.rcParams['ytick.major.size'] = 5
rc('font', **{'family': 'sans-serif', 'serif': ['Computer Modern']})
rc('text', usetex=True)

# Choose a colormap
colormap2 = cm.viridis
mus2 = [1,2,3,4,5,6,7,8,9,10]
colorparams2 = mus2
normalize2 = mcolors.Normalize(vmin=np.min(colorparams2), vmax=np.max(colorparams2))

colormap = cm.inferno
mus = [1,2,3,4,5,6,7]
colorparams = mus
normalize = mcolors.Normalize(vmin=np.min(colorparams), vmax=np.max(colorparams))




fig = plt.figure(figsize=(18, 18))
#fig, ax = plt.subplots(nrows=3, ncols=3, sharex=True, sharey=True, figsize=(18, 18))
fig.text(0.51, 0.01, r'$\mathrm{days}$', ha='center',fontsize=(30))
#plt.subplots_adjust(left=0.1, right=0.95,top=0.95, bottom=0.13)
gs =  fig.add_gridspec(2,4)

ax1 = fig.add_subplot(gs[0, 0])
ax2 = fig.add_subplot(gs[0, 1])
ax3 = fig.add_subplot(gs[1, 0])
ax4 = fig.add_subplot(gs[1, 1])
ax5 = fig.add_subplot(gs[0:,2:])


x0=0
x1=93
x2=112
x3=102
x4=116
x7=200
yl = [r'$0.25$',r'$0.5$',r'$1$']
yn=[0.25,0.5,1]

###############################################################################
#ax1.axvspan(x0,x1,color='lightskyblue')
#ax1.axvspan(x1,x7,color='lightcyan')
ax1.bar(gm5io1[:,0], gm5io1[:,1],color = colormap2(normalize2(4)), width=0.9 )
ax1.plot(0,0,color = colormap(normalize(2)),label=r'$W(t)$', linewidth=2)
ax1.plot(0,0,color = colormap(normalize(4)),label=r'$C(t)$', linewidth=2)
ax1.plot(0,0,color = colormap(normalize(6)),label=r'$H(t)$', linewidth=2)
ax1.legend(borderpad=0.1, shadow = True, loc='center left', ncol=1,fontsize=(15))
ax1.tick_params(labelsize='18',labeltop=False, labelright=False, labelbottom=False)
ax1.set_ylim(top = max(gm5io1[:,1]) + max(gm5io1[:,1])/10 , bottom = 0)
ax1.set_xlim(right = 200 , left = 0)
ax1.set_xticks([0,100,200])
ax1.set_yticklabels([r'$0$',r'$75K$',r'$150K$'])
ax1.set_yticks([0,75000,150000])
ax1.grid(True)

axw1 = ax1.twinx()
axw1.tick_params(axis="y",direction="in", pad=-55)
color = 'tab:red'
axw1.plot(gm5io1w[:,0],gm5io1w[:,1],color = colormap(normalize(2)),label=r'$W(t)$', linewidth=2)
axw1.plot(gm5io1w[:,0],gm5io1w[:,2],color = colormap(normalize(4)),label=r'$C(t)$', linewidth=2)
axw1.plot(gm5io1w[:,0],gm5io1w[:,3],color = colormap(normalize(6)),label=r'$H(t)$', linewidth=2)
axw1.tick_params(axis='y', labelcolor=color)
axw1.tick_params(labelsize='18',labeltop=False, labelright=False, labelbottom=False)
axw1.set_yticks([0,1])
#axw1.grid(True)
#ax1.legend(borderpad=0.1, shadow = True, loc='lower left', ncol=1,fontsize=(15))

###############################################################################

#ax3.axvspan(x0,x3,color='lightskyblue')
#ax3.axvspan(x3,x7,color='lightcyan')
ax3.bar(gm5io10[:,0], gm5io10[:,1],color = colormap2(normalize2(4)), width=0.9 )
ax3.plot(0,0,color = colormap(normalize(2)),label=r'$W(t)$', linewidth=2)
ax3.plot(0,0,color = colormap(normalize(4)),label=r'$C(t)$', linewidth=2)
ax3.plot(0,0,color = colormap(normalize(6)),label=r'$H(t)$', linewidth=2)
#ax3.legend(borderpad=0.1, shadow = True, loc='best', ncol=1,fontsize=(15))
ax3.tick_params(labelsize='18',labeltop=False, labelright=False, labelbottom=True)
ax3.set_ylim(top = max(gm5io10[:,1]) + max(gm5io10[:,1])/10 , bottom = 0)
ax3.set_xlim(right = 200 , left = 0)
ax3.set_xticks([0,100,200])
ax3.set_yticklabels([r'$0$',r'$100K$',r'$200K$'])
ax3.set_yticks([0,100000,200000])
ax3.grid(True)

axw3 = ax3.twinx()
axw3.tick_params(axis="y",direction="in", pad=-55)
color = 'tab:red'
axw3.plot(gm5io10w[:,0],gm5io10w[:,1],color = colormap(normalize(2)),label=r'$W(t)$', linewidth=2)
axw3.plot(gm5io10w[:,0],gm5io10w[:,2],color = colormap(normalize(4)),label=r'$C(t)$', linewidth=2)
axw3.plot(gm5io10w[:,0],gm5io10w[:,3],color = colormap(normalize(6)),label=r'$H(t)$', linewidth=2)
axw3.tick_params(axis='y', labelcolor=color)
axw3.tick_params(labelsize='18',labeltop=False, labelright=False, labelbottom=False)
axw3.set_yticks([0,1])
#axw3.grid(True)

###############################################################################

#ax2.axvspan(x0,x2,color='lightskyblue')
#ax2.axvspan(x2,x7,color='lightcyan')
ax2.bar(gm10io1[:,0], gm10io1[:,1],color = colormap2(normalize2(4)), width=0.9 )
ax2.plot(0,0,color = colormap(normalize(2)),label=r'$W(t)$', linewidth=2)
ax2.plot(0,0,color = colormap(normalize(4)),label=r'$C(t)$', linewidth=2)
ax2.plot(0,0,color = colormap(normalize(6)),label=r'$H(t)$', linewidth=2)
#ax2.legend(borderpad=0.1, shadow = True, loc='best', ncol=1,fontsize=(15))
ax2.tick_params(labelsize='18',labeltop=False, labelright=False, labelbottom=False, labelleft=False)
ax2.set_ylim(top = max(gm5io1[:,1]) + max(gm5io1[:,1])/10 , bottom = 0)
ax2.set_xlim(right = 200 , left = 0)
ax2.set_xticks([0,100,200])
ax2.set_yticklabels([r'$0$',r'$75K$',r'$150K$'])
ax2.set_yticks([0,75000,150000])
ax2.grid(True)

axw2 = ax2.twinx()
axw2.tick_params(axis="y",direction="out", pad=-20)
color = 'tab:red'
axw2.plot(gm10io1w[:,0],gm10io1w[:,1],color = colormap(normalize(2)),label=r'$W(t)$', linewidth=2)
axw2.plot(gm10io1w[:,0],gm10io1w[:,2],color = colormap(normalize(4)),label=r'$C(t)$', linewidth=2)
axw2.plot(gm10io1w[:,0],gm10io1w[:,3],color = colormap(normalize(6)),label=r'$H(t)$', linewidth=2)
axw2.tick_params(axis='y', labelcolor=color)
axw2.tick_params(labelsize='18',labeltop=False, labelright=False, labelbottom=False)
axw2.set_yticks([0,1])
#axw2.grid(True)

###############################################################################

#ax4.axvspan(x0,x4,color='lightskyblue')
#ax4.axvspan(x4,x7,color='lightcyan')
ax4.bar(gm10io10[:,0], gm10io10[:,1],color = colormap2(normalize2(4)), width=0.9 )
ax4.plot(0,0,color = colormap(normalize(2)),label=r'$W(t)$', linewidth=2)
ax4.plot(0,0,color = colormap(normalize(4)),label=r'$C(t)$', linewidth=2)
ax4.plot(0,0,color = colormap(normalize(6)),label=r'$H(t)$', linewidth=2)
#ax4.legend(borderpad=0.1, shadow = True, loc='best', ncol=1,fontsize=(15))
ax4.tick_params(labelsize='18',labeltop=False, labelright=False, labelbottom=True, labelleft=False)
ax4.set_ylim(top = max(gm5io10[:,1]) + max(gm5io10[:,1])/10 , bottom = 0)
ax4.set_xlim(right = 200 , left = 0)
ax4.set_xticks([0,100,200])
ax4.set_yticklabels([r'$0$',r'$100K$',r'$200K$'])
ax4.set_yticks([0,100000,200000])
ax4.grid(True)

axw4 = ax4.twinx()
axw4.tick_params(axis="y",direction="out", pad=-20)
color = 'tab:red'
axw4.plot(gm10io10w[:,0],gm10io10w[:,1],color = colormap(normalize(2)),label=r'$W(t)$', linewidth=2)
axw4.plot(gm10io10w[:,0],gm10io10w[:,2],color = colormap(normalize(4)),label=r'$C(t)$', linewidth=2)
axw4.plot(gm10io10w[:,0],gm10io10w[:,3],color = colormap(normalize(6)),label=r'$H(t)$', linewidth=2)
axw4.tick_params(axis='y', labelcolor=color)
axw4.tick_params(labelsize='18',labeltop=False, labelright=False, labelbottom=False)
axw4.set_yticks([0,1])
#axw4.grid(True)

###############################################################################
ax5.axvspan(x0,x1,color='lightskyblue')
ax5.axvspan(x1,x7,color='lightcyan')
ax5.plot(0,0,color = colormap(normalize(1)),label=r'$W(t)$', linewidth=2)
ax5.plot(0,0,color = colormap(normalize(3)),label=r'$C(t)$', linewidth=2)
ax5.plot(0,0,color = colormap(normalize(5)),label=r'$H(t)$', linewidth=2)
ax5.plot(g50io1[:,0],g50io1[:,1],color = colormap2(normalize2(2)),linestyle='--',label=r'$L(t)$', linewidth=2)
ax5.plot(g50io1[:,0],g50io1[:,3],color = colormap2(normalize2(4)),linestyle='--',label=r'$I(t)$', linewidth=2)
# plt.plot(g50io1[:,0],g50io1[:,4],color = colormap(normalize(6)),linestyle='--',label=r'$R(t)/N$', linewidth=2)
# plt.plot(g50io1[:,0],g50io1[:,5],color = colormap(normalize(8)),linestyle='--',label=r'$D(t)/N$', linewidth=2)
# plt.plot(g50io1[:,0],g50io1[:,6],color = colormap(normalize(10)),linestyle='--',label=r'$CI(t)/N$', linewidth=2)
ax5.legend(borderpad=0.1, shadow = True, loc='lower left', ncol=1,fontsize=(18))
ax5.yaxis.set_label_position("right")
ax5.yaxis.tick_right()
ax5.tick_params(labelsize='18',labeltop=False, labelright=True,labelleft=False, labelbottom=True)
ax5.set_xlim(right = 200 , left = 0)
ax5.set_ylim(top = 500000 , bottom = 0)
x=[0,50,100,150,200]
ax5.set_xticks(x)
ax5.set_yticklabels([r'$0$',r'$200K$',r'$400K$'])
ax5.set_yticks([0,200000,400000])
ax5.grid(True)

axw5=plt.axes([0.52,0.61,.25,.32])
axw5.axvspan(x0,x1,color='lightskyblue')
axw5.axvspan(x1,x7,color='lightcyan')
axw5.plot(g50io1w[:,0],g50io1w[:,1],color = colormap(normalize(1)),label=r'$W(t)$', linewidth=2)
axw5.plot(g50io1w[:,0],g50io1w[:,2],color = colormap(normalize(3)),label=r'$C(t)$', linewidth=2)
axw5.plot(g50io1w[:,0],g50io1w[:,3],color = colormap(normalize(5)),label=r'$H(t)$', linewidth=2)
axw5.set_yticks(yn,yl)
axw5.yaxis.set_label_position("right")
axw5.yaxis.tick_right()
axw5.tick_params(labelsize='18',labeltop=False, labelright=True, labelbottom=True)
axw5.set_xlim(right = 200 , left = 0)
#p1.legend(borderpad=0.1, shadow = True, loc='lower left', ncol=1,fontsize=(10))
axw5.grid(True)


plt.tight_layout()
figure_name = 'fig2.eps'	# name of the figure to be saved
plt.savefig(figure_name)

plt.show()
