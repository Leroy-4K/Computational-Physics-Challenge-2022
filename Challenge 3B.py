import numpy as np
import matplotlib.pyplot as plt
import math
import time


TIME = 0
def update_title(axes, s):
  global TIME
  TIME = time.time()-s
  axes.set_title(round(TIME,2))
  axes.figure.canvas.draw()

def update_time(s):
  global TIME
  TIME = time.time()-s
  


a = [5.2, 9.58, 19.29, 30.25, 39.51]
ecc = [0.05, 0.06, 0.05, 0.01, 0.25]





mass = [317.85, 95.16, 14.5, 17.2, 0.00]

earth_mass = 5.9722 * ((10)**(24))

for v in range(len(mass)):
  mass[v] = mass[v] * earth_mass

sun_mass = 1.9891 * ((10)**(30))
p = []

G = (6.67) * ((10)**(-11))

earth_a = 1
p_earth = ((earth_a**3) * (4 * (math.pi**2)) / ((G) * (sun_mass + earth_mass)))**(1 / 2)

for v in range(len(mass)):
  p.append(
    ((a[v]**3) * (4 * (math.pi**2)) / ((G) * (sun_mass + mass[v])))**(1 / 2))

frame_rate = 10
r = np.linspace(0.0, 2 * math.pi, 1000)
gap = 2 * math.pi / 1000
j = []
fig, ax = plt.subplots()
plt.ylabel("y/AU")
plt.xlabel("x/AU")
plt.grid()
plt.text(-5, 50, "Outer Planets Animation")
plt.text(40, 25, """Sun - Yellow
Jupiter - Red
Saturn - Orange
Uranus - Green
Neptune - Blue
Pluto - Grey""", fontsize = 12, 
         bbox = dict(facecolor = 'red', alpha = 0.5))

for i in range(0, len(ecc)):
  q = a[i] * (1 - (ecc[i]**2))
  j = q / (1 - (ecc[i] * np.cos(r)))
  x = j * np.cos(r)
  y = j * np.sin(r)
  if i == 0:
    ax.plot(x, y, 'red')
  elif i == 1:
    ax.plot(x, y, 'orange')
  elif i == 2:
    ax.plot(x, y, 'green')
  elif i == 3:
    ax.plot(x, y, 'blue')
  elif i == 4:
    ax.plot(x,y, 'grey')
theta = 2 * math.pi
TIME = 0
time_step = p_earth * 500
x_list = []
y_list = []

pls = []
arr = []
work = []
ng = 126
#timer = fig.canvas.new_timer(interval=100)

for i in range(0, len(ecc)):
  for ghj in range(ng):
    xd = ghj/250
    arr.append(xd * 500)
    q = a[i] * (1 - (ecc[i]**2))
    j = q / (1 - (ecc[i] * math.cos((theta * xd * time_step) / p[i])))
    x_list.append(j * math.cos((theta * xd * time_step) / p[i]))
    y_list.append(j * math.sin((theta * xd * time_step) / p[i]))
  pls.append(x_list)
  work.append(y_list)
  x_list = []
  y_list = []


#start=time.time()
#timer.add_callback(update_title, ax, start)
#timer.start()
plt.scatter(0, 0, c='yellow')
for bmx in range(ng-1):
  plt.title(str(round(arr[bmx],2)) + " years")
  plt.scatter(pls[4][bmx], work[4][bmx], c='grey')
  plt.scatter(pls[0][bmx], work[0][bmx], c='red')
  plt.scatter(pls[1][bmx], work[1][bmx], c='orange')
  plt.scatter(pls[2][bmx], work[2][bmx], c='green')
  plt.scatter(pls[3][bmx], work[3][bmx], c='blue')
  plt.pause(0.001)
  for nl in range(0, len(ecc)):
    plt.gca().collections[-1].remove()
plt.title(str(round(arr[-1],2)) + " years")
plt.scatter(pls[4][-1], work[4][-1], c='grey')
plt.scatter(pls[0][-1], work[0][-1], c='red')
plt.scatter(pls[1][-1], work[1][-1], c='orange')
plt.scatter(pls[2][-1], work[2][-1], c='green')
plt.scatter(pls[3][-1], work[3][-1], c='blue')

plt.show()
