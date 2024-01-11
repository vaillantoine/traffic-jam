import numpy as np
from itertools import combinations
def genere_flux(N,  gamma, N_voiture):
    xj = np.random.exponential(scale=1, size=N)
    xjgamma = np.power(xj, gamma)
    flux = xjgamma / np.sum(xjgamma)
    flux= flux*N_voiture #pour moduler l'intervalle des flux
    return flux


def genere_data(N, P,  gamma, N_voiture):
    """
    :param N: nombre de routes
    :param P: nombre de scénarios
    :param beta: parametres de la loi exp
    :param gamma: parametres de prédominance de la route la plus fréquentée
    :param N_voiture: nombre de voitures
    :return:

    """

    flux = np.array([genere_flux(N,  gamma,N_voiture ) for j in range(P)]).transpose()# flux[i,j] contient le flux de la route i sus le scénario j
    data= np.random.poisson(flux)
    return data, flux

def vraisemblance( j, flux, data):
    N,P=flux.shape
    l=1
    for i in range(N):
       # l*= np.exp(-flux[i,j]) * (flux[i,j]**data[i]) / np.math.factorial(data[i])
        l+=-flux[i,j] + data[i]*np.log(flux[i,j])
    return l

def classestime(flux,data):
    N,P=flux.shape
    L=[vraisemblance(j,flux,data ) for j in range(P)]
    j=L.index(max(L))
    return j

def bhattacharyya(flux1, flux2):
    return ((1/2) * (flux1+flux2)) - np.sqrt(flux1*flux2)

def combinaison_routes_optimales(flux,taille_combinaison):
    max=0
    indice=[]
    for combination in combinations(range(flux.shape[0]),taille_combinaison):
        a=1
        for route in combination:
            B=bhattacharyya(flux[route,0],flux[route,1])
            a*=B    #borne de bhattacharyya calculée
        if a>max:
            max=a
            indice=combination
    return indice, max  #retourne la combinaison et sa borne de bhattacharyya (B_ronde)
