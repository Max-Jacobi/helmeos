"""Test accuracy of code; to run: "python -m helmeos.test" """
import numpy as np
from .helm_table import HelmTable
from . import table_param as tab
try:
    import helmholtz
except ImportError:
    print('Python package "helmholtz" not found.')
    print('See https://github.com/jschwab/python-helmholtz for code download.')


vars_to_test = ['etot', 'ptot', 'cs', 'sele']

ht = HelmTable()
nrand = 100

# density
dlo, dhi = tab.dens_log_min, tab.dens_log_max
dens = np.arange(dlo, dhi + 1)
dens = 10**np.concatenate((dens,  (dhi - dlo) * np.random.random(nrand) + dlo))
# temperature
tlo, thi = tab.temp_log_min, tab.temp_log_max
temp = np.arange(tlo, thi + 1)
temp = 10**np.concatenate((temp,  (thi - tlo) * np.random.random(nrand) + tlo))

rho_in = np.zeros(dens.size * temp.size)
temp_in = np.zeros(dens.size * temp.size)

# make 1D array of all combinations of dens, temp
ind = 0
for i in dens:
    for j in temp:
        rho_in[ind] = i
        temp_in[ind] = j
        ind += 1

print("Loading tables.")
# our method
ours = ht.eos_call(rho_in, temp_in, 1.0, 1.0)
# their method
theirs = helmholtz.helmeos(rho_in, temp_in, 1.0, 1.0)


print("Showing max relative error for a few variables.")
print("var, rel_err")
for var in vars_to_test:
    a, b = ours[var], getattr(theirs, var)
    dif = np.abs((a - b) / b)
    i = dif.argmax()
    print(var, dif[i])