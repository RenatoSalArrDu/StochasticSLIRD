import numpy as np
import matplotlib.pyplot as plt
import pylab
from numpy.fft import fft
from matplotlib import rc
import matplotlib.colors as mcolors
import matplotlib.cm as cm


wcdmx=np.loadtxt('datas/cdmx/fort.16')
wjal=np.loadtxt('datas/jal/fort.16')
wnl=np.loadtxt('datas/nl/fort.16')

wcamp=np.loadtxt('datas/camp/fort.16')
wnay=np.loadtxt('datas/nay/fort.16')
woax=np.loadtxt('datas/oax/fort.16')

wchis=np.loadtxt('datas/chis/fort.16')
wedmx=np.loadtxt('datas/edmx/fort.16')
wmich=np.loadtxt('datas/mich/fort.16')




#Fourier transform
swcdmx=14
swjal=6
swnl=6 #7
swedmx=16 #17
swmich=5
swchis=9 #10
swcamp=0
swnay=0
swoax=10


rtcdmx=np.zeros(len(wcdmx)-swcdmx,dtype=np.float64) # defino arreglo para Rt
rtcdmx=wcdmx[swcdmx:len(wcdmx)]
Xcdmx = fft(rtcdmx[:,1],norm='ortho')
ocdmx= np.arange(len(Xcdmx)) /len(Xcdmx)

rtjal=np.zeros(len(wjal)-swjal,dtype=np.float64) # defino arreglo para Rt
rtjal=wjal[swjal:len(wjal)]
Xjal = fft(rtjal[:,1],norm='ortho')
ojal= np.arange(len(Xjal)) /len(Xjal)

rtnl=np.zeros(len(wnl)-swnl,dtype=np.float64) # defino arreglo para Rt
rtnl=wnl[swnl:len(wnl)]
Xnl = fft(rtnl[:,1],norm='ortho')
onl= np.arange(len(Xnl)) /len(Xnl)

rtedmx=np.zeros(len(wedmx)-swedmx,dtype=np.float64) # defino arreglo para Rt
rtedmx=wedmx[swedmx:len(wedmx)]
Xedmx = fft(rtedmx[:,1],norm='ortho')
oedmx= np.arange(len(Xedmx)) /len(Xedmx)

rtmich=np.zeros(len(wmich)-swmich,dtype=np.float64) # defino arreglo para Rt
rtmich=wmich[swmich:len(wmich)]
Xmich = fft(rtmich[:,1],norm='ortho')
omich= np.arange(len(Xmich)) /len(Xmich)

rtchis=np.zeros(len(wchis)-swchis,dtype=np.float64) # defino arreglo para Rt
rtchis=wchis[swchis:len(wchis)]
Xchis = fft(rtchis[:,1],norm='ortho')
ochis= np.arange(len(Xchis)) /len(Xchis)

rtcamp=np.zeros(len(wcamp)-swcamp,dtype=np.float64) # defino arreglo para Rt
rtcamp=wcamp[swcamp:len(wcamp)]
Xcamp = fft(rtcamp[:,1],norm='ortho')
ocamp= np.arange(len(Xcamp)) /len(Xcamp)

rtnay=np.zeros(len(wnay)-swnay,dtype=np.float64) # defino arreglo para Rt
rtnay=wnay[swnay:len(wnay)]
Xnay = fft(rtnay[:,1],norm='ortho')
onay= np.arange(len(Xnay)) /len(Xnay)

rtoax=np.zeros(len(woax)-swoax,dtype=np.float64) # defino arreglo para Rt
rtoax=woax[swoax:len(woax)]
Xoax = fft(rtoax[:,1],norm='ortho')
ooax= np.arange(len(Xoax)) /len(Xoax)

# N=len(Xcdmx) # se define el rango de frecuencias
# n=Xcdmx.size # se ordenan los datos de la transofmrada de Fourier con las frecuencias
# omega=np.fft.fftfreq(n)

