import matplotlib.pyplot as plt


def plot_data(data):
    P = len(data)
    for j in range(P):
        data_j = data[j]
        N = len(data_j)
        for i in range(N):
            plt.subplot(P, N, i + j + 1)
            plt.hist(data_j[i])
    plt.show()
