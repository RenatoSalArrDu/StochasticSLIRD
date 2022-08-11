import numpy as np
import matplotlib.pyplot as plt
import pylab
from numpy.fft import fft
from matplotlib import rc
import matplotlib.colors as mcolors
import matplotlib.cm as cm


cdmxp1=np.loadtxt('newfiguredatas/cdmx/punctual2/fort.15')
jalp1=np.loadtxt('newfiguredatas/jal/punctual2/fort.15')
nlp1=np.loadtxt('newfiguredatas/nl/punctual2/fort.15')
rtcdmx=np.loadtxt('newfiguredatas/cdmx/punctual2/fort.16')
rtjal=np.loadtxt('newfiguredatas/jal/punctual2/fort.16')
rtnl=np.loadtxt('newfiguredatas/nl/punctual2/fort.16')

campp1=np.loadtxt('newfiguredatas/camp/punctual2/fort.15')
nayp1=np.loadtxt('newfiguredatas/nay/punctual2/fort.15')
oaxp1=np.loadtxt('newfiguredatas/oax/punctual2/fort.15')
rtcamp=np.loadtxt('newfiguredatas/camp/punctual2/fort.16')
rtnay=np.loadtxt('newfiguredatas/nay/punctual2/fort.16')
rtoax=np.loadtxt('newfiguredatas/oax/punctual2/fort.16')

chisp1=np.loadtxt('newfiguredatas/chis/punctual2/fort.15')
edmxp1=np.loadtxt('newfiguredatas/edmx/punctual2/fort.15')
michp1=np.loadtxt('newfiguredatas/mich/punctual2/fort.15')
rtchis=np.loadtxt('newfiguredatas/chis/punctual2/fort.16')
rtedmx=np.loadtxt('newfiguredatas/edmx/punctual2/fort.16')
rtmich=np.loadtxt('newfiguredatas/mich/punctual2/fort.16')

cdmx=np.loadtxt('datas20_08_21/cdmx.dat')
jal=np.loadtxt('datas20_08_21/jal.dat')
nl=np.loadtxt('datas20_08_21/nl.dat')

camp=np.loadtxt('datas20_08_21/camp.dat')
nay=np.loadtxt('datas20_08_21/nay.dat')
oax=np.loadtxt('datas20_08_21/oax.dat')

chis=np.loadtxt('datas20_08_21/chis.dat')
edmx=np.loadtxt('datas20_08_21/edmx.dat')
mich=np.loadtxt('datas20_08_21/mich.dat')


Xcdmx = fft(rtcdmx[:,1])
Xjal = fft(rtjal[:,1])
Xnl = fft(rtnl[:,1])
Xcamp = fft(rtcamp[:,1])
Xnay = fft(rtnay[:,1])
Xoax = fft(rtoax[:,1])
Xchis = fft(rtchis[:,1])
Xedmx = fft(rtedmx[:,1])
Xmich = fft(rtmich[:,1])

N=len(Xcdmx)
n=np.arange(N)
T=N #/(2*np.pi)
omega= n /T



plt.rcParams['axes.linewidth'] = 2.0
plt.rcParams['xtick.major.width'] = 2.0
plt.rcParams['ytick.major.width'] = 2.0
plt.rcParams['xtick.major.size'] = 5
plt.rcParams['ytick.major.size'] = 5
rc('font', **{'family': 'sans-serif', 'serif': ['Computer Modern']})
rc('text', usetex=True)

style = dict(size=10, color='gray')

# Choose a colormap
colormap = cm.viridis
mus = [1,2,3,4,5,6,7,8,9]
colorparams = mus
normalize = mcolors.Normalize(vmin=np.min(colorparams), vmax=np.max(colorparams))

colormap2 = cm.tab10
mus2 = [1,2,3,4,5,6,7,8]
colorparams2 = mus2
normalize2 = mcolors.Normalize(vmin=np.min(colorparams2), vmax=np.max(colorparams2))




x=[0,200,400]
color = 'tab:red'
xl=[r'$0$',r'$0.25$',r'$0.5$']
xn=[0,0.25,0.5]
xlw=[r'$0$',r'$0.05$',r'$0.1$']
xnw=[0,0.05,0.1]

cdmxpx=[0.0037,0.0111,0.0298,0.1428,0.2857,0.4286,0.9888,0.9962]
jalpx=[0.0148,0.0241,0.0278,0.1428,0.2858,0.4286,0.9888,0.9962]
nlpx=[0.0079,0.0111,0.0148,0.0204,0.0259,0.1428,0.2857,0.4286,0.9888,0.9962]

edmxpx=[0.0037,0.0111,0.02412,0.1428,0.2857,0.4286,0.9888,0.9962]
michpx=[0.00927,0.01486,0.024128,0.14286,0.2858,0.4286,0.9888,0.9962]
chispx=[0.0056,0.0093,0.0167,0.03525,0.08535,0.1428,0.2857,0.4286,0.9888,0.9962]

oaxpx=[0.0075,0.0353,0.1428,0.2857,0.4286,0.9888,0.9962,0.999]
naypx=[0.0111,0.0225,0.03348,0.04645,0.1428,0.2857,0.9888,0.9962]
camppx=[0.00583,0.0188,0.02609,0.03743,0.1428,0.2857,0.4286,0.9888,0.9962,0.999]


cdmxpy=[33.5,25.75,9.455,25.534,17.743,8.9178,0.9888,0.9962]
jalpy=[25.281,11.588,14.1711,22.2331,14.1244,6.6005,0.9888,0.9962]
nlpy=[11.2709,24.6395,25.1804,16.8217,12.6327,22.35,16.5876,7.6497,0.9888,0.9962]

edmxpy=[31.875,23.108,8.8317,24.2306,19.0378,7.83315,0.9888,0.9962]
michpy=[23.6528,18.7811,12.6405,24.6299,16.0206,5.7488,0.9888,0.9962]
chispy=[19.4331,22.4589,17.9407,13.9961,6.7269,20.4357,14.1117,5.7552,0.9888,0.9962]

