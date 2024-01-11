from echantillon_Poisson import *
from plot import *


P = 2
N = 8
M=2
gamma = 10
N_voiture=50

data, flux=genere_data(N, P,  gamma, N_voiture)
indice, max=combinaison_routes_optimales(flux,M)
print(indice,max)