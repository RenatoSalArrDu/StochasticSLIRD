import numpy as np
import matplotlib.pyplot as plt
import pylab
#from matplotlib import colors
from matplotlib import rc
import matplotlib.colors as mcolors
import matplotlib.cm as cm

cdmx=np.loadtxt('datas20_08_21/cdmx.dat')
jal=np.loadtxt('datas20_08_21/jal.dat')
nl=np.loadtxt('datas20_08_21/nl.dat')

edmx = np.loadtxt('datas20_08_21/edmx.dat')
mich = np.loadtxt('datas20_08_21/mich.dat')
chis = np.loadtxt('datas20_08_21/chis.dat')

camp = np.loadtxt('datas20_08_21/camp.dat')
nay = np.loadtxt('datas20_08_21/nay.dat')
oax = np.loadtxt('datas20_08_21/oax.dat')



cdmxp1=np.loadtxt('newfiguredatas/cdmx/punctual2/fort.15') # av incidence cumm max and min
cdmxp2=np.loadtxt('newfiguredatas/cdmx/punctual2/fort.16') # R(t)
cdmxp3=np.loadtxt('newfiguredatas/cdmx/punctual2/fort.105') #quartils

jalp1=np.loadtxt('newfiguredatas/jal/punctual2/fort.15')
jalp2=np.loadtxt('newfiguredatas/jal/punctual2/fort.16')
jalp3=np.loadtxt('newfiguredatas/jal/punctual2/fort.105')

nlp1=np.loadtxt('newfiguredatas/nl/punctual2/fort.15')
nlp2=np.loadtxt('newfiguredatas/nl/punctual2/fort.16')
nlp3=np.loadtxt('newfiguredatas/nl/punctual2/fort.105')

edmxp1=np.loadtxt('newfiguredatas/edmx/punctual2/fort.15') # av incidence cumm max and min
edmxp2=np.loadtxt('newfiguredatas/edmx/punctual2/fort.16') # R(t)
edmxp3=np.loadtxt('newfiguredatas/edmx/punctual2/fort.105') #quartils

michp1=np.loadtxt('newfiguredatas/mich/punctual2/fort.15')
michp2=np.loadtxt('newfiguredatas/mich/punctual2/fort.16')
michp3=np.loadtxt('newfiguredatas/mich/punctual2/fort.105')

chisp1=np.loadtxt('newfiguredatas/chis/punctual2/fort.15')
chisp2=np.loadtxt('newfiguredatas/chis/punctual2/fort.16')
chisp3=np.loadtxt('newfiguredatas/chis/punctual2/fort.105')


campp1=np.loadtxt('newfiguredatas/camp/punctual2/fort.15') # av incidence cumm max and min
campp2=np.loadtxt('newfiguredatas/camp/punctual2/fort.16') # R(t)
campp3=np.loadtxt('newfiguredatas/camp/punctual2/fort.105') #quartils

nayp1=np.loadtxt('newfiguredatas/nay/punctual2/fort.15')
nayp2=np.loadtxt('newfiguredatas/nay/punctual2/fort.16')
nayp3=np.loadtxt('newfiguredatas/nay/punctual2/fort.105')

oaxp1=np.loadtxt('newfiguredatas/oax/punctual2/fort.15')
oaxp2=np.loadtxt('newfiguredatas/oax/punctual2/fort.16')
oaxp3=np.loadtxt('newfiguredatas/oax/punctual2/fort.105')



shcdmx=18
cdmxtot=len(cdmx[:,0])
cdmxtotp=len(cdmxp1[:,0])
cdmxcum = np.zeros(shape=(cdmxtot,1))
cdmxcump = np.zeros(shape=(cdmxtotp,1))
cdmxcum[0] = cdmx[0,1]
cdmxcump[0] = cdmxp1[0,1]
for j in range(0,cdmxtot-1):
    cdmxcum[j+1] += cdmxcum[j] + cdmx[j+1,1]
for j in range(0,cdmxtotp-1):
    cdmxcump[j+1] += cdmxcump[j] + cdmxp1[j+1,1]


shjal=25
jaltot=len(jal[:,0])
jaltotp=len(jalp1[:,0])
jalcum = np.zeros(shape=(jaltot,1))
jalcump = np.zeros(shape=(jaltotp,1))
jalcum[0] = jal[0,1]
jalcump[0] = jalp1[0,1]
for j in range(0,jaltot-1):
    jalcum[j+1] += jalcum[j] + jal[j+1,1]
