ni=12 #3 #7      # initial infected
ns=9999988 #3   # initial susceptible
nr=0      # initial recovered
nl=0      # initial latent
nd=0      # initial dead
t_r=18    # time of recovery (each t_recov cycles we recover)
t_l=4    # time of latency ( each t_laten cycles we infect)
ntot=540 #480 #402 #405    # number of time units (total number of days)
ro=4      # basic rep. num.
leth=0.1   # fatality
traj=5000 #5000   #nunber of trajectories

#measles  disease: $R_o=18$, $t_R=22$, $t_L=12$
#covid-19  disease: $R_o=4$, $t_R=18$, $t_L=4$

# ==========================================!
#state to compare to, untill Feb the 23th 2021
#reference
#ags, bc, bcs, camp, cdmx, chih, chis, coah, coli,dur, gto, guerr, hid, jal
#mex, mich, morel, nacional, nay, nl, oax, pueb, qroo, quer, slp, son, tab,
#tam, tlxc, ver, yuc, zac
state=chis
date=20_08_21 #23_02_21

# ======================================!
#time shift for left begining
#cdmx=18, jal=25, nl=**
tshf=39


#-----------------   Herd immunity function
# i) wop=1:
# No herd immunity

# ii) wop=2: Covid herd immunity
# Herd immunity based on an inverted logistic function (similar to Fermi function),
# based on the number of cumulative infected population with parameter dependence:
wop=2
alpho=0.22  # parameter of weight function
iop=0.0    # infected number treshold when confinement begins (local)
hp=0.01   # probability reduction to achieve stationarity in the long time limit



#--------------- Confinement measures function ---------------------------------
# i) cop=1
#cop=1
# No confinement

# ii) cop=2
#cop=2
# Confinement based on a piecewise time dependent function

tph3=10 # day of 1st decrement (increment)
tdays=7    # duration of 1st decrement (increment)
wpr2=0.465 # value of the 1st decrement (increment)

tph4=54    # day of 2nd decrement (increment)
tdays2=20   # duration of 2nd decrement (increment)
wpr3=0.25 #0.57 #0.55  # value of the 2nd decrement (increment)

tph5=81    # day of 3rd decrement (increment)
tdays3=3   # duration of 3rd decrement (increment)
wpr4=0.15  # value of the 3rd decrement (increment)

tph6=106  # day of 4th decrement (increment)
tdays4=3   # duration of 4th decrement (increment)
wpr5=0.6 #0.27  # value of the 4th decrement (increment)

tph7=100 #110   # day of 5th decrement (increment)
tdays5=3   # duration of 5th decrement (increment)
wpr6=0.3 #0.42  #0.35  # value of the 5th decrement (increment)

tph8=324    # day of 6th decrement (increment)
tdays6=5  # duration of 6th decrement (increment)
wpr7=0.17   # value of the 6th decrement (increment)

tph9=380    # day of 7th decrement (increment)
tdays7=3   # duration of 7th decrement (increment)
wpr8=0.23 #0.17   # value of the 7th decrement (increment)

tph10=460    # day of 8th decrement (increment)
tdays8=1   # duration of 8th decrement (increment)
wpr9=0.4 #0.43 #0.4   # value of the 8th decrement (increment)

tph11=520 #470    # day of 9th decrement (increment)
tdays9=5   # duration of 9th decrement (increment)
wpr10=0.1 #0.2 #0.23 #0.22  # value of the 9th decrement (increment)

tph12=0 #515 #470    # day of 9th decrement (increment)
tdays10=0 #1   # duration of 9th decrement (increment)
wpr11=0.1 #0.15 #0.22  # value of the 9th decrement (increment)

# iii) cop=3
#cop=3
# Confinement based on Yorch's calculated R(t)
# time retarded for computing Yorch's rt
tre=7

# iv) cop=4
#cop=4
# Confinement based on a Gaussian decaying weight function
# based on the number of infected  population with parameter dependence:
# something like c =  exp(-gamma * i(t)**2)
gamma=50.0
io=0.2

