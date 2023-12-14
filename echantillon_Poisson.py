import numpy as np


def generer_echantillons_poisson(taille, lambda_param):
    """
    Génère des échantillons suivant la loi de Poisson.

    Parameters:
        taille (int): Le nombre d'échantillons à générer.
        lambda_param (float): Le paramètre lambda de la distribution de Poisson.

    Returns:
        numpy.ndarray: Tableau contenant les échantillons générés.
    """
    echantillons = np.random.poisson(lambda_param, taille)
    return echantillons


def genere_flux(gamma, ß, N, P):
    """
    On genere des scénarios de flux avec des lois exponentielles
    :param gamma: réel positif
    :param ß: réel positif associé à la moyenne de la loi exp
    :param N: le nombre de route
    :param P: le nombre de scénarios
    :return: le flux
    """
    flux = []
    for j in range(P):
        x = np.random.exponential(ß, size=N) * gamma
        flux += x / np.sum(x)

    return flux


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
            data_j += generer_echantillons_poisson(taille, i)
        data += data_j
        flux += flux_j
    return data, flux