plt.rcParams['axes.linewidth'] = 2.0
plt.rcParams['xtick.major.width'] = 2.0
plt.rcParams['ytick.major.width'] = 2.0
plt.rcParams['xtick.major.size'] = 5
plt.rcParams['ytick.major.size'] = 5
rc('font', **{'family': 'sans-serif', 'serif': ['Computer Modern']})
rc('text', usetex=True)

# Choose a colormap
colormap = cm.tab10
mus = [1,2,3,4,5,6,7,8,9]
colorparams = mus
normalize = mcolors.Normalize(vmin=np.min(colorparams), vmax=np.max(colorparams))

colormap2 = cm.tab10
mus2 = [1,2,3,4,5,6,7,8]
colorparams2 = mus2
normalize2 = mcolors.Normalize(vmin=np.min(colorparams2), vmax=np.max(colorparams2))


cdmxpx=[0.0038,0.0095,0.02095,0.1428,0.2857,0.4286]
cdmxpy=[0.687,0.7815,0.4595,1.2043,0.8784,0.4038]

# jalpx=[0.0094,0.02251,0.04502,0.14258,0.2852,0.4278]
# jalpy=[1.0923,0.4793,0.2665,1.0631,0.7128,0.2801]

jalpx=[0.0094,0.0168,0.02251,0.04502,0.14258,0.2852,0.4278]
jalpy=[1.0923,0.5025,0.4793,0.2665,1.0631,0.7128,0.2801]

nlpx=[0.00563,0.015,0.02626,0.14258,0.2852,0.4278]
nlpy=[0.7141,0.7297,0.2851,0.9537,0.787,0.3630]

# edmxpx=[0.003828,0.00956,0.02104,0.02486,0.02869,0.1434,0.2848,0.4283]
# edmxpy=[0.6835,0.8793,0.3842,0.3334,0.2154,0.9045,0.6504,0.3674]

edmxpx=[0.003828,0.00956,0.02104,0.1434,0.2848,0.4283]
edmxpy=[0.6835,0.8793,0.3842,0.9045,0.6504,0.3674]

michpx=[0.00936,0.01498,0.02247,0.04495,0.14232,0.2865,0.4288]
michpy=[1.3405,0.7105,0.2941,0.3017,1.0137,0.6739,0.2926]

chispx=[0.0056,0.0094,0.03396,0.1434,0.2849,0.4283]
chispy=[0.9685,1.1866,0.4603,0.9423,0.6225,0.3363]

# camppx=[0.00556,0.01855,0.03154,0.14285,0.2857,0.42857]
# camppy=[1.1699,0.5743,0.5474,1.009,0.75,0.6273]

camppx=[0.00556,0.03154,0.14285,0.2857,0.42857]
camppy=[1.1699,0.5474,1.009,0.75,0.6273]

naypx=[0.00556,0.01113,0.02226,0.14285,0.2857]
naypy=[1.0568,1.336,0.5989,0.9427,0.7341]

oaxpx=[0.00945,0.03403,0.05104,0.14366,0.2854,0.4291]
oaxpy=[1.1885,0.2699,0.2862,0.6717,0.6043,0.4242]



cdmxcb=np.arange(6)
jalcb=np.arange(7)
nlcb=np.arange(6)

edmxcb=np.arange(6)
michcb=np.arange(7)
chiscb=np.arange(6)

campcb=np.arange(5)
oaxcb=np.arange(6)
naycb=np.arange(5)


fig, ((ax1,ax2,ax3),(ax4,ax5,ax6),(ax7,ax8,ax9) ) = plt.subplots(nrows=3, ncols=3, sharex=False, sharey=False, figsize=(18, 18))
fig.text(0.01, 0.51, r'$\mathcal{F}[W(t)]$',  va='center', rotation='vertical', fontsize=(15))
fig.text(0.51, 0.01, r'$f\, [1/\mathrm{days}]$', ha='center',fontsize=(15))
plt.subplots_adjust(left=0.1, right=0.95,top=0.95, bottom=0.13)


################################################################################


