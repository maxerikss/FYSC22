#%%
import numpy as np
import scipy.constants as c

#%%
# (a)

def r(theta, Ta , ma, mX):
	nom = np.sqrt(ma**2 * Ta)
	denom = ma + mX
	return nom/denom * np.cos(theta*np.pi/180)

def s(Q, Ta, ma,  mX):
	nom = mX*Q + Ta*(mX - ma)
	denom = ma + mX
	return nom/denom

def Tb(theta, Ta = 9, Q = 0,
	  ma = c.physical_constants['proton mass energy equivalent in MeV'][0], 
	  mX = 7.016003434*c.physical_constants['atomic mass constant energy equivalent in MeV'][0]):
	T = []
	pm = np.sqrt(r(theta, Ta, ma, mX)**2 + s(Q, Ta, ma, mX))
	sqrtTb_pos = r(theta, Ta, ma, mX) + pm
	sqrtTb_neg = r(theta, Ta, ma, mX) - pm
	T.append(sqrtTb_pos**2)
	if sqrtTb_neg >= 0:
		T.append(sqrtTb_neg**2)
	else:
		T.append(np.NaN)
	return T

#%%

print(f"The energy of the proton after scattering with theta = 45 deg, is T = {np.round(Tb(45)[0], 2)} or T = {np.round(Tb(45)[1], 2)}")
print(f"The energy of the proton after scattering with theta = 90 deg, is T = {np.round(Tb(90)[0], 2)} or T = {np.round(Tb(90)[1], 2)}")
print(f"The energy of the proton after scattering with theta = 135 deg, is T = {np.round(Tb(135)[0], 2)} or T = {np.round(Tb(135)[1], 2)}")

#%%
# (b)
print(f"The energy of the proton after scattering with theta = 90 deg and Q = -0.477 MeV, is T = {np.round(Tb(90, Q=-0.477)[0], 2)} or T = {np.round(Tb(90, Q=-0.477)[1], 2)}")

#%%
# (c)

def coulombWork(Za, ZX, ra, rX):
	vacuum = 1/(4*np.pi*c.epsilon_0)
	e = c.elementary_charge
	distance = (ra + rX)*1e-15
	return vacuum * Za * ZX * e**2 / (distance * c.electron_volt*1e6)

E_p_Au = coulombWork(1, 79, 0.833, 6.98)
print(f"The energy of the proton must be E_p = {E_p_Au} MeV")

#%%
# (d)

E_Ca_Am = coulombWork(20, 95, 4.36, 7.49)
print(f"The energy of the Ca-48 beam must be E_p = {E_Ca_Am} MeV")