for j in range(0,jaltotp-1):
    jalcump[j+1] += jalcump[j] + jalp1[j+1,1]

shnl=22
nltot=len(nl[:,0])
nltotp=len(nlp1[:,0])
nlcum = np.zeros(shape=(nltot,1))
nlcump = np.zeros(shape=(nltotp,1))
nlcum[0] = nl[0,1]
nlcump[0] = nlp1[0,1]
for j in range(0,nltot-1):
    nlcum[j+1] += nlcum[j] + nl[j+1,1]
for j in range(0,nltotp-1):
    nlcump[j+1] += nlcump[j] + nlp1[j+1,1]


shedmx=20
edmxtot=len(edmx[:,0])
edmxtotp=len(edmxp1[:,0])
edmxcum = np.zeros(shape=(edmxtot,1))
edmxcump = np.zeros(shape=(edmxtotp,1))
edmxcum[0] = edmx[0,1]
edmxcump[0] = edmxp1[0,1]
for j in range(0,edmxtot-1):
    edmxcum[j+1] += edmxcum[j] + edmx[j+1,1]
for j in range(0,edmxtotp-1):
    edmxcump[j+1] += edmxcump[j] + edmxp1[j+1,1]

shmich=35
michtot=len(mich[:,0])
michtotp=len(michp1[:,0])
michcum = np.zeros(shape=(michtot,1))
michcump = np.zeros(shape=(michtotp,1))
michcum[0] = mich[0,1]
michcump[0] = michp1[0,1]
for j in range(0,michtot-1):
    michcum[j+1] += michcum[j] + mich[j+1,1]
for j in range(0,michtotp-1):
    michcump[j+1] += michcump[j] + michp1[j+1,1]

shchis=39
chistot=len(chis[:,0])
chistotp=len(chisp1[:,0])
chiscum = np.zeros(shape=(chistot,1))
chiscump = np.zeros(shape=(chistotp,1))
chiscum[0] = chis[0,1]
chiscump[0] = chisp1[0,1]
for j in range(0,chistot-1):
    chiscum[j+1] += chiscum[j] + chis[j+1,1]
for j in range(0,chistotp-1):
    chiscump[j+1] += chiscump[j] + chisp1[j+1,1]


shcamp=48
camptot=len(camp[:,0])
camptotp=len(campp1[:,0])
campcum = np.zeros(shape=(camptot,1))
campcump = np.zeros(shape=(camptotp,1))
campcum[0] = camp[0,1]
campcump[0] = campp1[0,1]
for j in range(0,camptot-1):
    campcum[j+1] += campcum[j] + camp[j+1,1]
for j in range(0,camptotp-1):
    campcump[j+1] += campcump[j] + campp1[j+1,1]

shnay=46
naytot=len(nay[:,0])
naytotp=len(nayp1[:,0])
naycum = np.zeros(shape=(naytot,1))
naycump = np.zeros(shape=(naytotp,1))
naycum[0] = nay[0,1]
naycump[0] = nayp1[0,1]
for j in range(0,naytot-1):
    naycum[j+1] += naycum[j] + nay[j+1,1]
for j in range(0,naytotp-1):
    naycump[j+1] += naycump[j] + nayp1[j+1,1]

shoax=35
oaxtot=len(oax[:,0])
oaxtotp=len(oaxp1[:,0])
oaxcum = np.zeros(shape=(oaxtot,1))
oaxcump = np.zeros(shape=(oaxtotp,1))
oaxcum[0] = oax[0,1]
oaxcump[0] = oaxp1[0,1]
for j in range(0,oaxtot-1):
    oaxcum[j+1] += oaxcum[j] + oax[j+1,1]
for j in range(0,oaxtotp-1):
    oaxcump[j+1] += oaxcump[j] + oaxp1[j+1,1]


plt.rcParams['axes.linewidth'] = 2.0
plt.rcParams['xtick.major.width'] = 2.0
plt.rcParams['ytick.major.width'] = 2.0
plt.rcParams['xtick.major.size'] = 5
plt.rcParams['ytick.major.size'] = 5
rc('font', **{'family': 'sans-serif', 'serif': ['Computer Modern']})
rc('text', usetex=True)

