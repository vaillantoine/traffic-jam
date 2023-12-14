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