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
traj=5000   # number of trajectories


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
cd $runs