# Choose a colormap
colormap = cm.viridis
mus = [1,2,3,4,5,6,7]
colorparams = mus
normalize = mcolors.Normalize(vmin=np.min(colorparams), vmax=np.max(colorparams))

colormap2 = cm.tab20b
mus2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
colorparams2 = mus2
normalize2 = mcolors.Normalize(vmin=np.min(colorparams2), vmax=np.max(colorparams2))

yl = [r'$0.25$',r'$0.5$',r'$1$']
yn=[0.25,0.5,1]

color = 'tab:red'
x=[0,200,400]

fig, ((ax1,ax2,ax3),(ax4,ax5,ax6),(ax7,ax8,ax9),(ax10,ax11,ax12),(ax13,ax14,ax15),(ax16,ax17,ax18)) = plt.subplots(nrows=6, ncols=3, sharex=False, sharey=False, figsize=(18, 18))
fig.text(0.505, 0.01, r'$\mathrm{days}$', ha='center',fontsize=(20))
plt.subplots_adjust(left=0.1, right=0.95,top=0.95, bottom=0.13)
#

ax1.bar(cdmxp1[:,0]+shcdmx,cdmxp1[:,1],color = colormap(normalize(1)),label=r'$\bar{i}_s,\; \mathrm{CDMX}$', width=0.9)
ax1.bar(cdmx[:,0],cdmx[:,1],color = colormap(normalize(4)),label=r'$i_e,\; \mathrm{CDMX}$', width=0.7)
ax1.legend(borderpad=0.25, shadow = True, loc='upper left', ncol=1,fontsize=(10))
ax1.tick_params(labelsize='12',labeltop=False, labelright=False, labelbottom=False)
ax1.set_ylim(top = max(cdmxp1[:,1]) + max(cdmxp1[:,1])/10 , bottom = 0)
ax1.set_xlim(right = 570 , left = 0)
ax1.set_xticks(x)
ax1.set_yticklabels([r'$0$',r'$4K$',r'$8K$'])
ax1.set_yticks([0,4000,8000])
ax1.grid(True)

ax2.bar(jalp1[:,0]+shjal,jalp1[:,1],color = colormap(normalize(1)),label=r'$\bar{i}_s,\; \mathrm{Jal}$', width=0.9)
ax2.bar(jal[:,0],jal[:,1],color = colormap(normalize(4)),label=r'$i_e,\; \mathrm{Jal}$', width=0.7)
ax2.tick_params(labelsize='12',labeltop=False, labelright=False, labelbottom=False)
ax2.legend(borderpad=0.25, shadow = True, loc='upper left', ncol=2,fontsize=(10))
ax2.set_ylim(top = max(jalp1[:,1]) + max(jalp1[:,1])/10 , bottom = 0)
ax2.set_xlim(right = 570 , left = 0)
ax2.set_xticks(x)
ax2.set_yticklabels([r'$0$',r'$5C$',r'$1K$',r'$1.5K$'])
ax2.set_yticks([0,500,1000,1500])
ax2.grid(True)

ax3.bar(nlp1[:,0]+shnl,nlp1[:,1],color = colormap(normalize(1)),label=r'$\bar{i}_e,\; \mathrm{NL}$', width=0.9)
ax3.bar(nl[:,0],nl[:,1],color = colormap(normalize(4)),label=r'$i_e,\; \mathrm{NL}$', width=0.7)
ax3.tick_params(labelsize='12',labeltop=False, labelright=False, labelbottom=False)
ax3.legend(borderpad=0.25, shadow = True, loc='upper left', ncol=2,fontsize=(10))
ax3.set_ylim(top = max(nlp1[:,1]) + max(nlp1[:,1])/10 , bottom = 0)
ax3.set_xlim(right = 570 , left = 0)
ax3.set_xticks(x)
ax3.set_yticklabels([r'$0$',r'$5C$',r'$1K$',r'$1.5K$'])
ax3.set_yticks([0,500,1000, 1500])
ax3.grid(True)

#####################