oaxpy=[20.9005,9.0307,18.1674,11.997,9.5522,0.9888,0.9962,0.999]
naypy=[29.1544,15.059,10.7111,11.2005,13.3303,11.7267,0.9888,0.9962]
camppy=[24.449,18.846,14.4214,12.7058,20.8676,15.5074,12.4385,0.9888,0.9962,0.999]



cdmxcb=np.arange(8)
jalcb=np.arange(8)
nlcb=np.arange(10)

edmxcb=np.arange(8)
michcb=np.arange(8)
chiscb=np.arange(10)

oaxcb=np.arange(8)
naycb=np.arange(8)
campcb=np.arange(10)


shcdmx=18
shjal=25
shnl=22
shedmx=20
shmich=35
shchis=39
shcamp=48
shnay=46
shoax=35



fig, ((ax1,ax2,ax3),(ax4,ax5,ax6) )= plt.subplots(nrows=2, ncols=3, sharex=False, sharey=False, figsize=(18, 18))
fig.text(0.51, 0.515, r'$\mathrm{days}$', ha='center',fontsize=(20))
fig.text(0.51, 0.01, r'$f[1/\mathrm{days}]$', ha='center',fontsize=(20))
plt.subplots_adjust(left=0.1, right=0.95,top=0.95, bottom=0.13)


################################################################################

####################################  Cdmx
ax1.bar(cdmxp1[:,0]+shcdmx,cdmxp1[:,1],color = colormap(normalize(1)),label=r'$\bar{i}_s,\; \mathrm{CDMX}$', width=0.9)
ax1.bar(cdmx[:,0],cdmx[:,1],color = colormap(normalize(4)),label=r'$i_e,\; \mathrm{CDMX}$', linewidth=0.8)
ax1.tick_params(labelsize='15',labeltop=False, labelright=False, labelbottom=True)
ax1.set_ylim(top = 10000, bottom = 0)
ax1.set_xlim(right = 570 , left = 0)
ax1.set_xticks(x)
ax1.set_yticklabels([r'$0$',r'$5K$',r'$10K$'])
ax1.set_yticks([0,5000,10000])
ax1.grid(False)
ax1w = ax1.twinx()
ax1w.bar(0,0,color = colormap(normalize(1)),label=r'$\bar{i}_s,\; \mathrm{CDMX}$', width=0.9)
ax1w.bar(0,0,color = colormap(normalize(4)),label=r'$i_e,\;\mathrm{CDMX}$', width=0.8)
ax1w.plot(rtcdmx[:,0]+shcdmx, rtcdmx[:,1],color = color,label=r'$W(t)$', linewidth=0.8)
ax1w.tick_params(axis='y', labelcolor=color)
ax1w.tick_params(labelsize='15',labeltop=False, labelright=False, labelbottom=False)
ax1w.legend(borderpad=0.3, shadow = True, loc='upper left', ncol=1,fontsize=(13))
ax1w.grid(True)

####################################  Edmx
# ax1.bar(edmxp1[:,0]+shedmx,edmxp1[:,1],color = colormap(normalize(1)),label=r'$\bar{i}_s,\; \mathrm{Edmx}$', width=0.9)
# ax1.bar(edmx[:,0],edmx[:,1],color = colormap(normalize(4)),label=r'$i_e,\; \mathrm{Edmx}$', linewidth=0.8)
# ax1.tick_params(labelsize='15',labeltop=False, labelright=False, labelbottom=True)
# ax1.set_ylim(top = 3000, bottom = 0)
# ax1.set_xlim(right = 570 , left = 0)
# ax1.set_xticks(x)
# ax1.set_yticklabels([r'$0$',r'$1K$',r'$2K$'])
# ax1.set_yticks([0,1000,2000])
# ax1.grid(False)
# ax1w = ax1.twinx()
# ax1w.bar(0,0,color = colormap(normalize(1)),label=r'$\bar{i}_s,\; \mathrm{Edmx}$', width=0.9)
# ax1w.bar(0,0,color = colormap(normalize(4)),label=r'$i_e,\;\mathrm{Edmx}$', width=0.8)
# ax1w.plot(rtedmx[:,0]+shedmx, rtedmx[:,1],color = color,label=r'$W(t)$', linewidth=0.8)
# ax1w.tick_params(axis='y', labelcolor=color)
# ax1w.tick_params(labelsize='15',labeltop=False, labelright=False, labelbottom=False)
# ax1w.legend(borderpad=0.3, shadow = True, loc='upper left', ncol=1,fontsize=(13))
# ax1w.grid(True)

####################################  Camp
# ax1.bar(campp1[:,0]+shcamp,campp1[:,1],color = colormap(normalize(1)),label=r'$\bar{i}_s,\; \mathrm{Camp}$', width=0.9)
# ax1.bar(camp[:,0],camp[:,1],color = colormap(normalize(4)),label=r'$i_e,\; \mathrm{Camp}$', linewidth=0.8)
# ax1.tick_params(labelsize='15',labeltop=False, labelright=False, labelbottom=True)
# ax1.set_ylim(top = 300, bottom = 0)
# ax1.set_xlim(right = 570 , left = 0)
# ax1.set_xticks(x)
# ax1.set_yticklabels([r'$0$',r'$1C$',r'$2C$'])
# ax1.set_yticks([0,100,200])
# ax1.grid(False)
# ax1w = ax1.twinx()
# ax1w.bar(0,0,color = colormap(normalize(1)),label=r'$\bar{i}_s,\; \mathrm{Camp}$', width=0.9)
# ax1w.bar(0,0,color = colormap(normalize(4)),label=r'$i_e,\;\mathrm{Camp}$', width=0.8)
# ax1w.plot(rtcamp[:,0]+shcamp, rtcamp[:,1],color = color,label=r'$W(t)$', linewidth=0.8)
# ax1w.tick_params(axis='y', labelcolor=color)
# ax1w.tick_params(labelsize='15',labeltop=False, labelright=False, labelbottom=False)
# ax1w.legend(borderpad=0.3, shadow = True, loc='upper left', ncol=1,fontsize=(13))
# ax1w.grid(True)

