from numpy import argsort
from numpy.linalg import eig
from scipy.constants import hbar, m_e, eV, c

# Parameters
a=m_e # m size of electron
m= eV / c**2

L = # length of domain -10a<x<10a
N = 100 # number of grid cells
dx = # size of grid cell

# set the x interval for solving, 10 electron radii each direction: -10a < x < 10a
x =  # x runs -L/2 to +L/2 by steps dx

# Define the potential well
# either zero for square well or like above for quadratic well
Vpot =

# Form the matrix
Tdiag = # tridiagonal 2nd derivative
H =

# Get eigenvalues and eigenvectors
w,v = eig(H)

# sort by magnitude of eig vals, selecting just lowest 3 energy levels
idx=argsort(w)
E = w[idx[:3]]
Psi = v[:,idx[:3]]

# plot lowest 3 energy levels
from matplotlib.pyplot import plot,xlabel,ylabel,legend,show, figure, subplot
for i in range(3):
    plot(x,Psi[:,i], label='E='+str(round(E[i],1)))
legend()