####################################  Cdmx
ax1.plot(ocdmx, abs(Xcdmx),color = 'k', linewidth=1.5)#,label=r'$|\hat{W}(f)|$', linewidth=1.5)
ax1.scatter(cdmxpx,cdmxpy, c=cdmxcb, cmap=cm.tab10)
ax1.tick_params(labelsize='15',labeltop=False, labelright=False, labelbottom=False)
ax1.set_ylim(top = 3, bottom = 0)
ax1.set_xlim(left = 0, right = 0.5)
ax1.legend(borderpad=0.2, shadow = True, loc='upper left', ncol=1,fontsize=(10))

cdmxp1 = ax1.scatter(cdmxpx[0],cdmxpy[0], marker='o', color=colormap(normalize(1)))
cdmxp2 = ax1.scatter(cdmxpx[1],cdmxpy[1], marker='o', color=colormap(normalize(2)))
cdmxp3  = ax1.scatter(cdmxpx[2],cdmxpy[2], marker='o', color=colormap(normalize(3)))
cdmxp4  = ax1.scatter(cdmxpx[3],cdmxpy[3], marker='o', color=colormap(normalize(4)))
cdmxp5  = ax1.scatter(cdmxpx[4],cdmxpy[4], marker='o', color=colormap(normalize(5)))
cdmxp6 = ax1.scatter(cdmxpx[5],cdmxpy[5], marker='o', color=colormap(normalize(6)))


ax1.legend((cdmxp1, cdmxp2, cdmxp3, cdmxp4, cdmxp5, cdmxp6),
           (r'$263d$',r'$105d$', r'$48d$', r'$7d$', r'$3.5d$', r'$2.3d$'),
           scatterpoints=1,loc='upper right',ncol=1,fontsize=12)
ax1.grid(True)
ax1.set_axisbelow(True)
ax1.text(0.03, 2.5, "a)",fontsize=(20))


####################################  Jal

ax2.plot(ojal, abs(Xjal),color = 'k', linewidth=1.5)
ax2.scatter(jalpx,jalpy, c=jalcb, cmap=cm.tab10)
ax2.tick_params(labelsize='15',labeltop=False, labelright=False, labelbottom=False, labelleft=False)
ax2.set_ylim(top = 3, bottom = 0)
ax2.set_xlim(left = 0, right = 0.5)
ax2.legend(borderpad=0.2, shadow = True, loc='upper left', ncol=1,fontsize=(10))

jalp1 = ax2.scatter(jalpx[0],jalpy[0], marker='o', color=colormap(normalize(1)))
jalp2 = ax2.scatter(jalpx[1],jalpy[1], marker='o', color=colormap(normalize(2)))
jalp3  = ax2.scatter(jalpx[2],jalpy[2], marker='o', color=colormap(normalize(3)))
jalp4  = ax2.scatter(jalpx[3],jalpy[3], marker='o', color=colormap(normalize(4)))
jalp5  = ax2.scatter(jalpx[4],jalpy[4], marker='o', color=colormap(normalize(5)))
jalp6  = ax2.scatter(jalpx[5],jalpy[5], marker='o', color=colormap(normalize(6)))
jalp7  = ax2.scatter(jalpx[6],jalpy[6], marker='o', color=colormap(normalize(7)))

ax2.legend((jalp1, jalp2, jalp3, jalp4, jalp5, jalp6, jalp7),
           (r'$107d$',r'$60d$',r'$44d$',r'$22d$',r'$7d$', r'$3.5d$', r'$2.3d$'),
           scatterpoints=1,loc='upper right',ncol=1,fontsize=12)
ax2.grid(True)
ax2.set_axisbelow(True)
ax2.text(0.03, 2.5, "b)",fontsize=(20))

