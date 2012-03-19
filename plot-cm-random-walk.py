#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

md_output = np.loadtxt('data/cm-random-walk.csv', delimiter=',')
drift = md_output[:, 1:3]

driftx = drift[:,0]
drifty = drift[:,1]

plt.plot(driftx[0:5000], drifty[0:5000])
plt.xlim(-50, 50)
plt.xlabel("x-location of center of mass")
plt.ylim(-50, 50)
plt.ylabel("y-location of center of mass")
plt.title("Constrained random walk of center of mass of Lab molecular simulation\n(L-J forces only; 50 atoms; no thermostat; initial temperature = \"5\")")
plt.savefig('figures/cm-random-walk', dpi=300)
