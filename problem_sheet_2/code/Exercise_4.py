#%%
import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt
from matplotlib import rc

rc('font',**{'family':'serif','serif':['Computer Modern'], 'size':'16'})
rc('text', usetex=True)

#%%
k = np.sqrt( 938.9 * (35 - 2.2) / 197.3**2 )
q = np.sqrt(938.9 * 2.2 / 197.3**2)
R = 2.1

denom = R/2 - np.sin(2*k*R)/(4*k) + np.sin(k*R)**2 / (2*q)
A = np.sqrt(1 / denom)
C = np.sin(k*R)/(np.exp(-q*R)) * A

print(round(A,2), round(C,2))
#%%
r = np.linspace(0, 10, 500)
def u(r):
	return np.piecewise(r, [r <= 2.1, r > 2.1], [lambda x: A*np.sin(k*x), lambda x: C*np.exp(-q*x)])

def P(r):
	return np.abs(u(r))**2

I_outside = quad(P, 2.1, np.inf)[0]
time_outside = round(I_outside*100, 1)

fig, ax = plt.subplots(1,1)
fig.set_figwidth(8)
fig.set_figheight(4)


ax.plot(r, P(r), color='b', label=r'$\left| u(r) \right|^2$')
fill_x = np.linspace(2.1, 10, 300)
ax.fill_between(fill_x, P(fill_x), color='r', alpha=0.3, label=rf'$P(r>2.1) = {time_outside} \%$')
ax.legend()

ax.set_xlabel(r'Distance $r$ [fm]')
ax.set_ylabel(r'$\left| u(r) \right|^2$')

ax.set_xlim(0, 10)
ax.set_ylim(0, 0.35)

plt.savefig('Exercise4.pdf', bbox_inches='tight')


