import numpy as np
import matplotlib.pyplot as plt
import pylab
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



cdmxp1=np.loadtxt('datas/cdmx/fort.15') # av incidence cumm max and min
cdmxp2=np.loadtxt('datas/cdmx/fort.16') # R(t)
cdmxp3=np.loadtxt('datas/cdmx/fort.105') #quartils

jalp1=np.loadtxt('datas/jal/fort.15')
jalp2=np.loadtxt('datas/jal/fort.16')
jalp3=np.loadtxt('datas/jal/fort.105')

nlp1=np.loadtxt('datas/nl/fort.15')
nlp2=np.loadtxt('datas/nl/fort.16')
nlp3=np.loadtxt('datas/nl/fort.105')

edmxp1=np.loadtxt('datas/edmx/fort.15') # av incidence cumm max and min
edmxp2=np.loadtxt('datas/edmx/fort.16') # R(t)
edmxp3=np.loadtxt('datas/edmx/fort.105') #quartils

michp1=np.loadtxt('datas/mich/fort.15')
michp2=np.loadtxt('datas/mich/fort.16')
michp3=np.loadtxt('datas/mich/fort.105')

chisp1=np.loadtxt('datas/chis/fort.15')
chisp2=np.loadtxt('datas/chis/fort.16')
chisp3=np.loadtxt('datas/chis/fort.105')


campp1=np.loadtxt('datas/camp/fort.15') # av incidence cumm max and min
campp2=np.loadtxt('datas/camp/fort.16') # R(t)
campp3=np.loadtxt('datas/camp/fort.105') #quartils

nayp1=np.loadtxt('datas/nay/fort.15')
nayp2=np.loadtxt('datas/nay/fort.16')
nayp3=np.loadtxt('datas/nay/fort.105')

oaxp1=np.loadtxt('datas/oax/fort.15')
oaxp2=np.loadtxt('datas/oax/fort.16')
oaxp3=np.loadtxt('datas/oax/fort.105')



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


shcamp=48-4
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

shnay=46-4
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

shoax=35-6
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


#Fourier transform shift
swcdmx=14
swjal=6
swnl=6 #7
swedmx=16 #17
swmich=5
swchis=9 #10
swcamp=0
swnay=0
swoax=10


plt.rcParams['axes.linewidth'] = 2.0
plt.rcParams['xtick.major.width'] = 2.0
plt.rcParams['ytick.major.width'] = 2.0
plt.rcParams['xtick.major.size'] = 5
plt.rcParams['ytick.major.size'] = 5
rc('font', **{'family': 'sans-serif', 'serif': ['Computer Modern']})
rc('text', usetex=True)

# Choose a colormap
colormap2 = cm.cividis
mus2 = [1,2,3,4,5,6,7,8,9,10]
colorparams2 = mus2
normalize2 = mcolors.Normalize(vmin=np.min(colorparams2), vmax=np.max(colorparams2))

colormap = cm.viridis
mus = [1,2,3,4]
colorparams = mus
normalize = mcolors.Normalize(vmin=np.min(colorparams), vmax=np.max(colorparams))

colormap3 = cm.tab10
mus3 = [1,2,3,4,5,6,7,8,9,10]
colorparams3 = mus3
normalize3 = mcolors.Normalize(vmin=np.min(colorparams3), vmax=np.max(colorparams3))

x=[0,200,400]

fig, ((ax1,ax2,ax3),(ax4,ax5,ax6),(ax7,ax8,ax9)) = plt.subplots(nrows=3, ncols=3, sharex=False, sharey=False, figsize=(18, 18))
fig.text(0.505, 0.01, r'$\mathrm{days}$', ha='center',fontsize=(20))
fig.text(0.01, 0.65, r'$\mathrm{individuals}$', va='center', rotation='vertical',fontsize=(20))
plt.subplots_adjust(left=0.1, right=0.95,top=0.95, bottom=0.13)
#


