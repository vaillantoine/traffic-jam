from echantillon_Poisson import *
from plot import *


P = 6
N = 15
gamma = 10
N_voiture=50

data,flux = genere_data(N, P, gamma, N_voiture)


v=classestime(flux,data[:,3])
#print(v)
print(flux)
