#run these commands in cmd without hash_tag(#)
#pip install matplotlib

import sys
import argparse
import numpy as np
from matplotlib.pyplot import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# lorenz attractor - example of simple dynamical system governed by three simple
# differential equations: http://mathworld.wolfram.com/LorenzAttractor.html
#  http://en.wikipedia.org/wiki/Lorenz_attractor

def lorenz_attractor():

    steps = 10000
    dt = 0.01
    opfile = 'lorenz_map1.png'
    sigma = 10
    rho = 28
    beta = 8.0/3 

    if options.rho:
        rho = options.rho
    if options.sigma:
        sigma = options.sigma
    if options.beta:
        beta = options.beta
                        
    xs = np.empty((steps + 1,))
    ys = np.empty((steps + 1,))
    zs = np.empty((steps + 1,))
    xs[0], ys[0], zs[0] = (0., 1., 1.05)

    # loop over steps in increments of dt
    for i in np.arange(steps):
        xdot, ydot, zdot = lorenz(xs[i], ys[i], zs[i], rho, beta, sigma)
        xs[i+1] = xs[i] + (xdot * dt)
        ys[i+1] = ys[i] + (ydot * dt)
        zs[i+1] = zs[i] + (zdot * dt)              

    fig = plt.figure()
    ax = Axes3D(fig)
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    ax.plot(xs, ys, zs, label="lorenz")
    ax.legend()
    if options.f:
        plt.savefig(options.f)
    else:
        plt.show()

def lorenz(x, y, z, r, b, s):
    xdot = s*(y - x)
    ydot = r*x - y - x*z
    zdot = x*y - b*z
    return xdot, ydot, zdot

def main():
    lorenz_attractor()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-rho", type=float, help="r value")
    parser.add_argument("-sigma", type=float, help="sigma value")
    parser.add_argument("-beta", type=float, help="beta value")
    parser.add_argument("-f", help="o/p png file", metavar="FILE")
    options = parser.parse_args()
    main()
