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
frame_rate = 10
r = np.linspace(0.0, 2 * math.pi, 1000)
gap = 2 * math.pi / 1000
j = []
fig, ax = plt.subplots()
plt.xlabel("x/AU")
plt.ylabel("y/AU")
plt.grid()
plt.text(-0.4, 2, "Inner Planets Animation")
plt.text(1.35, 1.25, """Sun - Yellow
Mercury - Grey
Venus - Orange
Earth - Blue
Mars - Red""", fontsize = 12, 
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
    ax.plot(x, y, 'grey')
  else:
    ax.plot(x, y, 'blue')
theta = 2 * math.pi
TIME = 0
time_step = p[3] * 20
x_list = []
y_list = []

pls = []

work = []
ng = 48
#timer = fig.canvas.new_timer(interval=100)
arr = []
for i in range(0, len(ecc)):
  ghj = 1
  qwe = 0
  while ghj < ng:
    xd = ghj/500
    arr.append(xd*20)
    q = a[i] * (1 - (ecc[i]**2))
    j = q / (1 - (ecc[i] * math.cos((theta * xd * time_step) / p[i])))
    x_list.append(j * math.cos((theta * xd * time_step) / p[i]))
    y_list.append(j * math.sin((theta * xd * time_step) / p[i]))
    ghj = ghj + 2
    qwe += 1
  pls.append(x_list)
  work.append(y_list)
  x_list = []
  y_list = []

  

#start=time.time()
#timer.add_callback(update_title, ax, start)
#timer.start()
plt.scatter(0, 0, c='yellow')
for bmx in range(qwe-1):
  plt.title(str(round(arr[bmx],2)) + " years")
  plt.scatter(pls[0][bmx], work[0][bmx], c='red')
  plt.scatter(pls[1][bmx], work[1][bmx], c='orange')
  plt.scatter(pls[2][bmx], work[2][bmx], c='grey')
  plt.scatter(pls[3][bmx], work[3][bmx], c='blue')
  plt.pause(0.0001)
  for nl in range(0, len(ecc)):
    plt.gca().collections[-1].remove()

plt.title(str(round(arr[-1],2)) + " years")
plt.scatter(pls[0][-1], work[0][-1], c='red')
plt.scatter(pls[1][-1], work[1][-1], c='orange')
plt.scatter(pls[2][-1], work[2][-1], c='grey')
plt.scatter(pls[3][-1], work[3][-1], c='blue')


plt.show()