# v) cop=5 #Confinement based on an empirical description of Rt
cop=5

#-------------------------------------------------------------------------------
################################################################################

# ============= Distributions =================!
oprn=1 # opprn=0 random numbers generated from fortran library
      # opprn=1 random numbers generated from python's numpy lib (only here is defined lognormal)

#Type of distribution, some of distributions
#need additional parameters:
#distribitions are suppose to model rate oc congregation of the populaiton
# gamma and beta distribution doesn't seems to work fine
# type of distros ----
# op=1 --- > uniform distro from 0 to 2* rho_o, (this is something else)
# op=2 --- > exp distro with lambda = 1/rho_o (sim to pois)
# op=3 --- > pois distro with lambda = rho_o
# op=4 --- > gamma distro with kappa * theta = rho_o, kappa = rho_o, theta = 1 (sim to pois)
# op=5 --- > gamma distro with kappa * theta = rho_o, kappa = 4, theta = rho_o/4 (puntual)
# op=6 --- > no distribution--- (puntual)
# op=7 --- > lognormal distribution (only if opp=1) mu = ln(ro)-sigma^2/2, two par.distro
op=6
sigma=2.0   #Only for op=7

if [ $op == '7' ]; then
  oprn=1
elif [ $op == '6' ]; then
  oprn=0
fi

opt=1 #opt 0 write all trajectories, else not

# ==========================================!
# ==> Internal definitions (don't move)
i='_i'
s='_s'
l='_l'
r='_r'
d='_d'
tr='_tr'
tl='_tl'
rop='_Ro'
let='_let'
tep='_tep'
iopp='_iop'
alp='_alph'
cf='conf'
ga='_gam'
ioc='io'

if [ $opt == '0' ]; then
n2='alltr_rt_avf_'
else
n2='rt_avf_'
fi

nline='\\n'

if [ $op == '1' ]; then
opp='unif_'
elif [ $op == '2' ]; then
opp='exp_'
elif [ $op == '3' ]; then
opp='poiss_'
elif [ $op == '4' ]; then
opp='gamma1_'
elif [ $op == '5' ]; then
opp='gamma2_'
elif [ $op == '6' ]; then
opp='punctual_'
elif [ $op == '7' ]; then
opp='lognormal_'
fi

wopp='_wop'
dot=3 #dots in plots
mark=
#========================================================================================================
data=/Users/supercarlangas/schamm/epidemiology/Random_SLIRD/covid/proj_mx/covid-19_data
runs=/Users/supercarlangas/schamm/epidemiology/Random_SLIRD/manuscript/figures/fits/newfiguredatas/chis/
code=/Users/supercarlangas/schamm/epidemiology/Random_SLIRD/manuscript/figures/fits/newfiguredatas/chis/code
#========================================================================================================
#=========================================================================================================
if [ $cop == '4' ]; then
f=$n2$traj$cf$cop$ga$gamma$ioc$io$opp$sigma$i$ni$s$ns$l$nl$r$nr$d$nd$tr$t_r$tl$t_l$rop$ro$iopp$iop$wopp$wop$let$leth$alp$alpho
else
f=$n2$traj$cf$cop$opp$sigma$i$ni$s$ns$l$nl$r$nr$d$nd$tr$t_r$tl$t_l$rop$ro$iopp$iop$wopp$wop$let$leth$alp$alpho
fi
rundirh=$runs$f
mkdir -p $rundirh
./comp.sh
cp -r $code/exe $rundirh
cp -r $data/datas$date/$state.dat $rundirh
#cp fdaily.py $rundirh
cd $rundirh
printf "$ni $ns $nr $nl $nd $t_r $t_l $ntot $ro $op $wop $leth $alpho $iop $hp $cop $gamma $io $traj $tshf $tre $oprn $opt" > par.dat

printf "$wpr2 $tdays $tph3
$wpr3 $tdays2 $tph4
$wpr4 $tdays3 $tph5
$wpr5 $tdays4 $tph6
$wpr6 $tdays5 $tph7
$wpr7 $tdays6 $tph8
$wpr8 $tdays7 $tph9
$wpr9 $tdays8 $tph10
$wpr10 $tdays9 $tph11
$wpr11 $tdays10 $tph12
" > wpar.dat

