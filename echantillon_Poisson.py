import numpy as np


def genere_flux(N, beta, gamma):
    xj = np.random.exponential(scale=beta, size=N)
    xjgamma = np.power(xj,gamma)
    flux = xjgamma / np.sum(xjgamma)
    return flux


def genere_data(N, P, beta, gamma, taille):
    flux = np.array([genere_flux(N, beta, gamma) for j in range(P)])

