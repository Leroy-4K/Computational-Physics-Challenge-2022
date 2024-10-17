import numpy as np
import matplotlib.pyplot as plt
import math
import time


TIME = 0



a = [0.723, 1.00]
ecc = [0.01, 0.02]

mass = [0.815, 1]

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
ax.text(-0.4, 1.32, "Earth and Venus spirograph")
plt.xlabel("x/AU")
plt.ylabel("y/AU")
plt.text(0.75, 1, """Venus - orange
Earth - blue""", fontsize = 12, bbox = dict(facecolor = 'red', alpha = 0.5))

for i in range(0, len(ecc)):
  q = a[i] * (1 - (ecc[i]**2))
  j = q / (1 - (ecc[i] * np.cos(r)))
  x = j * np.cos(r)
  y = j * np.sin(r)
  if i == 0:
    ax.plot(x, y, 'orange')
  else:
    ax.plot(x, y, 'blue')
theta = 2 * math.pi
TIME = 0
time_step = p[1] * 3
x_list = []
y_list = []

pls = []

work = []
ng = 834
#timer = fig.canvas.new_timer(interval=100)
arr = []
for i in range(0, len(ecc)):
  ghj = 1
  qwe = 0
  while ghj < ng:
    xd = ghj/250
    arr.append(xd*3)
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
x_line = []
y_line = []
for bmx in range(qwe-1):
  plt.title(str(round(arr[bmx],2)) + " years")
  x_line.append(pls[0][bmx])
  x_line.append(pls[1][bmx])
  y_line.append(work[0][bmx])
  y_line.append(work[1][bmx])
  ax.plot(x_line,y_line, 'grey')
  plt.scatter(pls[0][bmx], work[0][bmx], c='orange')
  plt.scatter(pls[1][bmx], work[1][bmx], c='blue')
  x_line = []
  y_line = []
  for nl in range(0, len(ecc)):
    plt.gca().collections[-1].remove()

plt.title(str(round(arr[-1],2)) + " years")
plt.scatter(pls[0][-1], work[0][-1], c='orange')
plt.scatter(pls[1][-1], work[1][-1], c='blue')


plt.show()
