#%%
import numpy as np
import scipy.constants as c
from uncertainties import ufloat
from scipy.integrate import quad


#%%

rho_In = 7.3
m_In = ufloat(114.903878773, 0.000000012) * c.u*1000
n_In = rho_In/m_In

#%%
def decay(t, half_life=54):
	return np.exp(- np.log(2) * t / half_life)

counts = 5e4
efficiency = 3e-4
I = quad(decay, 15, 75)[0]
N_0 = counts / (efficiency * I)
r = N_0 / 60
print(f"There have been a total of {int(N_0)} reactions and a reaction rate of {r}")

#%%

flux = r / (n_In * 9e-6 * 160e-24)
print(f"The neutron flux is {flux}")