import numpy as np


def genere_flux(N, beta, gamma):
    xj = np.random.exponential(scale=beta, size=N)
    xjgamma = np.power(xj, gamma)
    flux = xjgamma / np.sum(xjgamma)
    return flux


def genere_data(N, P, beta, gamma, taille):
    flux = np.array([genere_flux(N, beta, gamma) for j in range(P)]).transpose()  # flux[i,j] contient le flux de la route i sus le scénario j

    data = np.zeros((N, P, taille))  # data[i,j,n] contient la valeur simulée n°n pour la route i sous le scénarion j
    for i in range(N):
        for j in range(P):
            data[i, j, :] = np.random.poisson(flux[i, j], size=taille)
    return data
