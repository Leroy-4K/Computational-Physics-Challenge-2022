import numpy as np
import matplotlib.pyplot as plt
import math

a = [9.58,
19.29,
5.20,
30.25,
39.51,
1.523,
0.723,
0.387,
1.00]
ecc = [0.06,
0.05,
0.05,
0.01,
0.25,
0.09,
0.01,
0.21,
0.02]

r = np.linspace(0.0,2*math.pi,1000)
j = []
fig, ax = plt.subplots()
plt.title("Elliptical Orbits of Planets")
plt.xlabel("x/AU")
plt.ylabel("y/AU")
plt.text(35, 8, """Sun - Yellow
Mercury - Grey
Venus - Crimson
Earth - Blue
Mars - Orange
Jupiter - Red
Saturn - Purple
Uranus - Cyan
Neptune - Magenta
Pluto - Black""", fontsize = 12, 
         bbox = dict(facecolor = 'red', alpha = 0.5))
ax.scatter(0,0,c='yellow')
for i in range (0, len(ecc)):
  q = a[i] * (1-(ecc[i]**2))
  j = q/(1 - (ecc[i] * np.cos(r)))
  x = j * np.cos(r) 
  y = j * np.sin(r)
  if i == 0:
    ax.plot(x,y,'purple')
  elif i == 1:
    ax.plot(x,y, 'cyan')
  elif i == 2:
    ax.plot(x,y, 'red')
  elif i == 3:
    ax.plot(x,y, 'magenta')
  elif i == 4:
    ax.plot(x,y, 'black')
  if i == 5:
    ax.plot(x,y, 'orange')
  if i == 6:
    ax.plot(x,y, 'crimson')
  elif i == 7:
    ax.plot(x,y, 'grey')
  elif i == 8:
    ax.plot(x,y,'blue')
  
plt.grid()
plt.show()