import numpy as np
#Generate a lot of random numbers from specific distribution according to
#imput options generated by user. These random numbers are the daily mean
#of new infections of each individual in the population at each day of
#propagation
op = 7
ntott = (10+9999990+0+0+0)*(18 - 4)
rot= 4/(18 - 4)
sigma = 2.0

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
    file.write(str(v_ran[j])+'\n')
file.close()