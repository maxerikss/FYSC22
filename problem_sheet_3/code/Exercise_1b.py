import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc

rc('font',**{'family':'serif','serif':['Computer Modern'], 'size':'16'})
rc('text', usetex=True)


def B(A: int, Z: int) -> float:
	"""
	Implementation of the Weizsacker mass formula from the lecture,
	for even-even nuclides

	parameters:
		A; int; The mass number
		Z; int; The atomic number

	returns:
		B; float; Binding energy [MeV]
	"""
	N = A - Z
	volume_term = 15.9 * A
	surface_term = 18.4 * A**(2/3)
	coulomb_term = 0.71 * Z**2 * A**(-1/3)
	assymetry_term = 23.2 * (N - Z)**2 / A
	pairing_term = 11.5 * A**(-1/2)
	return volume_term - surface_term - coulomb_term - assymetry_term + pairing_term

def Sn(A: int, Z: int) -> float:
	"""
	Finding the neutron seperation energy [MeV]

	parameters:
	A; int; The mass number
	Z; int; The atomic number

	returns:
		Sn; float; The neutron seperation energy [MeV]
	"""
	return B(A, Z) - B(A - 1, Z)

def Sp(A: int, Z: int) -> float:
	"""
	Finding the proton seperation energy [MeV]

	parameters:
	A; int; The mass number
	Z; int; The atomic number

	returns:
		Sp; float; The proton seperation energy [MeV]
	"""
	return B(A, Z) - B(A - 1, Z - 1)

def find_driplines(Z: int, pr: bool = False) -> float:
	"""
	Finding the neutron and proton driplines for an even-even nuclide with a given atomic number

	parameters:
		Z; int; the atomic number

	returns:
		Driplines; tuple; A tuple containging the mass numbers 
							on the form (neutron dripline, proton dripline)
	"""

	A_list = np.arange(Z+2, Z + 200, 2)
	
	Sn_list = Sn(A_list, Z)
	idx_N = np.argmin(np.abs(Sn_list))
	N_dripline = A_list[idx_N]

	Sp_list = Sp(A_list, Z)
	idx_P = np.argmin(np.abs(Sp_list))
	P_dripline = A_list[idx_P]
	
	if pr:
		print(f"The neutron dripline is nickel-{N_dripline} and the proton dripline is nickel-{P_dripline}")

	return (N_dripline, P_dripline)


def plot():
	"""
	Plotting the drip lines
	"""
	Z_list = np.arange(4, 82, 2)
	A_dripline = np.vectorize(find_driplines)

	N_neutron = A_dripline(Z_list)[0] - Z_list
	N_proton = A_dripline(Z_list)[1] - Z_list

	fig, ax = plt.subplots(1,1)
	fig.set_figheight(4*1.5)
	fig.set_figwidth(4*(11125/7438)*1.5)

	ax.plot(N_neutron, Z_list, c='b', lw=3, label='Neutron dripline')
	ax.plot(N_proton, Z_list, c='r', lw=3, label='Proton dripline')

	img = plt.imread('./NuclideMap.jpg')
	ax.imshow(img, extent=[-0.5, 176.5, -0.5, 117.5])

	ax.set_xlim(0, 120)
	ax.set_ylim(0, 80)

	ax.set_ylabel(r'Atomic number, $Z$')
	ax.set_xlabel(r'Neutron number, $N$')

	ax.legend()

	plt.savefig('driplines.pdf', dpi=500)

plot()