ax1.bar(campp1[:,0]+shcamp,campp1[:,1],color = colormap2(normalize2(1)),label=r'$\bar{i}_s,\; \mathrm{Camp}$', width=1)
ax1.bar(camp[:,0],camp[:,1],color = colormap3(normalize3(10)),label=r'$i_e,\; \mathrm{Camp}$', width=0.6)
ax1.legend(borderpad=0.25, shadow = True, loc='upper left', ncol=1,fontsize=(12))
ax1.tick_params(labelsize='12',labeltop=False, labelright=False, labelbottom=False)
ax1.set_ylim(top = max(campp1[:,1]) + max(campp1[:,1])/10 , bottom = 0)
ax1.set_xlim(right = 570 , left = 0)
ax1.set_xticks(x)
ax1.set_yticklabels([r'$0$',r'$1C$',r'$2C$'])
ax1.set_yticks([0,100,200])
ax1.grid(True)
#

ax2.bar(nayp1[:,0]+shnay,nayp1[:,1],color = colormap2(normalize2(1)),label=r'$\bar{i}_s,\; \mathrm{Nay}$', width=1)
ax2.bar(nay[:,0],nay[:,1],color = colormap3(normalize3(10)),label=r'$i_e,\; \mathrm{Nay}$', width=0.6)
ax2.tick_params(labelsize='12',labeltop=False, labelright=False, labelbottom=False)
ax2.legend(borderpad=0.25, shadow = True, loc='upper left', ncol=1,fontsize=(12))
ax2.set_ylim(top = max(nayp1[:,1]) + max(nayp1[:,1])/10 , bottom = 0)
ax2.set_xlim(right = 570 , left = 0)
ax2.set_xticks(x)
ax2.set_yticklabels([r'$0$',r'$2C$',r'$4C$'])
ax2.set_yticks([0,200,400])
ax2.grid(True)


ax3.bar(oaxp1[:,0]+shoax,oaxp1[:,1],color = colormap2(normalize2(1)),label=r'$\bar{i}_s,\; \mathrm{Oax}$', width=1)
ax3.bar(oax[:,0],oax[:,1],color = colormap3(normalize3(10)),label=r'$i_e,\; \mathrm{Oax}$', width=0.6)
ax3.tick_params(labelsize='12',labeltop=False, labelright=False, labelbottom=False)
ax3.legend(borderpad=0.25, shadow = True, loc='upper left', ncol=1,fontsize=(12))
ax3.set_ylim(top = max(oaxp1[:,1]) + max(oaxp1[:,1])/10 , bottom = 0)
ax3.set_xlim(right = 570 , left = 0)
ax3.set_xticks(x)
ax3.set_yticklabels([r'$0$',r'$2C$',r'$4C$'])
ax3.set_yticks([0,200,400])
ax3.grid(True)



############################################################################

ax4.fill_between(campp3[:,0]+shcamp, campp3[:,1],campp3[:,2],color='gainsboro')
ax4.plot(campp1[:,0]+shcamp,campcump[:,0],color = colormap2(normalize2(1)),label=r'$\bar{c}_s,\; \mathrm{Camp}$', linewidth=1.5)
ax4.plot(camp[:,0],campcum[:,0],color =colormap3(normalize3(10)),label=r'$c_e,\; \mathrm{Camp}$', linewidth=1.5)
ax4.tick_params(labelsize='12',labeltop=False, labelright=False, labelbottom=False)
ax4.set_xlim(right = 570 , left = 0)
ax4.set_xticks(x)
ax4.set_ylim(top = 20000, bottom = 0)
ax4.set_yticklabels([r'$0$',r'$5K$',r'$10K$'])
ax4.set_yticks([0,5000,10000])
ax4.legend(borderpad=0.25, shadow = True, loc='upper left', ncol=1,fontsize=(12))
ax4.grid(True)

#
ax5.fill_between(nayp3[:,0]+shnay, nayp3[:,1],nayp3[:,2],color='gainsboro', alpha=1)
ax5.plot(nayp1[:,0]+shnay,naycump[:,0],color = colormap2(normalize2(1)),label=r'$\bar{c}_s,\; \mathrm{Nay}$', linewidth=1.5)
ax5.plot(nay[:,0],naycum[:,0],color =colormap3(normalize3(10)),label=r'$c_e,\; \mathrm{Nay}$', linewidth=1.5)
ax5.tick_params(labelsize='12',labeltop=False, labelright=False, labelbottom=False)
ax5.set_xlim(right = 570 , left = 0)
ax5.set_xticks(x)
ax5.set_ylim(top = 30000, bottom = 0)
ax5.set_yticklabels([r'$0$',r'$10K$',r'$20K$'])
ax5.set_yticks([0,10000,20000])
ax5.legend(borderpad=0.25, shadow = True, loc='upper left', ncol=1,fontsize=(12))
ax5.grid(True)

