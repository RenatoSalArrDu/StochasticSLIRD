#!//bin/bash
#$ -S /bin/bash

# =============================================================================!
# Mexican states to simulate, (from Feb the 23th 2021)
#camp, cdmx, chis, jal, edmx, mich, nay, nl, oax
state=cdmx #state
date=20_08_21 # final date to simulate day_month_year

# ============= Simulation Parameters =================!
# === see initial condition reference file
ni=33   # initial infectious (this amount is estimated to fit real data)
ns=9999990  # initial susceptible (not necesary unless herd immunity is simulated)
nr=0      # initial recovered
nd=0      # initial dead
icum=117  #initial cumulative of incidence

nltm4=6      # latent at t0 - 4
nltm3=7      # latent at t0 - 3
nltm2=8      # latent at t0 - 2
nltm1=21     # latent at t0 - 1

tshf=26    # initial shift in time to beging cases from Feb the 23th 2021
ntot=540   # number of time units (total number of days)
traj=1000  # number of trajectories

# ======= COVID-19 Parameters ============#
t_r=18      # time of recovery (each t_recov cycles we recover)
t_l=4       # time of latency ( each t_laten cycles we infect)
ro=4        # basic rep. num.
leth=0.1    # fatality


# Additional options for simulations ==========================================!
#==============================================================================!
#----------------- Fluctuations around Ro
rop=0 # rop=0 --> no fluctuations,
      # rop=1 --> uniform distro fluctuations
      # rop=1 --> exp distro fluctuations
      # rop=2 --> poiss distro fluctuations

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

data=Mexico_covid-19_datas
iest=initial_estimation_states
runs=<Imput path to running folder>/StochasticSLIRD/

# ==> Internal definitions  ####################################################
#===============================================================================
#===============================================================================
#===============================================================================


#== switch option for simulation of states or not (there is no point of herd immunity under confinement;
#                                                the pandemia is effectively open in the sense that there
#                                                is an infinite number of susceptibles)
if [ $cop == 4 ]; then
  wop=1  # simulation of real cases
else
  wop=0  # simulation of concenptual behavior
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
ropp='_Ro'
let='_let'
cf='cfun'
hopp='_hop'
tra='ntrj'

if [ $cop == 4 ]; then
 f=$state$tra$traj$i$ni$s$ns$l$nl$r$nr$d$nd$tr$t_r$tl$t_l$ropp$ro$rop$let$leth
else
 f=$tra$traj$cf$cop$i$ni$s$ns$l$nl$r$nr$d$nd$tr$t_r$tl$t_l$ropp$ro$rop$let$leth
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
printf "$ni $ns $nr $nltm4 $nltm3 $nltm2 $nltm1 $nd $t_r $t_l $ntot $ro $hop $leth $cop $traj $tshf $opt $wop $rop" > par.dat
./exe


# python's code to generate a relevant representation of the simulation
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
plt.plot(dat4[:,0]+$tshf,cumsts[:,0]+$icum,color = colormap(normalize(6)),label='cumulative', linewidth=2)
plt.plot(dat5[:,0]+$tshf,dat5[:,1]+$icum,color = colormap(normalize(1)),label='q1', linewidth=2)
plt.plot(dat5[:,0]+$tshf,dat5[:,2]+$icum,color = colormap(normalize(2)),label='q3', linewidth=2)
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
