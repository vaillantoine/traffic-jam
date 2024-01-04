import numpy as np


def genere_flux(N):
    gamma = np.random.exponential(size=N)
    flux = np.random.exponential(N)


def genere_data(N, P, ß, gamma, taille):
    """
    On genere des données numériques ainsi que les flux utilisés
    :param N: le nombre de route
    :param P: le nombre de scénarios
    :param ß: réel positif associé à la moyenne de la loi exp
    :param gamma: réel positif - coef de dominance
    :param taille: taille de l'échantillon
    :return: une liste d'observations, une liste de flux
    """
    data = []
    flux = []
    for j in range(P):
        flux_j = genere_flux(gamma, ß, N, P)
        data_j = []
        for i in flux_j:
            data_j = data + list(generer_echantillons_poisson(taille, i))
        data += data_j
        flux += flux_j
    return data, flux