################################################################################
####################################  Jal
ax2.bar(jalp1[:,0]+shjal,jalp1[:,1],color = colormap(normalize(1)),label=r'$\bar{i}_s,\; \mathrm{Jal}$', width=0.9)
ax2.bar(jal[:,0],jal[:,1],color = colormap(normalize(4)),label=r'$i_e,\; \mathrm{jal}$', linewidth=0.8)
ax2.tick_params(labelsize='15',labeltop=False, labelright=False, labelbottom=True)
ax2.set_xlim(right = 570 , left = 0)
ax2.set_xticks(x)
ax2.set_ylim(top = 2000, bottom = 0)
ax2.set_yticklabels([r'$0$',r'$1K$',r'$2K$'])
ax2.set_yticks([0,1000,2000])
ax2.grid(False)
ax2w = ax2.twinx()
ax2w.bar(0,0,color = colormap(normalize(1)),label=r'$\bar{i}_s,\; \mathrm{Jal}$', width=0.9)
ax2w.bar(0,0,color = colormap(normalize(4)),label=r'$i_e,\;\mathrm{Jal}$', width=0.8)
ax2w.plot(rtjal[:,0]+shjal, rtjal[:,1],color = color,label=r'$W(t)$', linewidth=0.8)
ax2w.tick_params(axis='y', labelcolor=color)
ax2w.tick_params(labelsize='15',labeltop=False, labelright=False, labelbottom=False)
ax2w.legend(borderpad=0.3, shadow = True, loc='upper left', ncol=1,fontsize=(13))
ax2w.grid(True)

####################################  Mich
# ax2.bar(michp1[:,0]+shmich,michp1[:,1],color = colormap(normalize(1)),label=r'$\bar{i}_s,\; \mathrm{Mich}$', width=0.9)
# ax2.bar(mich[:,0],mich[:,1],color = colormap(normalize(4)),label=r'$i_e,\; \mathrm{Mich}$', linewidth=0.8)
# ax2.tick_params(labelsize='15',labeltop=False, labelright=False, labelbottom=True)
# ax2.set_xlim(right = 570 , left = 0)
# ax2.set_xticks(x)
# ax2.set_ylim(top = 600, bottom = 0)
# ax2.set_yticklabels([r'$0$',r'$2C$',r'$4C$'])
# ax2.set_yticks([0,200,400])
# ax2.grid(False)
# ax2w = ax2.twinx()
# ax2w.bar(0,0,color = colormap(normalize(1)),label=r'$\bar{i}_s,\; \mathrm{Mich}$', width=0.9)
# ax2w.bar(0,0,color = colormap(normalize(4)),label=r'$i_e,\;\mathrm{Mich}$', width=0.8)
# ax2w.plot(rtmich[:,0]+shmich, rtmich[:,1],color = color,label=r'$W(t)$', linewidth=0.8)
# ax2w.tick_params(axis='y', labelcolor=color)
# ax2w.tick_params(labelsize='15',labeltop=False, labelright=False, labelbottom=False)
# ax2w.legend(borderpad=0.3, shadow = True, loc='upper left', ncol=1,fontsize=(13))
# ax2w.grid(True)

####################################  Nay
# ax2.bar(nayp1[:,0]+shnay,nayp1[:,1],color = colormap(normalize(1)),label=r'$\bar{i}_s,\; \mathrm{Nay}$', width=0.9)
# ax2.bar(nay[:,0],nay[:,1],color = colormap(normalize(4)),label=r'$i_e,\; \mathrm{Nay}$', linewidth=0.8)
# ax2.tick_params(labelsize='15',labeltop=False, labelright=False, labelbottom=True)
# ax2.set_xlim(right = 570 , left = 0)
# ax2.set_xticks(x)
# ax2.set_ylim(top = 700, bottom = 0)
# ax2.set_yticklabels([r'$0$',r'$2C$',r'$4C$'])
# ax2.set_yticks([0,200,400])
# ax2.grid(False)
# ax2w = ax2.twinx()
# ax2w.bar(0,0,color = colormap(normalize(1)),label=r'$\bar{i}_s,\; \mathrm{Nay}$', width=0.9)
# ax2w.bar(0,0,color = colormap(normalize(4)),label=r'$i_e,\;\mathrm{Nay}$', width=0.8)
# ax2w.plot(rtnay[:,0]+shnay, rtnay[:,1],color = color,label=r'$W(t)$', linewidth=0.8)
# ax2w.tick_params(axis='y', labelcolor=color)
# ax2w.tick_params(labelsize='15',labeltop=False, labelright=False, labelbottom=False)
# ax2w.legend(borderpad=0.3, shadow = True, loc='upper left', ncol=1,fontsize=(13))
# ax2w.grid(True)

################################################################################
####################################  Nl
ax3.bar(nlp1[:,0]+shnl,nlp1[:,1],color = colormap(normalize(1)),label=r'$\bar{i}_e,\; \mathrm{NL}$', width=0.9)
ax3.bar(nl[:,0],nl[:,1],color = colormap(normalize(4)),label=r'$i_e,\; \mathrm{nl}$', linewidth=0.8)
ax3.tick_params(labelsize='15',labeltop=False, labelright=False, labelbottom=True)
ax3.set_xlim(right = 570 , left = 0)
ax3.set_xticks(x)
ax3.set_ylim(top = 2000, bottom = 0)
ax3.set_yticklabels([r'$0$',r'$1K$',r'$2K$'])
ax3.set_yticks([0,1000,2000])
ax3.grid(False)
ax3w = ax3.twinx()
ax3w.bar(0,0,color = colormap(normalize(1)),label=r'$\bar{i}_e,\; \mathrm{NL}$', width=0.9)
ax3w.bar(0,0,color = colormap(normalize(4)),label=r'$i_e,\;\mathrm{NL}$', width=0.8)
ax3w.plot(rtnl[:,0]+shnl, rtnl[:,1],color = color,label=r'$W(t)$', linewidth=0.8)
ax3w.tick_params(axis='y', labelcolor=color)
ax3w.tick_params(labelsize='15',labeltop=False, labelright=True, labelbottom=False)
ax3w.legend(borderpad=0.3, shadow = True, loc='upper left', ncol=1,fontsize=(13))
ax3w.grid(True)

