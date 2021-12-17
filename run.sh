#!//bin/bash
#$ -S /bin/bash

# ============= Epidemiological Parameters =================!
ni=10  # initial infectious (this amount is estimated by adding the number of the new infected in the empirical data, until every day is at least one new infected reported)
ns=9999990  # initial susceptible
nr=0      # initial recovered
nl=0      # initial latent
nd=0      # initial dead

t_r=18      # time of recovery (each t_recov cycles we recover)
t_l=4       # time of latency ( each t_laten cycles we infect)
ro=4        # basic rep. num.
leth=0.1    # fatality

# =============== Simulation Parameters ===================!
ntot=540    # number of time units (total number of days)
traj=10   # number of trajectories


#-----------------   Herd immunity function (only for wop=0)
# i) hop=1:  No herd immunity
# ii) hop=2: Herd immunity based on an inverted logistic function (similar to Fermi function),
#            based on the number of cumulative infected population with parameter dependence:
hop=1

#--------------- Confinement measures function
# i) cop=1    No confinement
# ii) cop=2   Confinement based on a piecewise time dependent function
# iii) cop=3  Confinement based on a Gaussian decaying weight function: c =  exp(-( gamma *  i(t) )**2)
#             with parameter dependence: gamma and io, the latter referencing the
# iv) cop=4    Confinement based on an empirical description of Rt (simuation of real cases)
#
cop=4

#--------------- Confinement measures function
opt=1 #opt 0 write all trajectories, else not

#--------------- Simulations modes
wopt=1 # wopt=0 conceptual features, wopt=1 simulation of real cases based on empirical wt

# ==========================================!
# Mexican states to simulate, (from Feb the 23th 2021)
#camp, cdmx, chis, jal, edmx, mich, nay, nl, oax
state=cdmx #state
date=20_08_21 # final date to simulate day_month_year

data=Mexico_covid-19_datas
iest=initial_estimation_states
runs=<Imput path to running folder>/StochasticSLIRD



# ==> Internal definitions  #############################################################################
#========================================================================================================
#========================================================================================================
#========================================================================================================


#== switch option for simulation of states or not (there is no point of herd immunity under confinement;
#                                                the pandemia is effectively open in the sense that there
#                                                is an infinite number of susceptibles)
if [ $cop == 4 ]; then
  wop=1  # simulation of real cases
else
  wop=0  # simulation of concenptual behavior
fi


#== initial shift in time to beging all cases from Feb the 23th 2021 (fixed parameter seen from the data files ****)
if [ $state == 'camp' ]; then
  tshf=48
elif [ $state == 'cdmx' ]; then
  tshf=18
elif [ $state == 'chis' ]; then
  tshf=39
elif [ $state == 'edmx' ]; then
  tshf=20
elif [ $state == 'jal' ]; then
  tshf=25
elif [ $state == 'mich' ]; then
  tshf=35
elif [ $state == 'nay' ]; then
  tshf=46
elif [ $state == 'oax' ]; then
  tshf=35
fi

#========================================================================================================
#========================================================================================================
# ========================================== write locations to run code
i='_i'
s='_s'
l='_l'
r='_r'
d='_d'
tr='_tr'
tl='_tl'
rop='_Ro'
let='_let'
cf='cfun'
hopp='_hop'
tra='ntrj'

if [ $cop == 4 ]; then
 f=$state$tra$traj$i$ni$s$ns$l$nl$r$nr$d$nd$tr$t_r$tl$t_l$rop$ro$let$leth
else
 f=$tra$traj$cf$cop$i$ni$s$ns$l$nl$r$nr$d$nd$tr$t_r$tl$t_l$rop$ro$let$leth
fi

code=$runs/code
rundirh=$runs/$f
mkdir -p $rundirh
cd $code
./comp.sh

cp $code/exe $rundirh
cp $data/datas$date/$state.dat $rundirh/state.dat
cp $iest/$date/$state.dat $rundirh/wpar.dat
cd $rundirh
printf "$ni $ns $nr $nl $nd $t_r $t_l $ntot $ro $hop $leth $cop $traj $tshf $opt $wop" > par.dat
./exe


# python's code to generate relevant figures of the simulation
printf "import numpy as np
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
dato=np.loadtxt('$runs/code/$data/datas$date/$state.dat')
ntotst=len(dato[:,0])
cumst = np.zeros(shape=(ntotst,1))
cumst[0] = dato[0,1]

for j in range(0,ntotst-1):
    cumst[j+1] += cumst[j] + dato[j+1,1]

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
fig.text(0.5, 0.95, '$opp$sigma', ha='center',fontsize=(20))
plt.subplots_adjust(left=0.1, right=0.95,top=0.95, bottom=0.13)


plt.subplot(221)
plt.plot(dat4[:,0]+$tshf,cumsts[:,0],color = colormap(normalize(6)),label='cumulative', linewidth=2)
plt.plot(dat5[:,0]+$tshf,dat5[:,1],color = colormap(normalize(1)),label='q1', linewidth=2)
plt.plot(dat5[:,0]+$tshf,dat5[:,2],color = colormap(normalize(2)),label='q3', linewidth=2)
plt.plot(dato[:,0],cumst[:,0],color = 'k',label='cumultive data', linewidth=2)
plt.tick_params(labelsize='30',labeltop=False, labelright=False, labelbottom=False)
plt.legend(borderpad=0.1, shadow = True, loc='upper left', ncol=1,fontsize=(10))
plt.xlim(left=0, right=$ntot + $tshf)
plt.grid(True)


plt.subplot(222)
plt.bar(dat4[:,0]+$tshf,dat4[:,1],color = colormap(normalize(2)),label='daily cases', width=0.9)
plt.bar(dato[:,0],dato[:,1],color = colormap(normalize(3)),label='$state', width=0.7)
plt.ylim(top = max(dato[:,1]) + max(dato[:,1])/10 , bottom = 0)
plt.tick_params(labelsize='30',labeltop=False, labelright=False, labelbottom=False)
plt.legend(borderpad=0.1, shadow = True, loc='upper left', ncol=1,fontsize=(15))
plt.xlim(left=0, right=$ntot + $tshf)
plt.grid(True)


plt.subplot(223)
plt.plot(dat3[:,0]+$tshf,dat3[:,1],color = colormap(normalize(3)),label='W(t)', linewidth=2)
plt.plot(dat3[:,0],dat3[:,1],color = colormap(normalize(6)), linewidth=2)
plt.tick_params(labelsize='30',labeltop=False, labelright=False, labelbottom=True)
plt.legend(borderpad=0.1, shadow = True, loc='best', ncol=1,fontsize=(15))
plt.xlim(left=0, right=$ntot + $tshf)
plt.grid(True)



plt.subplot(224)
plt.plot(dat3[:,0]+$tshf,dat3[:,1],color = colormap(normalize(3)),label='W(t)', linewidth=2)
plt.plot(dat3[:,0],dat3[:,1],color = colormap(normalize(6)), linewidth=2)
plt.tick_params(labelsize='30',labeltop=False, labelright=False, labelbottom=True)
plt.legend(borderpad=0.1, shadow = True, loc='best', ncol=1,fontsize=(15))
plt.xlim(left=0, right=$ntot + $tshf)
plt.grid(True)


plt.tight_layout()
figure_name = 'fig$state.eps'	# name of the figure to be saved
plt.savefig(figure_name)

plt.show()
"> fig.py

python fig.py &



cd $runs