ax4.fill_between(cdmxp3[:,0]+shcdmx, cdmxp3[:,1],cdmxp3[:,2],color='gainsboro')
ax4.plot(cdmxp1[:,0]+shcdmx, cdmxcump[:,0],color = colormap(normalize(1)),label=r'$\bar{c}_s,\; \mathrm{CDMX}$', linewidth=1.5)
ax4.plot(cdmx[:,0],cdmxcum[:,0],color =colormap(normalize(4)),label=r'$c_e,\; \mathrm{CDMX}$', linewidth=1.5)
ax4.tick_params(labelsize='12',labeltop=False, labelright=False, labelbottom=False)
ax4.set_xlim(right = 570 , left = 0)
ax4.set_xticks(x)
ax4.set_ylim(top = 1100000, bottom = 0)
ax4.set_yticklabels([r'$0$',r'$500K$',r'$1M$'])
ax4.set_yticks([0,500000,1000000,])
ax4.grid(False)
ax4w = ax4.twinx()
color = 'tab:red'
ax4w.plot(cdmxp2[:,0]+shcdmx,cdmxp2[:,1],color = 'r', linewidth=0.5)
ax4w.tick_params(axis='y', labelcolor=color)
ax4w.tick_params(labelsize='12',labeltop=False, labelright=False, labelbottom=False)
ax4w.plot(0,0,color = colormap(normalize(1)),label=r'$\bar{c}_s,\; \mathrm{CDMX}$', linewidth=1.5)
ax4w.plot(0,0,color =colormap(normalize(4)),label=r'$c_e,\; \mathrm{CDMX}$', linewidth=1.5)
ax4w.legend(borderpad=0.25, shadow = True, loc='upper left', ncol=2,fontsize=(10))
ax4w.set_yticklabels([r'$0$',r'$0.5$',r'$1$'])
ax4w.set_yticks([0,0.5,1])
ax4w.grid(True)

#
ax5.fill_between(jalp3[:,0]+shjal, jalp3[:,1],jalp3[:,2],color='gainsboro', alpha=1)
ax5.plot(jalp1[:,0]+shjal,jalcump[:,0],color = colormap(normalize(1)),label=r'$\bar{c}_s,\; \mathrm{Jal}$', linewidth=1.5)
ax5.plot(jal[:,0],jalcum[:,0],color =colormap(normalize(4)),label=r'$c_e,\; \mathrm{Jal}$', linewidth=1.5)
ax5.tick_params(labelsize='12',labeltop=False, labelright=False, labelbottom=False)
ax5.set_xlim(right = 570 , left = 0)
ax5.set_xticks(x)
ax5.set_ylim(top = 160000, bottom = 0)
ax5.set_yticklabels([r'$0$',r'$50K$',r'$100K$'])
ax5.set_yticks([0,50000,100000])
ax5.grid(False)
ax5w = ax5.twinx()
color = 'tab:red'
ax5w.plot(jalp2[:,0]+shjal,jalp2[:,1],color = 'r', linewidth=0.5)
ax5w.tick_params(axis='y', labelcolor=color)
ax5w.tick_params(labelsize='12',labeltop=False, labelright=False, labelbottom=False)
ax5w.plot(0,0,color = colormap(normalize(1)),label=r'$\bar{c}_s,\; \mathrm{Jal}$', linewidth=1.5)
ax5w.plot(0,0,color =colormap(normalize(4)),label=r'$c_e,\; \mathrm{Jal}$', linewidth=1.5)
ax5w.legend(borderpad=0.25, shadow = True, loc='upper left', ncol=2,fontsize=(10))
ax5w.set_yticklabels([r'$0$',r'$0.5$',r'$1$'])
ax5w.set_yticks([0,0.5,1])
ax5w.grid(True)

#
ax6.fill_between(nlp3[:,0]+shnl, nlp3[:,1],nlp3[:,2],color='gainsboro')
ax6.plot(nlp1[:,0]+shnl,nlcump[:,0],color = colormap(normalize(1)),label=r'$\bar{c}_s,\; \mathrm{NL}$', linewidth=1.5)
ax6.plot(nl[:,0],nlcum[:,0],color =colormap(normalize(4)),label=r'$c_e,\; \mathrm{NL}$', linewidth=1.5)
ax6.tick_params(labelsize='12',labeltop=False, labelright=False, labelbottom=False)
ax6.set_xlim(right = 570 , left = 0)
ax6.set_xticks(x)
ax6.set_ylim(top = 210000, bottom = 0)
ax6.set_yticklabels([r'$0$',r'$75K$',r'$150K$'])
ax6.set_yticks([0,75000,150000])
ax6.grid(False)
ax6w = ax6.twinx()
ax6w.plot(nlp2[:,0]+shnl,nlp2[:,1],color = 'r', linewidth=0.5)
ax6w.tick_params(axis='y', labelcolor=color)
ax6w.tick_params(labelsize='12',labeltop=False, labelright=True, labelbottom=False)
ax6w.plot(0,0,color = colormap(normalize(1)),label=r'$\bar{c}_s,\; \mathrm{NL}$', linewidth=1.5)
ax6w.plot(0,0,color =colormap(normalize(4)),label=r'$c_e,\; \mathrm{NL}$', linewidth=1.5)
ax6w.legend(borderpad=0.25, shadow = True, loc='upper left', ncol=2,fontsize=(10))
ax6w.set_yticklabels([r'$0$',r'$0.5$',r'$1$'])
ax6w.set_yticks([0,0.5,1])
ax6w.grid(True)