####################################  Chis
# ax3.bar(chisp1[:,0]+shchis,chisp1[:,1],color = colormap(normalize(1)),label=r'$\bar{i}_e,\; \mathrm{Chis}$', width=0.9)
# ax3.bar(chis[:,0],chis[:,1],color = colormap(normalize(4)),label=r'$i_e,\; \mathrm{Chis}$', linewidth=0.8)
# ax3.tick_params(labelsize='15',labeltop=False, labelright=False, labelbottom=True)
# ax3.set_xlim(right = 570 , left = 0)
# ax3.set_xticks(x)
# ax3.set_ylim(top = 300, bottom = 0)
# ax3.set_yticklabels([r'$0$',r'$1C$',r'$2C$'])
# ax3.set_yticks([0,100,200])
# ax3.grid(False)
# ax3w = ax3.twinx()
# ax3w.bar(0,0,color = colormap(normalize(1)),label=r'$\bar{i}_e,\; \mathrm{Chis}$', width=0.9)
# ax3w.bar(0,0,color = colormap(normalize(4)),label=r'$i_e,\;\mathrm{Chis}$', width=0.8)
# ax3w.plot(rtchis[:,0]+shchis, rtchis[:,1],color = color,label=r'$W(t)$', linewidth=0.8)
# ax3w.tick_params(axis='y', labelcolor=color)
# ax3w.tick_params(labelsize='15',labeltop=False, labelright=True, labelbottom=False)
# ax3w.legend(borderpad=0.3, shadow = True, loc='upper left', ncol=1,fontsize=(13))
# ax3w.grid(True)

####################################  Oax
# ax3.bar(oaxp1[:,0]+shoax,oaxp1[:,1],color = colormap(normalize(1)),label=r'$\bar{i}_e,\; \mathrm{Oax}$', width=0.9)
# ax3.bar(oax[:,0],oax[:,1],color = colormap(normalize(4)),label=r'$i_e,\; \mathrm{Oax}$', linewidth=0.8)
# ax3.tick_params(labelsize='15',labeltop=False, labelright=False, labelbottom=True)
# ax3.set_xlim(right = 570 , left = 0)
# ax3.set_xticks(x)
# ax3.set_ylim(top = 800, bottom = 0)
# ax3.set_yticklabels([r'$0$',r'$3C$',r'$6C$'])
# ax3.set_yticks([0,300,600])
# ax3.grid(False)
# ax3w = ax3.twinx()
# ax3w.bar(0,0,color = colormap(normalize(1)),label=r'$\bar{i}_e,\; \mathrm{Oax}$', width=0.9)
# ax3w.bar(0,0,color = colormap(normalize(4)),label=r'$i_e,\;\mathrm{Oax}$', width=0.8)
# ax3w.plot(rtoax[:,0]+shoax, rtoax[:,1],color = color,label=r'$W(t)$', linewidth=0.8)
# ax3w.tick_params(axis='y', labelcolor=color)
# ax3w.tick_params(labelsize='15',labeltop=False, labelright=True, labelbottom=False)
# ax3w.legend(borderpad=0.3, shadow = True, loc='upper left', ncol=1,fontsize=(13))
# ax3w.grid(True)

###################################################################################################
###################################################################################################
###################################################################################################


####################################  Cdmx
ax4.plot(omega, abs(Xcdmx),color = 'k',linewidth=1.5)#,label=r'$|\hat{W}(f)|$', linewidth=1.5)
#ax4.scatter(cdmxpx,cdmxpy, c=cdmxcb, cmap=cm.tab10)
ax4.tick_params(labelsize='15',labeltop=False, labelright=False, labelbottom=True)
ax4.set_ylim(top = 50, bottom = 0)
ax4.set_xlim(left = 0, right = 0.5)
# #ax4.legend(borderpad=0.1, shadow = True, loc='upper right', ncol=8,fontsize=(11))
# ax4.set_xticklabels(xl)
# ax4.set_xticks(xn)

cdmxp1 = ax4.scatter(cdmxpx[0],cdmxpy[0], marker='o', color=colormap(normalize(1)))
cdmxp2 = ax4.scatter(cdmxpx[1],cdmxpy[1], marker='o', color=colormap(normalize(2)))
cdmxp3  = ax4.scatter(cdmxpx[2],cdmxpy[2], marker='o', color=colormap(normalize(3)))
cdmxp4  = ax4.scatter(cdmxpx[3],cdmxpy[3], marker='o', color=colormap(normalize(4)))
cdmxp5  = ax4.scatter(cdmxpx[4],cdmxpy[4], marker='o', color=colormap(normalize(5)))
cdmxp6 = ax4.scatter(cdmxpx[5],cdmxpy[5], marker='o', color=colormap(normalize(6)))
cdmxp7 = ax4.scatter(cdmxpx[6],cdmxpy[6], marker='o', color=colormap(normalize(7)))
cdmxp8 = ax4.scatter(cdmxpx[7],cdmxpy[7], marker='o', color=colormap(normalize(8)))

ax4.legend((cdmxp1, cdmxp2, cdmxp3, cdmxp4, cdmxp5, cdmxp6, cdmxp7, cdmxp8),
           (r'$T_1=270d$',r'$T_2=90d$', r'$T_3=33.5d$', r'$T_4=7d$', r'$T_5=3.5d$', r'$T_6=2.3d$'),
           scatterpoints=1,loc='upper right',ncol=1,fontsize=12)
