import numpy as np
import scipy.constants as c
from scipy.stats import linregress as linreg
import matplotlib.pyplot as plt
import uncertainties as u
from uncertainties import unumpy as unp
from matplotlib import rc

rc('font',**{'family':'serif','serif':['Computer Modern'], 'size':'16'})
rc('text', usetex=True)


nuclide_data = np.array([
	["B",  11, 5,  u.ufloat(9305  , 1)],
	["C",  11, 6,  u.ufloat(11434 , 1)],
	["N",  15, 7,  u.ufloat(109   , 1)],
	["O",  15, 8,  u.ufloat(3065  , 1)],
	["F",  19, 9,  u.ufloat(-1597 , 1)],
	["Ne", 19, 10, u.ufloat(1880  , 1)],
	["Na", 23, 11, u.ufloat(-10230, 1)],
	["Mg", 23, 12, u.ufloat(-5875 , 1)],
	["Si", 29, 14, u.ufloat(-23505, 1)],
	["P",  29, 15, u.ufloat(-18199, 1)],
	["Cl", 35, 17, u.ufloat(-31147, 1)],
	["Ar", 35, 18, u.ufloat(-24743, 1)],
	["Ca", 41, 20, u.ufloat(-37722, 1)],
	["Sc", 41, 21, u.ufloat(-30749, 1)],
	["Ti", 45, 22, u.ufloat(-41876, 1)],
	["V",  45, 23, u.ufloat(-34218, 1)]
])

def mass_diff(data: np.ndarray) -> np.ndarray:
	"""
	Calculates the mass difference

	parameters:
		data; numpy array; the input data
	returns:
		mass_diff_total; numpy array, the mass difference and the error
		mass_diff; numpy array; the mass difference
		error; numpy array; the error after the calculations
	"""
	idx1 = np.arange(0, len(data), 2)
	idx2 = np.arange(1, len(data), 2)
	data1 = data[idx1]
	data2 = data[idx2]
	mass_diff_total = (data2[:,3] - data1[:,3]) * 0.0009315 # MeV / u
	mass_diff = unp.nominal_values(mass_diff_total) 
	error = unp.std_devs(mass_diff_total)
	return mass_diff_total, mass_diff, error

def plot(X, Y, error):
	"""
	Plotting
	"""
	fig, ax = plt.subplots(1,1)
	fig.set_figwidth(6)
	fig.set_figheight(4)

	ax.set_xlabel(r'$\frac{3 e^2 A^{2/3}}{20 \pi \epsilon_0}$ [MeV $\times$ fm]')
	ax.set_ylabel(r'$\Delta E$ [MeV]')

	scale = 1.602e-13*1e-15 # Scaling the X data/axis to MeV * fm
	reg = linreg(X, Y)
	x_reg = np.linspace(X[0], X[-1], 200)
	y_reg = (x_reg*reg[0] + reg[1])

	print(reg)
	slope = 1/(reg[0]*scale)
	err = 2*(reg[4]/reg[0]) * 1/(reg[0]*scale) # calculating 2 standard deviations so approx 95% confidence
	print(f'r0 = {round(slope,2)} fm +/- {round(err,2)} fm')
	
	ax.plot(x_reg/scale, y_reg, c='r', label='Linear regression')
	ax.scatter(X/scale, Y, c='fuchsia', s=16, zorder=3, label='Data points')
	ax.errorbar(X/scale, Y, yerr=error, ls='None', zorder=1, label='Error')

	ax.legend()
	plt.tight_layout()
	plt.savefig('r0.pdf')


mdt, Dm, error = mass_diff(nuclide_data)
A = np.array([11, 15, 19, 23, 29, 35, 41, 45])
x_list = 3*(1.6e-19)**2 * A**(2/3) / (20*np.pi*8.85e-12)

plot(x_list, Dm, error)