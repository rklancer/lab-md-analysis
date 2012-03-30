#!/usr/bin/env python

from math import pi
import numpy as np
import matplotlib.pyplot as plt


# a = 48 * epsilon * sigma^12, in eV nm**12
# b = 24 * epsilon * sigma^6, in eV nm**6
# c = 1 elementary charge^2 / (4 * pi * epsilon_0) in eV nm

epsilon = 0.01034                   # eV
sigma = 0.340                       # nm
q = 1.602e-19                       # C
qe = 1 / (4 * pi * 8.8542e-12)      # J m / C**2

nm_per_m = 1e9                      # 1, in nm/m
eV_per_J = 6.2415e18                # 1, in eV/J

# equilibrium distance of a pair of stably attracted LJ+Coulomb particles of +1 and -1 charges
def eq_dist(epsilon = epsilon, sigma = sigma, charge1 = 1, charge2 = -1):

    a = 48 * epsilon * sigma**12        # eV nm**12
    b = 24 * epsilon * sigma**6         # eV nm**6
    c = -charge1*q * charge2*q * qe * nm_per_m * eV_per_J  # eV nm

    # Given potential:
    #    V(r) = 4 * epsilon * (sigma/r)**12 
    #           - 4 * epsilon * (sigma/r)**6 
    #           + (charge1*charge2)/(4*pi*epsilon_0) * (1/r)
    # then the roots of:
    #    p(r) = c * r**11 + b * r**6 - a
    # are the values at which dV/dr is 0

    # Therefore, find the roots of p(r):
    n = 11
    p = [0]*(n+1)

    p[n-11] = c
    p[n-6] = b
    p[n-0] = -a

    positive_real_roots = filter(lambda x: x.imag == 0 and x.real > 0, np.roots(p))

    if len(positive_real_roots) < 1:
       raise Exception("There ought to be a positive, real root in here somewhere")
    
    if len(positive_real_roots) >= 2:
        raise Exception("Oops, too many positive real roots!")
    
    eq_dist = positive_real_roots[0].real
    return eq_dist


def plot_dist():

    epsilons = np.linspace(epsilon/4, epsilon*4, 100)
    dists = map(eq_dist, epsilons)

    plt.plot(epsilons, dists)

    plt.xlim(epsilons[0], epsilons[99])
    plt.xlabel(r'Lennard-Jones $\epsilon$ parameter (eV)')
    plt.ylim(0, dists[99]*1.1)
    plt.ylabel("Equilibrium separation distance (nm)")
    plt.title("Equilibrium separation of 2 Lennard-Jones particles with charge +1 and -1\n" + r'(Plotted as a function of $\epsilon$ using $\sigma = 0.340$ nm)');

    (x, y) = (epsilon, eq_dist())
    plt.annotate(r'default $\epsilon$', xy=(x,y), xytext=(0.012, 0.22), 
        arrowprops=dict(facecolor='blue', shrink=0.05, frac=0.25, width=2, headwidth = 8))

plot_dist()
plt.savefig('figures/lj-coulomb-equilibrium-distance', dpi=300)
