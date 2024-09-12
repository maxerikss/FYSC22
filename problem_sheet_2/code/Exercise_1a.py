import numpy as np

def Zmin(A: int) -> float:
	"""
	Calculation of Zmin from mass number

	parameters: 
		A; int; The mass number.
	returns: 
		Zmin; float; The minimum Z
	"""
	return A/(1.98 + 0.015 * A**(2/3))

def find_ee_A(Z: int) -> int:
	"""
	Calculation of the mass number of the most stable even-even nuclide of given atomic number

	parameters:
		Z; int; The atomic number for which the most stable nuclide is to be found
	returns: 
		A; int; The mass number of the most stable even-even nuclide with atomic number Z
	"""
	A_list = np.arange(Z, Z +200, 2)
	idx = np.argmin(np.abs((Zmin(A_list) - Z)))
	return A_list[idx]

print(f"The most stable nuclide is nickel-{find_ee_A(28)}")