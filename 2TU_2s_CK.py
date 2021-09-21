#!/bin/python3

import numpy as np
import plotUtils

data = np.loadtxt("data/day1/Scan_devices_X2s_NEXAFS_CK_013.txt", skiprows=343)

energy = np.flip(np.arange(215,235.1,0.25))
xrange = np.arange(data.shape[0]) #np.linspace(100,165,1301)

data = data[:,1:]

plotUtils.plot(xrange,energy,data, name="2TU-2p CK", percentile=(5,85),savefig=True)
