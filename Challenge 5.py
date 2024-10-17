import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
from scipy.interpolate import make_interp_spline, PPoly
import random
a = 39.51
ecc = 0.25
P = 248.35
g = np.linspace(0.0,2*math.pi,1000)
fig, ax = plt.subplots()
earth_mass = 5.9722 * (10)**(24)
mass = 0.0022 * earth_mass
beta = 17.5
sun_mass = 1.9891 * ((10)**(30))
G = (6.67) * ((10)**(-11))
p = (a**3) * (4 * (math.pi**2)) / ((G) * (sun_mass + mass))**(1/2)
theta = 0
pluto_ecc = 0.25
t = np.arange(10, 800, 10)
plt.xlabel("Time/Yr")
plt.ylabel("Orbit Polar angle/rad")
plt.title("Orbital angle vs time: Pluto")
plt.text(0, 18, """Circular ecc = 0: blue
ecc = 0.25: red""", fontsize = 12, bbox = dict(facecolor = 'red', alpha = 0.5))
#Numeric method to compute polar angle vs orbit time
def angle_vs_time( t, P, ecc, theta0 ):
  #%Angle step for Simpson's rule
  dtheta = 1/1000
  #%Number of orbits
  N = math.ceil(t[-1]/P)
  #%Define array of polar angles for orbits
  theta = np.arange(theta0, ( 2*math.pi*N + theta0 ), dtheta)
  #%Evaluate integrand of time integral
  
  f = (1 - ecc*np.cos(theta) )**(-2)
  #%Define Simpson rule coefficients c = [ 1, 4, 2, 4, 2, 4, ....1 ]
  L = len(theta)
  hg = np.arange(0, L-2, 1)
  isodd = []
  for jk in range(len(hg)):
    v = hg[jk] % 2
    if v == 1:
      isodd.append(4)
    else:
      isodd.append(2)
  c = [1]
  for be in range(len(isodd)):
    c.append(isodd[be])
  c.append(1)
  kl = c * f
  #%Calculate array of times
  tt = P*( (1-ecc**2)**(3/2) )*(1/(2*math.pi))*dtheta*(1/3)*np.cumsum(kl)
  #%Interpolate the polar angles for the eccentric orbit at the circular orbit
  #times
  #theta = interp1( tt, theta, t, 'spline' );
  bhu = interpolate.interp1d(tt, theta, kind="linear")
  x = []
  y = []
  for l in range(len(t)):
    x.append(t[l])
    y.append(bhu(t[l]))
  if ecc == pluto_ecc:
    ax.plot(x,y, 'blue')
  else:
    ax.plot(x,y, 'red')
angle_vs_time(t,248, 0.25, 0)
angle_vs_time(t, 248, 0, 0)
plt.show()