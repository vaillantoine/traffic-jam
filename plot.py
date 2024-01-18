import matplotlib.pyplot as plt
from echantillon_Poisson import *
import numpy as np

N = 15
P = 6
gamma = 0.5
N_voiture = 50


def plot_data(flux):
    N,P = flux.shape
    fig, ax = plt.subplots()
    for j in range(P):
        ax.plot(range(N), flux[:,j], label=f'senario {j}')
    plt.legend()
    plt.savefig("./fig/plotdata.png")
    plt.show()

def plot_vraisemblance(flux, data):
    P = flux.shape(1)
    L=[vraisemblance(j,flux,data ) for j in range(P)]
    fig, ax = plt.subplots()
    ax.plot(range(P),L)
    plt.savefig("./fig/plot_vraisemblance.png")
    plt.show()


def hist_estime():
    C=[]
    for k in range(10000):
        data, flux = genere_data(N,P,gamma, N_voiture)
        C+=[classestime(flux,data[:,3] )]
    print(np.histogram(C))
    fig, ax = plt.subplots()
    ax.hist(C,bins=range(P))
    plt.savefig("./fig/hist_estime.png")
    plt.show()

def plot_perf(N,P,N_voiture):
        plt.subplot(131)
        L=[]
        K=[]
        for capteur in range(1,N+1):
            data,flux=genere_data(N,P,gamma, N_voiture)
            K.append(erreur_exp(N,P,capteur,gamma,N_voiture)) #liste de proba d'erreur
            L.append(borne_proba_erreur(flux)) #liste de borne sup
        plt.plot(L)
        plt.plot(K)
        plt.show()




if __name__ == '__main__':
    # data, flux = genere_data(N,P,gamma, N_voiture)
    # plot_data(flux)
    # plot_vraisemblance(flux, data[:, 3], P) #toutes les routes sur le senarios 5
    # hist_estime()
    plot_perf(N, P, N_voiture)

