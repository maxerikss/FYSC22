import uncertainties as u
from uncertainties import unumpy as unp


def kgYear(P: float):
	"""
	Calculates the kg of U-235 used per year to generate a constant power of P

	parameters:
		P; float; The total Power
	return:
		prints the total mass used per year.
	"""
	eff = u.ufloat(0.35, 0.02) #efficiency of nuclear power plants
	power = P/1.602e-13 # converting from watt to MeV/s
	E_fission = u.ufloat(190, 5) * eff # energy per fission events in MeV
	year = 31556952 #seconds in a year
	p = u.ufloat(0.84, 0.002) # probability that U-236 decays with fission
	activity = power/E_fission 
	mass_per_N = (236 + 45562e-6)*1.66e-27 #mass per nuclide in kg
	N = activity * year/p # Total number of decays in a year
	total_mass = N*mass_per_N
	return print(f"The total number of nuclides needed is {N} and the mass is {total_mass}")

kgYear(2.2e9)
