#!/bin/python3

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("day1/Scan_devices_X2s_NEXAFS_CK_013.txt", skiprows=343)

energy = np.flip(np.arange(215,235.1,0.25))
xrange = np.arange(data.shape[0]) #np.linspace(100,165,1301)

data = data[:,1:]

cmax = np.percentile(data, 85)
cmin = np.percentile(data, 20)
plt.title("2TU - CK")
plt.pcolormesh(xrange, energy, data.T, shading='nearest', cmap='inferno', vmax=cmax, vmin=cmin)
plt.show()
