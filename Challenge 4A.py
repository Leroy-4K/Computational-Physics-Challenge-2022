import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import math
import time

fig = plt.figure(figsize = (6,6))
ax = plt.axes(projection='3d')
plt.xlabel("x/AU")
plt.ylabel("y/AU")
ax.set_zlabel("z/AU")
ax.text(-0.5, -1, 0.14, "Inner Planets 3D animation")
ax.text(-3.5, 0, 0.06, """Sun - yellow
Mercury - grey
Venus - orange
Earth - blue
Mars - red""", fontsize = 12, 
         bbox = dict(facecolor = 'red', alpha = 0.5))

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

beta = [1.85, 3.39, 7, 0]
# get degrees in radians
for er in range(len(beta)):
  beta[er] = beta[er] * math.pi/180

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


for i in range(0, len(ecc)):
  q = a[i] * (1 - (ecc[i]**2))
  j = q / (1 - (ecc[i] * np.cos(r)))
  x = j * np.cos(r) * math.cos(beta[i])
  y = j * np.sin(r)
  z = j * np.cos(r) * math.sin(beta[i])
  if i == 0:
    ax.plot3D(x, y, z, 'red')
  elif i == 1:
    ax.plot3D(x, y, z, 'orange')
  elif i == 2:
    ax.plot3D(x, y, z, 'grey')
  else:
    ax.plot3D(x, y, z, 'blue')
theta = 2 * math.pi
TIME = 0
time_step = p[3] * 20
x_list = []
y_list = []
z_list = []
pls = []

work = []

zzz = []
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
    x_list.append(j * math.cos((theta * xd * time_step) / p[i]) * math.cos(beta[i]))
    y_list.append(j * math.sin((theta * xd * time_step) / p[i]))
    z_list.append(j * math.cos((theta * xd * time_step) / p[i]) * math.sin(beta[i]))
    ghj += 2
    qwe += 1
  pls.append(x_list)
  work.append(y_list)
  zzz.append(z_list)
  x_list = []
  y_list = []
  z_list = []




#start=time.time()
#timer.add_callback(update_title, ax, start)
#timer.start()
ax.scatter3D(0, 0, 0, c='yellow')
for bmx in range(qwe-1):
  plt.title(str(round(arr[bmx],2)) + " years")
  ax.scatter3D(pls[0][bmx], work[0][bmx], zzz[0][bmx], c='red')
  ax.scatter3D(pls[1][bmx], work[1][bmx], zzz[1][bmx], c='orange')
  ax.scatter3D(pls[2][bmx], work[2][bmx], zzz[2][bmx], c='grey')
  ax.scatter3D(pls[3][bmx], work[3][bmx], zzz[3][bmx], c='blue')
  plt.pause(0.0001)
  for nl in range(0, len(ecc)):
    plt.gca().collections[-1].remove()

plt.title(str(round(arr[-1],2)) + " years")
ax.scatter3D(pls[0][-1], work[0][-1], zzz[0][-1], c='red')
ax.scatter3D(pls[1][-1], work[1][-1], zzz[1][-1], c='orange')
ax.scatter3D(pls[2][-1], work[2][-1], zzz[2][-1], c='grey')
ax.scatter3D(pls[3][-1], work[3][-1], zzz[3][-1], c='blue')

plt.show()