#
ax6.fill_between(oaxp3[:,0]+shoax, oaxp3[:,1],oaxp3[:,2],color='gainsboro')
ax6.plot(oaxp1[:,0]+shoax,oaxcump[:,0],color = colormap2(normalize2(1)),label=r'$\bar{c}_s,\; \mathrm{Oax}$', linewidth=1.5)
ax6.plot(oax[:,0],oaxcum[:,0],color =colormap3(normalize3(10)),label=r'$c_e,\; \mathrm{Oax}$', linewidth=1.5)
ax6.tick_params(labelsize='12',labeltop=False, labelright=False, labelbottom=False)
ax6.set_xlim(right = 570 , left = 0)
ax6.set_xticks(x)
ax6.set_ylim(top = 80000, bottom = 0)
ax6.set_yticklabels([r'$0$',r'$25K$',r'$50K$'])
ax6.set_yticks([0,25000,50000])
ax6.legend(borderpad=0.25, shadow = True, loc='upper left', ncol=1,fontsize=(12))
ax6.grid(True)



############################################################################


ax7.plot(campp2[:,0]+shcamp,campp2[:,1],color = 'r', label=r'$W(t),\; \mathrm{Camp}$',linewidth=0.8)
ax7.tick_params(labelsize='12',labeltop=False, labelright=False, labelbottom=True)
ax7.legend(borderpad=0.25, shadow = True, loc='upper right', ncol=1,fontsize=(12))
ax7.set_yticklabels([r'$0$',r'$0.5$',r'$1$'])
ax7.set_ylim(bottom = 0 , top = 1.5)
ax7.set_yticks([0,0.5,1])
ax7.set_xlim(right = 570 , left = 0)
ax7.set_xticks(x)
ax7.grid(True)


#
ax8.plot(nayp2[:,0]+shnay,nayp2[:,1],color = 'r', label=r'$W(t),\; \mathrm{Nay}$', linewidth=0.8)
ax8.tick_params(labelsize='12',labeltop=False, labelright=False, labelbottom=True)
ax8.legend(borderpad=0.25, shadow = True, loc='upper right', ncol=1,fontsize=(12))
ax8.set_yticklabels([r'$0$',r'$0.5$',r'$1$'])
ax8.set_ylim(bottom = 0 , top = 1.5)
ax8.set_yticks([0,0.5,1])
ax8.set_xlim(right = 570 , left = 0)
ax8.set_xticks(x)
ax8.grid(True)



#####################
#
ax9.plot(oaxp2[:,0]+shoax,oaxp2[:,1],color = 'r', label=r'$W(t),\; \mathrm{Oax}$', linewidth=0.8)
ax9.axvspan(0,shoax + swoax,color='gainsboro')
ax9.tick_params(labelsize='12',labeltop=False, labelright=False, labelbottom=True)
ax9.legend(borderpad=0.25, shadow = True, loc='upper right', ncol=1,fontsize=(12))
ax9.set_yticklabels([r'$0$',r'$0.5$',r'$1$'])
ax9.set_ylim(bottom = 0 , top = 1.5)
ax9.set_yticks([0,0.5,1])
ax9.set_xlim(right = 570 , left = 0)
ax9.set_xticks(x)
ax9.grid(True)
left, bottom, width, height = [0.765, 0.21, 0.1, 0.13]
ax9s = fig.add_axes([left, bottom, width, height])
ax9s.plot(oaxp2[:,0]+shoax,oaxp2[:,1],color = 'r', label=r'$W(t),\; \mathrm{Oax}$', linewidth=0.8)
ax9s.set_xlim(right = shoax + swoax+1 , left = shoax-1)
ax9s.set_xticks([shoax,shoax + swoax])
ax9s.axvspan(0,shoax + swoax,color='gainsboro')
ax9s.tick_params(labelsize='12',labeltop=False, labelright=False, labelbottom=True)
ax9s.grid(True)

plt.tight_layout()
figure_name = 'fig4c.png'	# name of the figure to be saved
plt.savefig(figure_name)

plt.show()