############################################################################
#
ax7.bar(edmxp1[:,0]+shedmx,edmxp1[:,1],color = colormap(normalize(1)),label=r'$\bar{i}_s,\; \mathrm{EDMX}$', width=0.9)
ax7.bar(edmx[:,0],edmx[:,1],color = colormap(normalize(4)),label=r'$i_e,\; \mathrm{EDMX}$', width=0.7)
ax7.legend(borderpad=0.25, shadow = True, loc='upper left', ncol=1,fontsize=(10))
ax7.tick_params(labelsize='12',labeltop=False, labelright=False, labelbottom=False)
ax7.set_ylim(top = max(edmxp1[:,1]) + max(edmxp1[:,1])/10 , bottom = 0)
ax7.set_xlim(right = 570 , left = 0)
ax7.set_xticks(x)
ax7.set_yticklabels([r'$0$',r'$1K$',r'$2K$'])
ax7.set_yticks([0,1000,2000])
ax7.grid(True)
#
ax8.bar(michp1[:,0]+shmich,michp1[:,1],color = colormap(normalize(1)),label=r'$\bar{i}_s,\; \mathrm{Mich}$', width=0.9)
ax8.bar(mich[:,0],mich[:,1],color = colormap(normalize(4)),label=r'$i_e,\; \mathrm{Mich}$', width=0.7)
ax8.tick_params(labelsize='12',labeltop=False, labelright=False, labelbottom=False)
ax8.legend(borderpad=0.25, shadow = True, loc='upper left', ncol=2,fontsize=(10))
ax8.set_ylim(top = max(michp1[:,1]) + max(michp1[:,1])/10 , bottom = 0)
ax8.set_xlim(right = 570 , left = 0)
ax8.set_xticks(x)
ax8.set_yticklabels([r'$0$',r'$3C$',r'$6C$'])
ax8.set_yticks([0,300,600])
ax8.grid(True)

#
ax9.bar(chisp1[:,0]+shchis,chisp1[:,1],color = colormap(normalize(1)),label=r'$\bar{i}_s,\; \mathrm{Chis}$', width=0.9)
ax9.bar(chis[:,0],chis[:,1],color = colormap(normalize(4)),label=r'$i_e,\; \mathrm{Chis}$', width=0.7)
ax9.tick_params(labelsize='12',labeltop=False, labelright=False, labelbottom=False)
ax9.legend(borderpad=0.25, shadow = True, loc='upper left', ncol=2,fontsize=(10))
ax9.set_ylim(top = max(chisp1[:,1]) + max(chisp1[:,1])/5 , bottom = 0)
ax9.set_xlim(right = 570 , left = 0)
ax9.set_xticks(x)
ax9.set_yticklabels([r'$0$',r'$1C$',r'$2C$'])
ax9.set_yticks([0,100,200])
ax9.grid(True)