ax4.grid(True)
sfax4=plt.axes([0.0495,0.33,.13,.15])
sfax4.plot(omega, abs(Xcdmx),color = 'k',label=r'$\hat{W}(f)$', linewidth=1.5)
sfax4.scatter(cdmxpx,cdmxpy, c=cdmxcb, cmap=cm.viridis)
sfax4.yaxis.set_label_position("right")
sfax4.yaxis.tick_right()
sfax4.tick_params(labelsize='15',labeltop=False, labelleft=False,labelright=True, labelbottom=True)
sfax4.set_xlim(right =0.1, left = -0.01)
sfax4.set_ylim(top = 50, bottom = 0)
sfax4.set_xticklabels(xlw)
sfax4.set_xticks(xnw)
sfax4.grid(True)


####################################  Edmx
# ax4.plot(omega, abs(Xedmx),color = 'k',linewidth=1.5)#,label=r'$|\hat{W}(f)|$', linewidth=1.5)
# #ax4.scatter(edmxpx,edmxpy, c=edmxcb, cmap=cm.tab10)
# ax4.tick_params(labelsize='15',labeltop=False, labelright=False, labelbottom=True)
# ax4.set_ylim(top = 50, bottom = 0)
# ax4.set_xlim(left = 0, right = 0.5)
# # ax4.set_xticklabels(xl)
# # ax4.set_xticks(xn)
# # #ax4.legend(borderpad=0.1, shadow = True, loc='upper right', ncol=8,fontsize=(11))
#
#
# edmxp1 = ax4.scatter(edmxpx[0],edmxpy[0], marker='o', color=colormap(normalize(1)))
# edmxp2 = ax4.scatter(edmxpx[1],edmxpy[1], marker='o', color=colormap(normalize(2)))
# edmxp3  = ax4.scatter(edmxpx[2],edmxpy[2], marker='o', color=colormap(normalize(3)))
# edmxp4  = ax4.scatter(edmxpx[3],edmxpy[3], marker='o', color=colormap(normalize(4)))
# edmxp5  = ax4.scatter(edmxpx[4],edmxpy[4], marker='o', color=colormap(normalize(5)))
# edmxp6 = ax4.scatter(edmxpx[5],edmxpy[5], marker='o', color=colormap(normalize(6)))
# edmxp7 = ax4.scatter(edmxpx[6],edmxpy[6], marker='o', color=colormap(normalize(7)))
# edmxp8 = ax4.scatter(edmxpx[7],edmxpy[7], marker='o', color=colormap(normalize(8)))
#
# ax4.legend((edmxp1, edmxp2, edmxp3, edmxp4, edmxp5, edmxp6, edmxp7, edmxp8),
#            (r'$T_1=270d$',r'$T_2=90d$', r'$T_3=41.5d$', r'$T_4=7d$', r'$T_5=3.5d$', r'$T_6=2.3d$'),
#            scatterpoints=1,loc='upper right',ncol=1,fontsize=12)
# ax4.grid(True)
# sfax4=plt.axes([0.0495,0.33,.13,.15])
# sfax4.plot(omega, abs(Xedmx),color = 'k',label=r'$\hat{W}(f)$', linewidth=1.5)
# sfax4.scatter(edmxpx,edmxpy, c=edmxcb, cmap=cm.viridis)
# sfax4.yaxis.set_label_position("right")
# sfax4.yaxis.tick_right()
# sfax4.tick_params(labelsize='15',labeltop=False, labelleft=False,labelright=True, labelbottom=True)
# sfax4.set_xlim(right =0.1, left = -0.01)
# sfax4.set_ylim(top = 50, bottom = 0)
# sfax4.set_xticklabels(xlw)
# sfax4.set_xticks(xnw)
# sfax4.grid(True)

####################################  Oax
# ax4.plot(omega, abs(Xoax),color = 'k',linewidth=1.5)#,label=r'$|\hat{W}(f)|$', linewidth=1.5)
# #ax4.scatter(oaxpx,oaxpy, c=oaxcb, cmap=cm.tab10)
# ax4.tick_params(labelsize='15',labeltop=False, labelright=False, labelbottom=True)
# ax4.set_ylim(top = 50, bottom = 0)
# ax4.set_xlim(left = 0, right = 0.5)
# # ax4.set_xticklabels(xl)
# # ax4.set_xticks(xn)
# # #ax4.legend(borderpad=0.1, shadow = True, loc='upper right', ncol=8,fontsize=(11))
#
#
# oaxp1 = ax4.scatter(oaxpx[0],oaxpy[0], marker='o', color=colormap(normalize(1)))
# oaxp2 = ax4.scatter(oaxpx[1],oaxpy[1], marker='o', color=colormap(normalize(2)))
# oaxp3  = ax4.scatter(oaxpx[2],oaxpy[2], marker='o', color=colormap(normalize(3)))
# oaxp4  = ax4.scatter(oaxpx[3],oaxpy[3], marker='o', color=colormap(normalize(4)))
# oaxp5  = ax4.scatter(oaxpx[4],oaxpy[4], marker='o', color=colormap(normalize(5)))
# oaxp6 = ax4.scatter(oaxpx[5],oaxpy[5], marker='o', color=colormap(normalize(6)))
# oaxp7 = ax4.scatter(oaxpx[6],oaxpy[6], marker='o', color=colormap(normalize(7)))
# oaxp8 = ax4.scatter(oaxpx[7],oaxpy[7], marker='o', color=colormap(normalize(8)))
#
# ax4.legend((oaxp1, oaxp2, oaxp3, oaxp4, oaxp5, oaxp6, oaxp7, oaxp8),
#            (r'$T_1=133.3d$',r'$T_2=28.33d$',r'$T_3=7d$', r'$T_4=3.5d$', r'$T_5=2.3d$'),
#            scatterpoints=1,loc='upper right',ncol=1,fontsize=12)
# ax4.grid(True)
# sfax4=plt.axes([0.0495,0.33,.13,.15])
# sfax4.plot(omega, abs(Xoax),color = 'k',label=r'$\hat{W}(f)$', linewidth=1.5)
# sfax4.scatter(oaxpx,oaxpy, c=oaxcb, cmap=cm.viridis)
# sfax4.yaxis.set_label_position("right")
# sfax4.yaxis.tick_right()
# sfax4.tick_params(labelsize='15',labeltop=False, labelleft=False,labelright=True, labelbottom=True)
# sfax4.set_xlim(right =0.1, left = -0.01)
# sfax4.set_ylim(top = 50, bottom = 0)
# sfax4.set_xticklabels(xlw)
# sfax4.set_xticks(xnw)
# sfax4.grid(True)

