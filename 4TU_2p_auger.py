#!/bin/python3
import plotUtils
import numpy as np


plotlist = [166.5,165.25, 161.75, 162.8, 160]

data       = np.loadtxt("day3/Scan_devices_X4TU_2p_NEXAFS_008.txt", skiprows=1403)
intensity  = np.loadtxt("day3/Scan_devices_X4TU_2p_NEXAFS_008.txt", skiprows=55, max_rows=41)[:,3]

energy = np.flip(np.arange(160,170.1,0.25))
xrange = np.linspace(100,165,1301)

data = data[:,1:] / intensity

plotUtils.plot(xrange,energy,data, name="4TU-2p", plotlist=plotlist)