############################################################################
#
ax10.fill_between(edmxp3[:,0]+shedmx, edmxp3[:,1],edmxp3[:,2],color='gainsboro')
ax10.plot(edmxp1[:,0]+shedmx, edmxcump[:,0],color = colormap(normalize(1)),label=r'$\bar{c}_s,\; \mathrm{Edmx}$', linewidth=1.5)
ax10.plot(edmx[:,0],edmxcum[:,0],color =colormap(normalize(4)),label=r'$c_e,\; \mathrm{Edmx}$', linewidth=1.5)
ax10.tick_params(labelsize='12',labeltop=False, labelright=False, labelbottom=False)
ax10.set_xlim(right = 570 , left = 0)
ax10.set_xticks(x)
ax10.set_ylim(top = 500000, bottom = 0)
ax10.set_yticklabels([r'$0$',r'$250K$',r'$500K$'])
ax10.set_yticks([0,250000,500000])
ax10.grid(False)
ax10w = ax10.twinx()
color = 'tab:red'
ax10w.plot(edmxp2[:,0]+shedmx,edmxp2[:,1],color = 'r', linewidth=0.5)
ax10w.tick_params(axis='y', labelcolor=color)
ax10w.tick_params(labelsize='12',labeltop=False, labelright=False, labelbottom=False)
ax10w.plot(0,0,color = colormap(normalize(1)),label=r'$\bar{c}_s,\; \mathrm{EDMX}$', linewidth=1.5)
ax10w.plot(0,0,color =colormap(normalize(4)),label=r'$c_e,\; \mathrm{EDMX}$', linewidth=1.5)
ax10w.legend(borderpad=0.25, shadow = True, loc='upper left', ncol=2,fontsize=(10))
ax10w.set_yticklabels([r'$0$',r'$0.5$',r'$1$'])
ax10w.set_yticks([0,0.5,1])
ax10w.grid(True)
#
ax11.fill_between(michp3[:,0]+shmich, michp3[:,1],michp3[:,2],color='gainsboro', alpha=1)
ax11.plot(michp1[:,0]+shmich,michcump[:,0],color = colormap(normalize(1)),label=r'$\bar{c}_s,\; \mathrm{mich}$', linewidth=1.5)
ax11.plot(mich[:,0],michcum[:,0],color =colormap(normalize(4)),label=r'$c_e,\; \mathrm{mich}$', linewidth=1.5)
ax11.tick_params(labelsize='12',labeltop=False, labelright=False, labelbottom=False)
ax11.set_xlim(right = 570 , left = 0)
ax11.set_xticks(x)
ax11.set_ylim(top = 100000, bottom = 0)
ax11.set_yticklabels([r'$0$',r'$50K$'])
ax11.set_yticks([0,50000])
ax11.grid(False)
ax11w = ax11.twinx()
color = 'tab:red'
ax11w.plot(michp2[:,0]+shmich,michp2[:,1],color = 'r', linewidth=0.5)
ax11w.tick_params(axis='y', labelcolor=color)
ax11w.tick_params(labelsize='12',labeltop=False, labelright=False, labelbottom=False)
ax11w.plot(0,0,color = colormap(normalize(1)),label=r'$\bar{c}_s,\; \mathrm{Mich}$', linewidth=1.5)
ax11w.plot(0,0,color =colormap(normalize(4)),label=r'$c_e,\; \mathrm{Mich}$', linewidth=1.5)
ax11w.legend(borderpad=0.25, shadow = True, loc='upper left', ncol=2,fontsize=(10))
ax11w.set_yticklabels([r'$0$',r'$0.5$',r'$1$'])
ax11w.set_yticks([0,0.5,1])
ax11w.grid(True)
#
ax12.fill_between(chisp3[:,0]+shchis, chisp3[:,1],chisp3[:,2],color='gainsboro')
ax12.plot(chisp1[:,0]+shchis,chiscump[:,0],color = colormap(normalize(1)),label=r'$\bar{c}_s,\; \mathrm{chis}$', linewidth=1.5)
ax12.plot(chis[:,0],chiscum[:,0],color =colormap(normalize(4)),label=r'$c_e,\; \mathrm{chis}$', linewidth=1.5)
ax12.tick_params(labelsize='12',labeltop=False, labelright=False, labelbottom=False)
ax12.set_xlim(right = 570 , left = 0)
ax12.set_xticks(x)
ax12.set_ylim(top = 25000, bottom = 0)
ax12.set_yticklabels([r'$0$',r'$10K$',r'$20K$'])
ax12.set_yticks([0,10000,20000])
ax12.grid(False)
ax12w = ax12.twinx()
ax12w.plot(chisp2[:,0]+shchis,chisp2[:,1],color = 'r', linewidth=0.5)
ax12w.tick_params(axis='y', labelcolor=color)
ax12w.tick_params(labelsize='12',labeltop=False, labelright=True, labelbottom=False)
ax12w.plot(0,0,color = colormap(normalize(1)),label=r'$\bar{c}_s,\; \mathrm{Chis}$', linewidth=1.5)
ax12w.plot(0,0,color =colormap(normalize(4)),label=r'$c_e,\; \mathrm{Chis}$', linewidth=1.5)
ax12w.legend(borderpad=0.25, shadow = True, loc='upper left', ncol=2,fontsize=(10))
ax12w.set_yticklabels([r'$0$',r'$0.5$',r'$1$'])
ax12w.set_yticks([0,0.5,1])
ax12w.grid(True)