################################################################################
####################################  Jal

ax5.plot(omega, abs(Xjal),color = 'k', linewidth=1.5)
ax5.scatter(jalpx,jalpy, c=jalcb, cmap=cm.Reds_r)
ax5.tick_params(labelsize='15',labeltop=False, labelright=False, labelbottom=True)
ax5.set_ylim(top = 50, bottom = 0)
ax5.legend(borderpad=0.3, shadow = True, loc='upper left', ncol=1,fontsize=(13))
# ax5.set_xticklabels(xl)
# ax5.set_xticks(xn)
ax5.set_xlim(left = 0, right = 0.5)

jalp1 = ax5.scatter(jalpx[0],jalpy[0], marker='o', color=colormap(normalize(1)))
jalp2 = ax5.scatter(jalpx[1],jalpy[1], marker='o', color=colormap(normalize(2)))
jalp3  = ax5.scatter(jalpx[2],jalpy[2], marker='o', color=colormap(normalize(3)))
jalp4  = ax5.scatter(jalpx[3],jalpy[3], marker='o', color=colormap(normalize(4)))
jalp5  = ax5.scatter(jalpx[4],jalpy[4], marker='o', color=colormap(normalize(5)))
jalp6 = ax5.scatter(jalpx[5],jalpy[5], marker='o', color=colormap(normalize(6)))
jalp7 = ax5.scatter(jalpx[6],jalpy[6], marker='o', color=colormap(normalize(7)))
jalp8 = ax5.scatter(jalpx[7],jalpy[7], marker='o', color=colormap(normalize(8)))

ax5.legend((jalp1, jalp2, jalp3, jalp4, jalp5, jalp6, jalp7, jalp8),
           (r'$T_1=67.5d$',r'$T_2=41.5d$', r'$T_3=36d$', r'$T_4=7d$', r'$T_5=3.5d$', r'$T_6=2.3d$'),
           scatterpoints=1,loc='upper right',ncol=1,fontsize=12)


ax5.grid(True)
sfax5=plt.axes([0.3725,0.33,.13,.15])
sfax5.plot(omega, abs(Xjal),color = 'k',label=r'$\hat{W}(f)$', linewidth=1.5)
sfax5.scatter(jalpx,jalpy, c=jalcb, cmap=cm.viridis)
sfax5.yaxis.set_label_position("right")
sfax5.yaxis.tick_right()
sfax5.tick_params(labelsize='15',labeltop=False, labelright=True,labelleft=False, labelbottom=True)
sfax5.set_xlim(right = 0.1 , left = -0.01)
sfax5.set_ylim(top = 50, bottom = 0)
sfax5.set_xticklabels(xlw)
sfax5.set_xticks(xnw)
sfax5.grid(True)

####################################  Mich
# ax5.plot(omega, abs(Xmich),color = 'k', linewidth=1.5)
# ax5.scatter(michpx,michpy, c=michcb, cmap=cm.Reds_r)
# ax5.tick_params(labelsize='15',labeltop=False, labelright=False, labelbottom=True)
# ax5.set_ylim(top = 50, bottom = 0)
# ax5.legend(borderpad=0.3, shadow = True, loc='upper left', ncol=1,fontsize=(13))
# # ax5.set_xticklabels(xl)
# # ax5.set_xticks(xn)
# ax5.set_xlim(left = 0, right = 0.5)
#
# michp1 = ax5.scatter(michpx[0],michpy[0], marker='o', color=colormap(normalize(1)))
# michp2 = ax5.scatter(michpx[1],michpy[1], marker='o', color=colormap(normalize(2)))
# michp3  = ax5.scatter(michpx[2],michpy[2], marker='o', color=colormap(normalize(3)))
# michp4  = ax5.scatter(michpx[3],michpy[3], marker='o', color=colormap(normalize(4)))
# michp5  = ax5.scatter(michpx[4],michpy[4], marker='o', color=colormap(normalize(5)))
# michp6 = ax5.scatter(michpx[5],michpy[5], marker='o', color=colormap(normalize(6)))
# michp7 = ax5.scatter(michpx[6],michpy[6], marker='o', color=colormap(normalize(7)))
# michp8 = ax5.scatter(michpx[7],michpy[7], marker='o', color=colormap(normalize(8)))
#
# ax5.legend((michp1, michp2, michp3, michp4, michp5, michp6, michp7, michp8),
#            (r'$T_1=108d$',r'$T_2=67.3d$', r'$T_3=41.5d$', r'$T_4=7d$', r'$T_5=3.5d$', r'$T_6=2.3d$'),
#            scatterpoints=1,loc='upper right',ncol=1,fontsize=12)
#
#
# ax5.grid(True)
# sfax5=plt.axes([0.3725,0.33,.13,.15])
# sfax5.plot(omega, abs(Xmich),color = 'k',label=r'$\hat{W}(f)$', linewidth=1.5)
# sfax5.scatter(michpx,michpy, c=michcb, cmap=cm.viridis)
# sfax5.yaxis.set_label_position("right")
# sfax5.yaxis.tick_right()
# sfax5.tick_params(labelsize='15',labeltop=False, labelright=True,labelleft=False, labelbottom=True)
# sfax5.set_xlim(right = 0.1 , left = -0.01)
# sfax5.set_ylim(top = 50, bottom = 0)
# sfax5.set_xticklabels(xlw)
# sfax5.set_xticks(xnw)
# sfax5.grid(True)

