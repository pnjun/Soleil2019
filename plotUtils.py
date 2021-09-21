import numpy as np
import matplotlib.pyplot as plt

def plot(xrange, energy, data, name="", plotlist=[], percentile=(1,99)):

    def plot2d():
        cmax = np.percentile(data, percentile[1])
        cmin = np.percentile(data, percentile[0])

        plt.xlabel("Kinetic Energy [eV]")
        plt.ylabel("Photon Energy [eV]")
        plt.pcolormesh(xrange, energy, data.T, shading='nearest', cmap='inferno', vmax=cmax, vmin=cmin)

    def plotCutout():
        plt.xlabel("Kinetic Energy [eV]")
        plt.ylabel("Inensiity [a.u.]")
        for en in plotlist:
            id = np.argmin(np.abs(en-energy))
            plt.plot(xrange-en, data.T[id], label=f'{energy[id]} eV')
        plt.legend()

    if plotlist:
        plt.figure(figsize=(8,12))
        plt.subplot(212)
        plotCutout()
        plt.subplot(211)
    else:
        plt.figure(figsize=(8,6))
    plot2d()

    plt.suptitle(name)
    plt.tight_layout()

    if name:
        plt.savefig(f"{name}.png")
    plt.show()