####################################  NL
ax3.plot(onl, abs(Xnl),color = 'k', linewidth=1.5)
ax3.scatter(nlpx,nlpy, c=nlcb, cmap=cm.tab10)
ax3.tick_params(labelsize='15',labeltop=False, labelright=False, labelbottom=False, labelleft=False)
ax3.legend(borderpad=0.25, shadow = True, loc='upper left', ncol=1,fontsize=(10))
ax3.set_ylim(top = 3, bottom = 0)
ax3.set_xlim(left = 0, right = 0.5)
ax3.legend(borderpad=0.2, shadow = True, loc='upper left', ncol=1,fontsize=(10))

nlp1 = ax3.scatter(nlpx[0],nlpy[0], marker='o', color=colormap(normalize(1)))
nlp2 = ax3.scatter(nlpx[1],nlpy[1], marker='o', color=colormap(normalize(2)))
nlp3  = ax3.scatter(nlpx[2],nlpy[2], marker='o', color=colormap(normalize(3)))
nlp4  = ax3.scatter(nlpx[3],nlpy[3], marker='o', color=colormap(normalize(4)))
nlp5  = ax3.scatter(nlpx[4],nlpy[4], marker='o', color=colormap(normalize(5)))
nlp6 = ax3.scatter(nlpx[5],nlpy[5], marker='o', color=colormap(normalize(6)))

ax3.legend((nlp1, nlp2, nlp3, nlp4, nlp5, nlp6),
           (r'$178d$',r'$66d$', r'$38d$', r'$7d$',r'$3.5d$',r'$2.3d$'),
           scatterpoints=1,loc='upper right',ncol=1,fontsize=12)
ax3.grid(True)
ax3.set_axisbelow(True)
ax3.text(0.03, 2.5, "c)",fontsize=(20))

# ####################################  Edmx
ax4.plot(oedmx, abs(Xedmx),color = 'k', linewidth=1.5)
ax4.scatter(edmxpx,edmxpy, c=edmxcb, cmap=cm.tab10)
ax4.tick_params(labelsize='15',labeltop=False, labelright=False, labelbottom=False)
ax4.set_ylim(top = 3, bottom = 0)
ax4.set_xlim(left = 0, right = 0.5)
ax4.legend(borderpad=0.2, shadow = True, loc='upper left', ncol=1,fontsize=(10))

edmxp1 = ax4.scatter(edmxpx[0],edmxpy[0], marker='o', color=colormap(normalize(1)))
edmxp2 = ax4.scatter(edmxpx[1],edmxpy[1], marker='o', color=colormap(normalize(2)))
edmxp3  = ax4.scatter(edmxpx[2],edmxpy[2], marker='o', color=colormap(normalize(3)))
edmxp4  = ax4.scatter(edmxpx[3],edmxpy[3], marker='o', color=colormap(normalize(4)))
edmxp5  = ax4.scatter(edmxpx[4],edmxpy[4], marker='o', color=colormap(normalize(5)))
edmxp6 = ax4.scatter(edmxpx[5],edmxpy[5], marker='o', color=colormap(normalize(6)))
# edmxp7 = ax4.scatter(edmxpx[6],edmxpy[6], marker='o', color=colormap(normalize(7)))
# edmxp8 = ax4.scatter(edmxpx[7],edmxpy[7], marker='o', color=colormap(normalize(8)))

# ax4.legend((edmxp1, edmxp2, edmxp3, edmxp4, edmxp5, edmxp6, edmxp7, edmxp8),
#           (r'$261d$',r'$105d$', r'$48d$', r'$40d$', r'$35d$', r'$7d$',r'$3.5d$',r'$2.3d$'),
#           scatterpoints=1,loc='upper right',ncol=2,fontsize=12)

ax4.legend((edmxp1, edmxp2, edmxp3, edmxp4, edmxp5, edmxp6),
          (r'$261d$',r'$105d$', r'$48d$', r'$7d$',r'$3.5d$',r'$2.3d$'),
          scatterpoints=1,loc='upper right',ncol=1,fontsize=12)

ax4.grid(True)
ax4.set_axisbelow(True)
ax4.text(0.03, 2.5, "d)",fontsize=(20))