####################################  Nay
# ax5.plot(omega, abs(Xnay),color = 'k', linewidth=1.5)
# ax5.scatter(naypx,naypy, c=naycb, cmap=cm.Reds_r)
# ax5.tick_params(labelsize='15',labeltop=False, labelright=False, labelbottom=True)
# ax5.set_ylim(top = 50, bottom = 0)
# ax5.legend(borderpad=0.3, shadow = True, loc='upper left', ncol=1,fontsize=(13))
# # ax5.set_xticklabels(xl)
# # ax5.set_xticks(xn)
# ax5.set_xlim(left = 0, right = 0.5)
#
# nayp1 = ax5.scatter(naypx[0],naypy[0], marker='o', color=colormap(normalize(1)))
# nayp2 = ax5.scatter(naypx[1],naypy[1], marker='o', color=colormap(normalize(2)))
# nayp3  = ax5.scatter(naypx[2],naypy[2], marker='o', color=colormap(normalize(3)))
# nayp4  = ax5.scatter(naypx[3],naypy[3], marker='o', color=colormap(normalize(4)))
# nayp5  = ax5.scatter(naypx[4],naypy[4], marker='o', color=colormap(normalize(5)))
# nayp6 = ax5.scatter(naypx[5],naypy[5], marker='o', color=colormap(normalize(6)))
# nayp7 = ax5.scatter(naypx[6],naypy[6], marker='o', color=colormap(normalize(7)))
# nayp8 = ax5.scatter(naypx[7],naypy[7], marker='o', color=colormap(normalize(8)))
#
# ax5.legend((nayp1, nayp2, nayp3, nayp4, nayp5, nayp6, nayp7, nayp8),
#            (r'$T_1=90d$',r'$T_2=44.4d$', r'$T_3=30d$', r'$T_4=21.5d$', r'$T_5=7d$', r'$T_6=3.5d$'),
#            scatterpoints=1,loc='upper right',ncol=1,fontsize=12)
#
#
# ax5.grid(True)
# sfax5=plt.axes([0.3725,0.33,.13,.15])
# sfax5.plot(omega, abs(Xnay),color = 'k',label=r'$\hat{W}(f)$', linewidth=1.5)
# sfax5.scatter(naypx,naypy, c=naycb, cmap=cm.viridis)
# sfax5.yaxis.set_label_position("right")
# sfax5.yaxis.tick_right()
# sfax5.tick_params(labelsize='15',labeltop=False, labelright=True,labelleft=False, labelbottom=True)
# sfax5.set_xlim(right = 0.1 , left = -0.01)
# sfax5.set_ylim(top = 50, bottom = 0)
# sfax5.set_xticklabels(xlw)
# sfax5.set_xticks(xnw)
# sfax5.grid(True)

################################################################################
####################################  NL
ax6.plot(omega, abs(Xnl),color = 'k', linewidth=1.5)
ax6.scatter(nlpx,nlpy, c=nlcb, cmap=cm.Reds_r)
ax6.tick_params(labelsize='15',labeltop=False, labelright=False, labelbottom=True)
ax6.set_ylim(top = 50, bottom = 0)
ax6.legend(borderpad=0.3, shadow = True, loc='upper left', ncol=1,fontsize=(13))
# ax6.set_xticklabels(xl)
# ax6.set_xticks(xn)
ax6.set_xlim(left = 0, right = 0.5)
nlp1 = ax6.scatter(nlpx[0],nlpy[0], marker='o', color=colormap(normalize(1)))
nlp2 = ax6.scatter(nlpx[1],nlpy[1], marker='o', color=colormap(normalize(2)))
nlp3  = ax6.scatter(nlpx[2],nlpy[2], marker='o', color=colormap(normalize(3)))
nlp4  = ax6.scatter(nlpx[3],nlpy[3], marker='o', color=colormap(normalize(4)))
nlp5  = ax6.scatter(nlpx[4],nlpy[4], marker='o', color=colormap(normalize(5)))
nlp6 = ax6.scatter(nlpx[5],nlpy[5], marker='o', color=colormap(normalize(6)))
nlp7 = ax6.scatter(nlpx[6],nlpy[6], marker='o', color=colormap(normalize(7)))
nlp8 = ax6.scatter(nlpx[7],nlpy[7], marker='o', color=colormap(normalize(8)))
nlp9 = ax6.scatter(nlpx[8],nlpy[8], marker='o', color=colormap(normalize(9)))

ax6.legend((nlp1, nlp2, nlp3, nlp4, nlp5, nlp6, nlp7, nlp8, nlp9),
           (r'$T_1=126d$',r'$T_2=90d$', r'$T_3=67.5d$', r'$T_4=49d$', r'$T_5=38d$', r'$T_6=7d$',r'$T_7=3.5d$',r'$T_8=2.3d$'),
           scatterpoints=1,loc='upper right',ncol=1,fontsize=12)
ax6.grid(True)
sfax6=plt.axes([0.696,0.33,.13,.15])
sfax6.plot(omega, abs(Xnl),color = 'k',label=r'$\hat{W}(f)$', linewidth=1.5)
sfax6.yaxis.set_label_position("right")
sfax6.yaxis.tick_right()
sfax6.scatter(nlpx,nlpy, c=nlcb, cmap=cm.viridis)
sfax6.tick_params(labelsize='15',labeltop=False, labelright=True, labelleft=False, labelbottom=True)
sfax6.set_xlim(right = 0.1 , left = -0.01)
sfax6.set_ylim(top = 50, bottom = 0)
sfax6.set_xticklabels(xlw)
sfax6.set_xticks(xnw)
sfax6.grid(True)

