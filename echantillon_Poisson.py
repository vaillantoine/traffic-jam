import numpy as np
from itertools import combinations


def genere_flux(N, gamma, N_voiture):
    """
    Génère les flux
    :[int] N: nombre de route
    :[float] gamma: facteur de difficulté (gamma<1 : discrimination difficile, gamma>1: facile
    :[int] N_voiture: nombre de voiture par sénario
    :return: tableau de flux. flux[i]: flux de la route i
    """
    xj = np.random.exponential(scale=1, size=N)
    xjgamma = np.power(xj, gamma)
    flux = xjgamma / np.sum(xjgamma)
    flux = flux * N_voiture  # pour moduler l'intervalle des flux
    return flux


def genere_data(N, P, gamma, N_voiture):
    """
    :param N: nombre de routes
    :param P: nombre de scénarios
    :param beta: parametres de la loi exp
    :param gamma: parametres de prédominance de la route la plus fréquentée
    :param N_voiture: nombre de voitures
    :return:

    """

    flux = np.array([genere_flux(N, gamma, N_voiture) for j in range(P)]).transpose()  # flux[i,j] contient le flux de la route i sus le scénario j
    data = np.random.poisson(flux)
    return data, flux


def vraisemblance(j, flux, data):
    """
    Calcule la vraisemblance pour chaque scénarion sachant les données entrées
    :[int] j: numéro du scénario
    :[np.array(N,P)] flux: flux[i,j] flux de la route i sous le scénario j
    :[np.array(N,P)] data: data[i,j] traffic observé sur la route i (généré avec le scénario j)
    :[float] return: l = vraisemblance du flux[:,j] sur data + sum(ln(data!))
    """
    N, P = flux.shape
    l = 1
    for i in range(N):
        # l*= np.exp(-flux[i,j]) * (flux[i,j]**data[i]) / np.math.factorial(data[i])
        l += -flux[i, j] + data[i] * np.log(flux[i, j])
    return l


def classestime(flux, data):
    """
    Estime le scénario selon les data observées
    [np.array(N,P)] flux: tableau des flux ; flux[i,j]: flux de la route i sous le scénario j
    [np.array(N,P)] data: tableau des données observées ; data[i,j]: traffic observé sur la route i sous le scénario j
    [int] return: indice j qui maximise vraisemblance(j, flux, data)
    """
    N, P = flux.shape
    L = [vraisemblance(j, flux, data) for j in range(P)]
    j = L.index(max(L))
    return j


def bhattacharyya(flux1, flux2):
    """
    Calcule la borne de Bhattacharyya entre les loi de Poisson de moyyenne flux1 et flux2 (sur une donnée)
    [float] flux1: moyenne de la loi de Poisson 1
    [float] flux2: moyenne de la loi de Poisson 2
    [float] return: borne de Bhattacharyya
    """
    return ((1 / 2) * (flux1 + flux2)) - np.sqrt(flux1 * flux2)
    return (1/2) * (flux1+flux2) - np.sqrt(flux1*flux2)

def bhattacharyya_N(flux1, flux2):
    a = 0
    N = flux1.shape[0]
    for i in range(N):
        B = bhattacharyya(flux1[i], flux2[i])
        a += B
    return a


def combinaison_routes_optimales(flux, taille_combinaison):
    """
    Donne la combinaison de route qui minimise la borne de Bhattacharyya dans le cas à 2 scénarios
    [ flux:
    :param taille_combinaison:
    :return:
    """
    max = 0
    indice = []
    for combination in combinations(range(flux.shape[0]), taille_combinaison):
        a = 1
        for route in combination:
            B = bhattacharyya(flux[route, 0], flux[route, 1])
            a *= B  # borne de bhattacharyya calculée
        if a > max:
            max = a
            indice = combination
    return indice, max  # retourne la combinaison et sa borne de bhattacharyya (B_ronde)

def bhattacharyya_generalise(flux):
    N,P = flux.shape
    c=0
    for j1 in range(P):
        for j2 in range(j1+1,P):
            c+=np.exp(-bhattacharyya_N(flux[:,j1],flux[:,j2]))
    dBG=-np.log((2/P)*c)
    return dBG

def borne_proba_erreur(flux):
    return (1/2)*np.exp(-bhattacharyya_generalise(flux))
def erreur_exp(N,P,M,gamma,N_voiture):
    C = [0 for k in range(P)]
    for k in range(100):
        data, flux = genere_data(N, P, gamma, N_voiture)
        index, _ = combinaison_routes_optimales(flux,M) #indice qu'on veut garder
        for i in range(P-1, -1, -1):
            if i not in index:
                np.delete(data, i, axis=1)
                np.delete(flux, i, axis=1)
        C[classestime(flux, data[:, 3])] +=1
    C.pop(3)
    C=np.array(C)
    C=C/100
    return np.sum(C)