####################################  mich
ax5.plot(omich, abs(Xmich),color = 'k', linewidth=1.5)
ax5.scatter(michpx,michpy, c=michcb, cmap=cm.tab10)
ax5.tick_params(labelsize='15',labeltop=False, labelright=False, labelbottom=False, labelleft=False)
ax5.set_ylim(top = 3, bottom = 0)
ax5.set_xlim(left = 0, right = 0.5)
ax5.legend(borderpad=0.2, shadow = True, loc='upper left', ncol=1,fontsize=(10))

michp1 = ax5.scatter(michpx[0],michpy[0], marker='o', color=colormap(normalize(1)))
michp2 = ax5.scatter(michpx[1],michpy[1], marker='o', color=colormap(normalize(2)))
michp3  = ax5.scatter(michpx[2],michpy[2], marker='o', color=colormap(normalize(3)))
michp4  = ax5.scatter(michpx[3],michpy[3], marker='o', color=colormap(normalize(4)))
michp5  = ax5.scatter(michpx[4],michpy[4], marker='o', color=colormap(normalize(5)))
michp6 = ax5.scatter(michpx[5],michpy[5], marker='o', color=colormap(normalize(6)))
michp7 = ax5.scatter(michpx[6],michpy[6], marker='o', color=colormap(normalize(7)))

ax5.legend((michp1, michp2, michp3, michp4, michp5, michp6, michp7),
          (r'$107d$', r'$67d$', r'$45d$', r'$22d$', r'$7d$', r'$3.5d$', r'$2.3d$'),
          scatterpoints=1,loc='upper right',ncol=1,fontsize=12)
ax5.grid(True)
ax5.set_axisbelow(True)
ax5.text(0.03, 2.5, "e)",fontsize=(20))

# ####################################  chis
ax6.plot(ochis, abs(Xchis),color = 'k', linewidth=1.5)
ax6.scatter(chispx,chispy, c=chiscb, cmap=cm.tab10)
ax6.tick_params(labelsize='15',labeltop=False, labelright=False, labelbottom=False, labelleft=False)
ax6.set_ylim(top = 3, bottom = 0)
ax6.set_xlim(left = 0, right = 0.5)
ax6.legend(borderpad=0.2, shadow = True, loc='upper left', ncol=1,fontsize=(10))

chisp1 = ax6.scatter(chispx[0],chispy[0], marker='o', color=colormap(normalize(1)))
chisp2 = ax6.scatter(chispx[1],chispy[1], marker='o', color=colormap(normalize(2)))
chisp3  = ax6.scatter(chispx[2],chispy[2], marker='o', color=colormap(normalize(3)))
chisp4  = ax6.scatter(chispx[3],chispy[3], marker='o', color=colormap(normalize(4)))
chisp5  = ax6.scatter(chispx[4],chispy[4], marker='o', color=colormap(normalize(5)))
chisp6 = ax6.scatter(chispx[5],chispy[5], marker='o', color=colormap(normalize(6)))

ax6.legend((chisp1, chisp2, chisp3, chisp4, chisp5, chisp6),
          (r'$179d$', r'$106d$', r'$29d$', r'$7d$', r'$3.5d$', r'$2.3d$'),
          scatterpoints=1,loc='upper right',ncol=1,fontsize=12)
ax6.grid(True)
ax6.set_axisbelow(True)
ax6.text(0.03, 2.5, "f)",fontsize=(20))

####################################  camp
ax7.plot(ocamp, abs(Xcamp),color = 'k', linewidth=1.5)
ax7.scatter(camppx,camppy, c=campcb, cmap=cm.tab10)
ax7.tick_params(labelsize='15',labeltop=False, labelright=False, labelbottom=True)
ax7.set_ylim(top = 3, bottom = 0)
ax7.set_xlim(left = 0, right = 0.5)
ax7.legend(borderpad=0.2, shadow = True, loc='upper left', ncol=1,fontsize=(10))

