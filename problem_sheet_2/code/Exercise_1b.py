#%%
from uncertainties import ufloat
import math as m

#%%
# (b)
def activity(N: float, half_life: float):
	"""
	parameters:
		N, the number of nuclides
		half_life, the half life in years
	returns:
		A, the activity
	"""
	year_to_sec = 31556926
	T = half_life*year_to_sec
	A = N * m.log(2) / T
	return A

A_C14 = activity(6.02e14, ufloat(5730, 40))
A_K40 = activity(3.08e20, ufloat(1.277e9, 0.008e9))
A_Ar40 = 0.11*A_K40
print(A_C14)
print(A_K40)
print(A_Ar40)
print(A_C14 + A_K40 + A_Ar40)
#%%
# (c)
def dose_yr(A: float, E: float, m: float = 70):
	"""
	parameters:
		A, the activity in Bq
		E, the energy per decay in MeV
		m, the mass of the person in kg
	returns:
		D, the dose in one year
	"""
	year = 31556926
	energy = E * 1.602e-13
	N_decays = A * year
	D = N_decays * energy / m
	return D

D_C14 = dose_yr(A_C14, 0.16)
D_K40_Ca40 = dose_yr(0.89*A_K40, 1.3)
D_K40_Ar40 = dose_yr(0.11*A_K40, 1.461)

print(D_C14)
print(D_K40_Ca40)
print(D_K40_Ar40)
print(D_C14 + D_K40_Ca40 + D_K40_Ar40)
