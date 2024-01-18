from echantillon_Poisson import *
from plot import *


P = 6
N = 15
M=2
gamma = 1
N_voiture=50

data, flux=genere_data(N, P,  gamma, N_voiture)
indice, max=combinaison_routes_optimales(flux,M)

dbg=bhattacharyya_generalise(flux)
c=borne_proba_erreur(flux)-erreur_exp(N,P,M,gamma,N_voiture)
print(borne_proba_erreur(flux))
print(erreur_exp(N,P,M,gamma,N_voiture))
print(c)
