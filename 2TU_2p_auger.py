#!/bin/python3
import plotUtils
import numpy as np


plotlist = [166.5,165.0, 161.5, 162.8, 160]

file1 = "data/day2/Scan_devices_X2p_RAM_NEXAFS_020.txt"
file2 = "data/day2/Scan_devices_X2p_RAM_NEXAFS_021.txt"

data1 = np.loadtxt(file1, skiprows=1403)
data2 = np.loadtxt(file2, skiprows=1403)
intensity1 = np.loadtxt(file1, skiprows=55, max_rows=41)[:,3]
intensity2 = np.loadtxt(file2, skiprows=55, max_rows=41)[:,3]


energy = np.flip(np.arange(160,170.1,0.25))
xrange = np.linspace(100,165,1301)

data = ( data1[:,1:] + data2[:,1:] ) / (intensity1 + intensity2)

plotUtils.plot(xrange,energy,data, name="2TU-2p", plotlist=plotlist, savefig=True)