if [ $oprn == '1' ]; then
printf "import numpy as np
#Generate a lot of random numbers from specific distribution according to
#imput options generated by user. These random numbers are the daily mean
#of new infections of each individual in the population at each day of
#propagation
op = $op
ntott = ($ni+$ns+$nr+$nl+$nd)*($t_r - $t_l)
rot= $ro/($t_r - $t_l)
sigma = $sigma

v_ran = np.zeros(ntott,dtype=np.float64)
if  op == 1 :
    v_ran = np.random.uniform(0, 2*rot , size = ntott)
elif  op == 2 :
    v_ran = np.random.exponential(1/rot , size = ntott)
elif op == 3 :
    v_ran = np.random.poisson(rot , size = ntott)
elif op == 4 :
    v_ran = np.random.gamma(rot, 1, size = ntott)
elif op == 5 :
    v_ran = np.random.gamma(4, rot/4, size = ntott)
elif op == 6 :
    v_ran = np.full(ntott,rot)
elif op == 7 :
    mu = np.log(rot) - sigma**2/2
    v_ran =  np.random.lognormal(mu, sigma, size = ntott)

file=open('rn.dat','w+')
for j in range(0,ntott):
    file.write(str(v_ran[j])+\'$nline\')
file.close()" > rn.py
fi

# Plots
printf "import numpy as np
import matplotlib.pyplot as plt
import pylab
#from matplotlib import colors
from matplotlib import rc
import matplotlib.colors as mcolors
import matplotlib.cm as cm

dat1=np.loadtxt('fort.21')
dat2=np.loadtxt('fort.20')
dat3=np.loadtxt('fort.16')
dat4=np.loadtxt('fort.15')
dat5=np.loadtxt('fort.105')
dato=np.loadtxt('$data/datas$date/$state.dat')
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
plt.plot(dat4[:,0]+$tshf,cumsts[:,0],color = colormap(normalize(6)),marker='$mark',
markevery=$dot,markersize=8,label='cumulative', linewidth=2)
plt.plot(dat4[:,0]+$tshf,dat4[:,4],color = 'r',marker='$mark',
markevery=$dot,markersize=8,label='I', linewidth=2)
# plt.plot(dat5[:,0]+$tshf,dat5[:,1],color = colormap(normalize(2)),marker='$mark',
# markevery=$dot,markersize=8,label='q1', linewidth=2)
# plt.plot(dat5[:,0]+$tshf,dat5[:,2],color = colormap(normalize(2)),marker='$mark',
# markevery=$dot,markersize=8,label='q3', linewidth=2)
# plt.plot(dat4[:,0]+$tshf,dat4[:,8],color = colormap(normalize(8)),marker='$mark',
# markevery=$dot,markersize=8,label='min. cumulative', linewidth=2)
# plt.plot(dat4[:,0]+$tshf,dat4[:,9],color = colormap(normalize(9)),marker='$mark',
# markevery=$dot,markersize=8,label='max. cumulative', linewidth=2)
plt.plot(dato[:,0],cumst[:,0],color = 'k',label='cumultive data', linewidth=2)
plt.tick_params(labelsize='30',labeltop=False, labelright=False, labelbottom=False)
plt.legend(borderpad=0.1, shadow = True, loc='upper left', ncol=1,fontsize=(10))
plt.xlim(left=0, right=$ntot + $tshf)
plt.grid(True)


plt.subplot(222)
plt.bar(dat4[:,0]+$tshf,dat4[:,1],color = colormap(normalize(2)),
label='daily cases', width=0.9)
plt.bar(dato[:,0],dato[:,1],color = colormap(normalize(3)),
label='$state', width=0.7)
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
figure_name = 'fig.eps'	# name of the figure to be saved
plt.savefig(figure_name)

plt.show()
"> fig.py

if [ $oprn == '1' ]; then
python rn.py
fi

./exe
python fig.py &
cd $code
