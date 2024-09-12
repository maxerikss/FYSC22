import uncertainties as u

def xi(R: float):
	"""
	Calculates xi as seen in the assignment

	parameters:
		R; float; The  relative neutron capture probability
	
	returns;
		xi; float; the ratio
	"""
	U235 = 0.0072
	U238 = 0.9928
	return R * U238/U235

def Ncapture(xi: float, Nfission: float):
	"""
	Calculates the number of U238 turning into Pu239
	parameters:
		xi; float; The ratio against fission
		Nfission; float; the number of U235
	
	returns;
		Ncapture; float; the number of Pu239
	"""
	return Nfission * xi
	
N = Ncapture(xi(u.ufloat(4e-3, 0.1e-3)), u.ufloat(7.8e27, 0.5e27))

print(f"The total mass of Pu-239 {N * 239.052157 * 1.66e-27} kg" )