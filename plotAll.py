#!/bin/bash/python

import numpy as np
import matplotlib.pyplot as plt
import glob

FOLDER = "Runs"

for filename in glob.glob(FOLDER):
    data = np.loadtxt(filename)
    plt.plot(data[0], data[1])

plt.show()
