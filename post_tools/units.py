import numpy as np
import matplotlib.pylab as plt

# units of metal in lammps
M = 15.99
m_c = 1.993E-26
kindex = 1.6E-19
vscale = 100
# v = 100
Ek1 = 0.5*M*m_c*vscale**2/(12*kindex)
Ek = 1000
v = np.sqrt(Ek/Ek1)
print(v)