#################################### Chis
# ax6.plot(omega, abs(Xchis),color = 'k', linewidth=1.5)
# ax6.scatter(chispx,chispy, c=chiscb, cmap=cm.Reds_r)
# ax6.tick_params(labelsize='15',labeltop=False, labelright=False, labelbottom=True)
# ax6.set_ylim(top = 50, bottom = 0)
# ax6.legend(borderpad=0.3, shadow = True, loc='upper left', ncol=1,fontsize=(13))
# # ax6.set_xticklabels(xl)
# # ax6.set_xticks(xn)
# ax6.set_xlim(left = 0, right = 0.5)
# chisp1 = ax6.scatter(chispx[0],chispy[0], marker='o', color=colormap(normalize(1)))
# chisp2 = ax6.scatter(chispx[1],chispy[1], marker='o', color=colormap(normalize(2)))
# chisp3  = ax6.scatter(chispx[2],chispy[2], marker='o', color=colormap(normalize(3)))
# chisp4  = ax6.scatter(chispx[3],chispy[3], marker='o', color=colormap(normalize(4)))
# chisp5  = ax6.scatter(chispx[4],chispy[4], marker='o', color=colormap(normalize(5)))
# chisp6 = ax6.scatter(chispx[5],chispy[5], marker='o', color=colormap(normalize(6)))
# chisp7 = ax6.scatter(chispx[6],chispy[6], marker='o', color=colormap(normalize(7)))
# chisp8 = ax6.scatter(chispx[7],chispy[7], marker='o', color=colormap(normalize(8)))
# chisp9 = ax6.scatter(chispx[8],chispy[8], marker='o', color=colormap(normalize(9)))
#
# ax6.legend((chisp1, chisp2, chisp3, chisp4, chisp5, chisp6, chisp7, chisp8, chisp9),
#            (r'$T_1=179d$',r'$T_2=107.5d$', r'$T_3=60d$', r'$T_4=28.4d$', r'$T_5=12d$', r'$T_6=7d$',r'$T_7=3.5d$',r'$T_8=2.3d$'),
#            scatterpoints=1,loc='upper right',ncol=1,fontsize=12)
# ax6.grid(True)
# sfax6=plt.axes([0.696,0.33,.13,.15])
# sfax6.plot(omega, abs(Xchis),color = 'k',label=r'$\hat{W}(f)$', linewidth=1.5)
# sfax6.yaxis.set_label_position("right")
# sfax6.yaxis.tick_right()
# sfax6.scatter(chispx,chispy, c=chiscb, cmap=cm.viridis)
# sfax6.tick_params(labelsize='15',labeltop=False, labelright=True, labelleft=False, labelbottom=True)
# sfax6.set_xlim(right = 0.1 , left = -0.01)
# sfax6.set_ylim(top = 50, bottom = 0)
# sfax6.set_xticklabels(xlw)
# sfax6.set_xticks(xnw)
# sfax6.grid(True)

#################################### Camp
# ax6.plot(omega, abs(Xcamp),color = 'k', linewidth=1.5)
# ax6.scatter(camppx,camppy, c=campcb, cmap=cm.Reds_r)
# ax6.tick_params(labelsize='15',labeltop=False, labelright=False, labelbottom=True)
# ax6.set_ylim(top = 50, bottom = 0)
# ax6.legend(borderpad=0.3, shadow = True, loc='upper left', ncol=1,fontsize=(13))
# # ax6.set_xticklabels(xl)
# # ax6.set_xticks(xn)
# ax6.set_xlim(left = 0, right = 0.5)
# campp1 = ax6.scatter(camppx[0],camppy[0], marker='o', color=colormap(normalize(1)))
# campp2 = ax6.scatter(camppx[1],camppy[1], marker='o', color=colormap(normalize(2)))
# campp3  = ax6.scatter(camppx[2],camppy[2], marker='o', color=colormap(normalize(3)))
# campp4  = ax6.scatter(camppx[3],camppy[3], marker='o', color=colormap(normalize(4)))
# campp5  = ax6.scatter(camppx[4],camppy[4], marker='o', color=colormap(normalize(5)))
# campp6 = ax6.scatter(camppx[5],camppy[5], marker='o', color=colormap(normalize(6)))
# campp7 = ax6.scatter(camppx[6],camppy[6], marker='o', color=colormap(normalize(7)))
# campp8 = ax6.scatter(camppx[7],camppy[7], marker='o', color=colormap(normalize(8)))
# campp9 = ax6.scatter(camppx[8],camppy[8], marker='o', color=colormap(normalize(9)))
#
# ax6.legend((campp1, campp2, campp3, campp4, campp5, campp6, campp7, campp8, campp9),
#            (r'$T_1=171.5d$',r'$T_2=53.2d$', r'$T_3=38.3d$', r'$T_4=26.7d$', r'$T_5=7d$', r'$T_6=3.5d$',r'$T_7=2.3d$'),
#            scatterpoints=1,loc='upper right',ncol=1,fontsize=12)
# ax6.grid(True)
# sfax6=plt.axes([0.696,0.33,.13,.15])
# sfax6.plot(omega, abs(Xcamp),color = 'k',label=r'$\hat{W}(f)$', linewidth=1.5)
# sfax6.yaxis.set_label_position("right")
# sfax6.yaxis.tick_right()
# sfax6.scatter(camppx,camppy, c=campcb, cmap=cm.viridis)
# sfax6.tick_params(labelsize='15',labeltop=False, labelright=True, labelleft=False, labelbottom=True)
# sfax6.set_xlim(right = 0.1 , left = -0.01)
# sfax6.set_ylim(top = 50, bottom = 0)
# sfax6.set_xticklabels(xlw)
# sfax6.set_xticks(xnw)
# sfax6.grid(True)

plt.show()
