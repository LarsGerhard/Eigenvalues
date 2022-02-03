from numpy import argsort, linspace, eye
from numpy.linalg import eig
from matplotlib.pyplot import plot,legend, show
from scipy.constants import hbar, c, eV, angstrom

# Parameters
a = angstrom # m size of electron
m = eV / c**2

L = 20 * a # length of domain -10a<x<10a
N = 101 # number of grid cells
dx = L / (N - 1) # size of grid cell

# set the x interval for solving, 10 electron radii each direction: -10a < x < 10a
x = linspace((-L / 2), (L / 2), N) # x runs -L/2 to +L/2 by steps dx

# Define the potential well
# either zero for square well or like above for quadratic well
Vpot = 0

# Form the matrix
Tdiag = -2 * eye(N) + 1 * eye(N,N,1) + 1 * eye(N,N,-1)  # tridiagonal 2nd derivative
M = (1 / L**2) * Tdiag
H = -(hbar**2 / (2 * m)) * M + Vpot

# Get eigenvalues and eigenvectors
w,v = eig(H)

# sort by magnitude of eig vals, selecting just lowest 3 energy levels
idx=argsort(w)
E = w[idx[:3]]
Psi = v[:,idx[:3]]

# plot lowest 3 energy levels

for i in range(3):
    plot(x,Psi[:,i], label='E='+str(round(E[i],1)))
legend()
show()