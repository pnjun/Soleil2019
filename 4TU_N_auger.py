#!/bin/python3
import plotUtils
import numpy as np


plotlist = []

fname = "data/day5/root_NEXAFS_4TU_013.txt"

data       = np.loadtxt(fname, skiprows=281)
intensity  = np.loadtxt(fname, skiprows=59, max_rows=45)[:,3]

energy = np.loadtxt(fname, skiprows=12, max_rows=45)[:,1]
xrange = np.linspace(320,405,171)

data = data[:,1:] / intensity

plotUtils.plot(xrange,energy,data, name="4TU-N", plotlist=plotlist, savefig=True)
