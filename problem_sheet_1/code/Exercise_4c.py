import uncertainties as u
import numpy as np

def power(mass: float):
	"""
	Calculates the power from a given mass Cf254

	parameters:
		mass; float; the mass of Cf254

	return:
		power; float; The total power released from Fission
	"""
	nuclide_mass = 254.087317 * 1.66e-27 #mass in kg/nuclide
	N_0 = mass/nuclide_mass #total number
	T12 = u.ufloat(60.5, 0.2) * 86400 #half life in seconds
	l = np.log(2)/(T12)
	A_0 = N_0 * l
	E_per_event = u.ufloat(225, 5) * 1.602e-13
	print(N_0)
	return A_0 * E_per_event  # power in W

P = power(1e-9) 
Peff = P * u.ufloat(0.35, 0.02) # Reactor efficiency

print(f" The power is {Peff*1e3} mW")

energy_minute = P * 60
print(f"The temperature change in one minute is {energy_minute/(1e-9 * 110)}")