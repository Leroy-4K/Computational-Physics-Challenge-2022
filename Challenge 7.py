import numpy as np
import matplotlib.pyplot as plt
import math
import time




a = [1.523, 0.723, 0.387, 1.00]
ecc = [0.09, 0.01, 0.21, 0.02]

mass = [0.107, 0.815, 0.055, 1]

earth_mass = 5.9722 * ((10)**(24))

for v in range(len(mass)):
  mass[v] = mass[v] * earth_mass

sun_mass = 1.9891 * ((10)**(30))
p = []

G = (6.67) * ((10)**(-11))
for v in range(len(mass)):
  p.append(
    ((a[v]**3) * (4 * (math.pi**2)) / ((G) * (sun_mass + mass[v])))**(1 / 2))
r = np.linspace(0.0, 2 * math.pi, 1000)
gap = 2 * math.pi / 1000
j = []
fig, ax = plt.subplots()
plt.xlabel("x/AU")
plt.ylabel("y/AU")
ax.text(-1.2, 3.3, "Inner solar system relative to Earth")
plt.text(1.35, 1.25, """Sun - yellow
Mercury - grey
Venus - orange
Earth - blue
Mars - red""", fontsize = 12, 
         bbox = dict(facecolor = 'red', alpha = 0.5))
theta = 2 * math.pi
time_step = p[3]
x_list = []
y_list = []

pls = []

work = []
ng = 10001
arr = []
for i in range(0, len(ecc)):
  ghj = 1
  qwe = 0
  while ghj < ng:
    xd = ghj/500
    arr.append(xd)
    q = a[i] * (1 - (ecc[i]**2))
    j = q / (1 - (ecc[i] * math.cos((theta * xd * time_step) / p[i])))
    x_list.append(j * math.cos((theta * xd * time_step) / p[i]))
    y_list.append(j * math.sin((theta * xd * time_step) / p[i]))
    ghj = ghj + 1
    qwe += 1
  pls.append(x_list)
  work.append(y_list)
  x_list = []
  y_list = []
for f in range(len(pls[0])):
  x_list.append(0)
  y_list.append(0)
pls.append(x_list)
work.append(y_list)
x_list = []
y_list = []

merc_x = []
merc_y = []
sun_x = []
sun_y = []
venus_x = []
venus_y = []
mars_x = []
mars_y = []
ax.scatter(0, 0, c='blue')
for gh in range(len(pls[0])):
  earth_x = pls[3][gh]
  earth_y = work[3][gh]
  merc_x.append(pls[2][gh]-earth_x)
  merc_y.append(work[2][gh]-earth_y)
  sun_x.append(pls[-1][gh]-earth_x)
  sun_y.append(work[-1][gh]-earth_y)
  venus_x.append(pls[1][gh]-earth_x)
  venus_y.append(work[1][gh]-earth_y)
  mars_x.append(pls[0][gh]-earth_x)
  mars_y.append(work[0][gh]-earth_y)
ax.plot(merc_x,merc_y,'grey')
ax.plot(sun_x, sun_y, 'yellow')
ax.plot(venus_x, venus_y, 'orange')
ax.plot(mars_x, mars_y, 'red')
plt.title(str(round(arr[-1],2)) + " years")
plt.show()