campp1 = ax7.scatter(camppx[0],camppy[0], marker='o', color=colormap(normalize(1)))
campp2 = ax7.scatter(camppx[1],camppy[1], marker='o', color=colormap(normalize(2)))
campp3  = ax7.scatter(camppx[2],camppy[2], marker='o', color=colormap(normalize(3)))
campp4  = ax7.scatter(camppx[3],camppy[3], marker='o', color=colormap(normalize(4)))
campp5  = ax7.scatter(camppx[4],camppy[4], marker='o', color=colormap(normalize(5)))

ax7.legend((campp1, campp2, campp3, campp4, campp5),
          (r'$180d$',r'$32d$', r'$7d$',r'$3.5d$',r'$2.3d$'),
          scatterpoints=1,loc='upper right',ncol=1,fontsize=12)
ax7.grid(True)
ax7.set_axisbelow(True)
ax7.text(0.03, 2.5, "g)",fontsize=(20))

####################################  nay
ax8.plot(onay, abs(Xnay),color = 'k', linewidth=1.5)
ax8.scatter(naypx,naypy, c=naycb, cmap=cm.tab10)
ax8.tick_params(labelsize='15',labeltop=False, labelright=False, labelbottom=True, labelleft=False)
ax8.set_ylim(top = 3, bottom = 0)
ax8.set_xlim(left = 0, right = 0.5)
ax8.legend(borderpad=0.2, shadow = True, loc='upper left', ncol=1,fontsize=(10))

nayp1 = ax8.scatter(naypx[0],naypy[0], marker='o', color=colormap(normalize(1)))
nayp2 = ax8.scatter(naypx[1],naypy[1], marker='o', color=colormap(normalize(2)))
nayp3  = ax8.scatter(naypx[2],naypy[2], marker='o', color=colormap(normalize(3)))
nayp4  = ax8.scatter(naypx[3],naypy[3], marker='o', color=colormap(normalize(4)))
nayp5  = ax8.scatter(naypx[4],naypy[4], marker='o', color=colormap(normalize(5)))

ax8.legend((nayp1, nayp2, nayp3, nayp4, nayp5),
          (r'$180d$',r'$90d$', r'$45d$', r'$7d$',r'$3.5d$'),
          scatterpoints=1,loc='upper right',ncol=1,fontsize=12)
ax8.grid(True)
ax8.set_axisbelow(True)
ax8.text(0.03, 2.5, "h)",fontsize=(20))

####################################  oax
ax9.plot(ooax, abs(Xoax),color = 'k', linewidth=1.5)
ax9.scatter(oaxpx,oaxpy, c=oaxcb, cmap=cm.tab10)
ax9.tick_params(labelsize='15',labeltop=False, labelright=False, labelbottom=True, labelleft=False)
ax9.set_ylim(top = 3, bottom = 0)
ax9.set_xlim(left = 0, right = 0.5)
ax9.legend(borderpad=0.2, shadow = True, loc='upper left', ncol=1,fontsize=(10))

oaxp1 = ax9.scatter(oaxpx[0],oaxpy[0], marker='o', color=colormap(normalize(1)))
oaxp2 = ax9.scatter(oaxpx[1],oaxpy[1], marker='o', color=colormap(normalize(2)))
oaxp3  = ax9.scatter(oaxpx[2],oaxpy[2], marker='o', color=colormap(normalize(3)))
oaxp4  = ax9.scatter(oaxpx[3],oaxpy[3], marker='o', color=colormap(normalize(4)))
oaxp5  = ax9.scatter(oaxpx[4],oaxpy[4], marker='o', color=colormap(normalize(5)))
oaxp6 = ax9.scatter(oaxpx[5],oaxpy[5], marker='o', color=colormap(normalize(6)))

ax9.legend((oaxp1, oaxp2, oaxp3, oaxp4, oaxp5, oaxp6),
          (r'$106d$',r'$29d$', r'$20d$', r'$7d$',r'$3.5d$',r'$2.3d$'),
          scatterpoints=1,loc='upper right',ncol=1,fontsize=12)
ax9.grid(True)
ax9.set_axisbelow(True)
ax9.text(0.03, 2.5, "i)",fontsize=(20))

plt.show()