############################################################################
#
ax13.bar(campp1[:,0]+shcamp,campp1[:,1],color = colormap(normalize(1)),label=r'$\bar{i}_s,\; \mathrm{Camp}$', width=0.9)
ax13.bar(camp[:,0],camp[:,1],color = colormap(normalize(4)),label=r'$i_e,\; \mathrm{Camp}$', width=0.7)
ax13.legend(borderpad=0.25, shadow = True, loc='upper left', ncol=1,fontsize=(10))
ax13.tick_params(labelsize='12',labeltop=False, labelright=False, labelbottom=False)
ax13.set_ylim(top = max(campp1[:,1]) + max(campp1[:,1])/10 , bottom = 0)
ax13.set_xlim(right = 570 , left = 0)
ax13.set_xticks(x)
ax13.set_yticklabels([r'$0$',r'$1C$',r'$2C$'])
ax13.set_yticks([0,100,200])
ax13.set_ylim(top = 250, bottom = 0)
ax13.grid(True)
#
ax14.bar(nayp1[:,0]+shnay,nayp1[:,1],color = colormap(normalize(1)),label=r'$\bar{i}_s,\; \mathrm{Nay}$', width=0.9)
ax14.bar(nay[:,0],nay[:,1],color = colormap(normalize(4)),label=r'$i_e,\; \mathrm{Nay}$', width=0.7)
ax14.legend(borderpad=0.25, shadow = True, loc='upper left', ncol=1,fontsize=(10))
ax14.tick_params(labelsize='12',labeltop=False, labelright=False, labelbottom=False)
ax14.set_ylim(top = max(nayp1[:,1]) + max(nayp1[:,1])/10 , bottom = 0)
ax14.set_xlim(right = 570 , left = 0)
ax14.set_xticks(x)
ax14.set_yticklabels([r'$0$',r'$2C$',r'$4C$'])
ax14.set_yticks([0,200,400])
ax14.set_ylim(top = 600, bottom = 0)
ax14.grid(True)
#
ax15.bar(oaxp1[:,0]+shoax,oaxp1[:,1],color = colormap(normalize(1)),label=r'$\bar{i}_s,\; \mathrm{Oax}$', width=0.9)
ax15.bar(oax[:,0],oax[:,1],color = colormap(normalize(4)),label=r'$i_e,\; \mathrm{Oax}$', width=0.7)
ax15.legend(borderpad=0.25, shadow = True, loc='upper left', ncol=1,fontsize=(10))
ax15.tick_params(labelsize='12',labeltop=False, labelright=False, labelbottom=False)
ax15.set_ylim(top = max(oaxp1[:,1]) + max(oaxp1[:,1])/10 , bottom = 0)
ax15.set_xlim(right = 570 , left = 0)
ax15.set_xticks(x)
ax15.set_yticklabels([r'$0$',r'$2C$',r'$4C$'])
ax15.set_yticks([0,200,400])
ax15.set_ylim(top = 500, bottom = 0)
ax15.grid(True)
###########
#
ax16.fill_between(campp3[:,0]+shcamp, campp3[:,1],campp3[:,2],color='gainsboro')
ax16.plot(campp1[:,0]+shcamp,campcump[:,0],color = colormap(normalize(1)),label=r'$\bar{c}_s,\; \mathrm{camp}$', linewidth=1.5)
ax16.plot(camp[:,0],campcum[:,0],color =colormap(normalize(4)),label=r'$c_e,\; \mathrm{camp}$', linewidth=1.5)
ax16.tick_params(labelsize='12',labeltop=False, labelright=False, labelbottom=True)
ax16.set_xlim(right = 570 , left = 0)
ax16.set_xticks(x)
ax16.set_ylim(top = 20000, bottom = 0)
ax16.set_yticklabels([r'$0$',r'$5K$',r'$10K$'])
ax16.set_yticks([0,5000,10000])
ax16.grid(False)
ax16w = ax16.twinx()
ax16w.plot(campp2[:,0]+shcamp,campp2[:,1],color = 'r', linewidth=0.5)
ax16w.tick_params(axis='y', labelcolor=color)
ax16w.tick_params(labelsize='12',labeltop=False, labelright=False, labelbottom=False)
ax16w.plot(0,0,color = colormap(normalize(1)),label=r'$\bar{c}_s,\; \mathrm{Camp}$', linewidth=1.5)
ax16w.plot(0,0,color =colormap(normalize(4)),label=r'$c_e,\; \mathrm{Camp}$', linewidth=1.5)
ax16w.legend(borderpad=0.25, shadow = True, loc='upper left', ncol=2,fontsize=(10))
ax16w.set_yticklabels([r'$0$',r'$0.5$',r'$1$'])
ax16w.set_yticks([0,0.5,1])
ax16w.grid(True)
#
ax17.fill_between(nayp3[:,0]+shnay, nayp3[:,1],nayp3[:,2],color='gainsboro')
ax17.plot(nayp1[:,0]+shnay,naycump[:,0],color = colormap(normalize(1)),label=r'$\bar{c}_s,\; \mathrm{nay}$', linewidth=1.5)
ax17.plot(nay[:,0],naycum[:,0],color =colormap(normalize(4)),label=r'$c_e,\; \mathrm{nay}$', linewidth=1.5)
ax17.tick_params(labelsize='12',labeltop=False, labelright=False, labelbottom=True)
ax17.set_xlim(right = 570 , left = 0)
ax17.set_xticks(x)
ax17.set_ylim(top = 30000, bottom = 0)
ax17.set_yticklabels([r'$0$',r'$10K$',r'$20K$'])
ax17.set_yticks([0,10000,20000])
ax17.grid(False)
ax17w = ax17.twinx()
ax17w.plot(nayp2[:,0]+shnay,nayp2[:,1],color = 'r', linewidth=0.5)
ax17w.tick_params(axis='y', labelcolor=color)
ax17w.tick_params(labelsize='12',labeltop=False, labelright=False, labelbottom=False)
ax17w.plot(0,0,color = colormap(normalize(1)),label=r'$\bar{c}_s,\; \mathrm{Nay}$', linewidth=1.5)
ax17w.plot(0,0,color =colormap(normalize(4)),label=r'$c_e,\; \mathrm{Nay}$', linewidth=1.5)
ax17w.legend(borderpad=0.25, shadow = True, loc='upper left', ncol=2,fontsize=(10))
ax17w.set_yticklabels([r'$0$',r'$0.5$',r'$1$'])
ax17w.set_yticks([0,0.5,1])
ax17w.grid(True)
#
ax18.fill_between(oaxp3[:,0]+shoax, oaxp3[:,1],oaxp3[:,2],color='gainsboro')
ax18.plot(oaxp1[:,0]+shoax,oaxcump[:,0],color = colormap(normalize(1)),label=r'$\bar{c}_s,\; \mathrm{Oax}$', linewidth=1.5)
ax18.plot(oax[:,0],oaxcum[:,0],color =colormap(normalize(4)),label=r'$c_e,\; \mathrm{Oax}$', linewidth=1.5)
ax18.tick_params(labelsize='12',labeltop=False, labelright=False, labelbottom=True)
ax18.set_xlim(right = 570 , left = 0)
ax18.set_xticks(x)
ax18.set_ylim(top = 80000, bottom = 0)
ax18.set_yticklabels([r'$0$',r'$25K$',r'$50K$'])
ax18.set_yticks([0,25000,50000])
ax18.grid(False)
ax18w = ax18.twinx()
ax18w.plot(oaxp2[:,0]+shoax,oaxp2[:,1],color = 'r', linewidth=0.5)
ax18w.tick_params(axis='y', labelcolor=color)
ax18w.tick_params(labelsize='12',labeltop=False, labelright=True, labelbottom=False)
ax18w.plot(0,0,color = colormap(normalize(1)),label=r'$\bar{c}_s,\; \mathrm{Oax}$', linewidth=1.5)
ax18w.plot(0,0,color =colormap(normalize(4)),label=r'$c_e,\; \mathrm{Oax}$', linewidth=1.5)
ax18w.legend(borderpad=0.25, shadow = True, loc='upper left', ncol=2,fontsize=(10))
ax18w.set_yticklabels([r'$0$',r'$0.5$',r'$1$'])
ax18w.set_yticks([0,0.5,1])
ax18w.grid(True)



plt.tight_layout()
figure_name = 'fig4.eps'	# name of the figure to be saved
plt.savefig(figure_name)

plt.show()
