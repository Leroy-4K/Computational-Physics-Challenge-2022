import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import math
import time


inner_planets = ["Mercury", "Venus", "Earth", "Mars"]
outer_planets = ["Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]
inner_a = [0.387, 0.723, 1.00, 1.523]
inner_ecc = [0.21, 0.01, 0.02, 0.09]
inner_mass = [0.055, 0.815, 1, 0.107]

earth_mass = 5.9722 * ((10)**(24))

for v in range(len(inner_mass)):
  inner_mass[v] = inner_mass[v] * earth_mass

sun_mass = 1.9891 * ((10)**(30))
inner_p = []
G = (6.67) * ((10)**(-11))
for v in range(len(inner_mass)):
  inner_p.append(
    ((inner_a[v]**3) * (4 * (math.pi**2)) / ((G) * (sun_mass + inner_mass[v])))**(1 / 2))
outer_a = [5.2, 9.58, 19.29, 30.25, 39.51]
outer_ecc = [0.05, 0.06, 0.05, 0.01, 0.25]
outer_mass = [317.85, 95.16, 14.5, 17.2, 0.00]
outer_p = []
for v in range(len(outer_mass)):
  outer_p.append(
    ((outer_a[v]**3) * (4 * (math.pi**2)) / ((G) * (sun_mass + outer_mass[v])))**(1 / 2))

with st.sidebar:
    g = st.radio(
        "Choose a page",
        ("Inner Planets", "Outer Planets")
    )
theta = 2 * math.pi
time_step = inner_p[2]
if g == "Outer Planets":
  option = st.selectbox('Which entity do you want at the centre',("Sun", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"))
  nt = st.text_input("Enter years of sim", "1000")
  nt = int(nt)
  fig, ax = plt.subplots()
  plt.xlabel("x/AU")
  plt.ylabel("y/AU")
  x_list = []
  y_list = []

  pls = []
  
  work = []
  ng = nt *30 + 1
  arr = []
  for i in range(0, len(outer_ecc)):
    ghj = 1
    qwe = 0
    while ghj < ng:
      xd = ghj/30
      arr.append(xd)
      q = outer_a[i] * (1 - (outer_ecc[i]**2))
      j = q / (1 - (outer_ecc[i] * math.cos((theta * xd * time_step) / outer_p[i])))
      x_list.append(j * math.cos((theta * xd * time_step) / outer_p[i]))
      y_list.append(j * math.sin((theta * xd * time_step) / outer_p[i]))
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
  sun_x = []
  sun_y = []
  jup_x = []
  jup_y = []
  sat_x = []
  sat_y = []
  ur_x = []
  ur_y = []
  nep_x = []
  nep_y = []
  plu_x = []
  plu_y = []
  fig, ax = plt.subplots()
  if option == "Sun":
    pl_x = pls[5]
    pl_y = work[5]
    ax.scatter(0,0,c='yellow')
  if option == "Jupiter":
    pl_x = pls[0]
    pl_y = work[0]
    ax.scatter(0,0,c='red')
  elif option == "Saturn":
    pl_x = pls[1]
    pl_y = work[1]
    ax.scatter(0,0,c='orange')
  elif option == "Uranus":
    pl_x = pls[2]
    pl_y = work[2]
    ax.scatter(0,0,c='grey')
  elif option == "Neptune":
    pl_x = pls[3]
    pl_y = work[3]
    ax.scatter(0,0,c='blue')
  elif option == "Pluto":
    pl_x = pls[4]
    pl_y = work[4]
    ax.scatter(0,0,c='grey')    
  plt.xlabel("x/AU")
  plt.ylabel("y/AU")
  for gh in range(len(pls[0])):
    ur_x.append(pls[2][gh]-pl_x[gh])
    ur_y.append(work[2][gh] - pl_y[gh])
    jup_x.append(pls[0][gh]-pl_x[gh])
    jup_y.append(work[0][gh]-pl_y[gh])
    sun_x.append(pls[5][gh]-pl_x[gh])
    sun_y.append(work[5][gh]-pl_y[gh])
    sat_x.append(pls[1][gh]-pl_x[gh])
    sat_y.append(work[1][gh]-pl_y[gh])
    nep_x.append(pls[3][gh]-pl_x[gh])
    nep_y.append(work[3][gh]-pl_y[gh])
    plu_x.append(pls[-2][gh]-pl_x[gh])
    plu_y.append(work[-2][gh]-pl_y[gh])
  ax.plot(jup_x,jup_y,'red')
  ax.plot(sun_x, sun_y, 'yellow')
  ax.plot(sat_x, sat_y, 'orange')
  ax.plot(ur_x, ur_y, 'green')
  ax.plot(nep_x, nep_y, 'blue')
  ax.plot(plu_x, plu_y, 'grey')
  plt.title("Orbits around " + option + " for " + str(round(arr[-1],2)) + " years")
  st.pyplot(fig)





  
elif g == "Inner Planets":
  option = st.selectbox('Which entity do you want at the centre',('Sun', 'Mercury', 'Venus', 'Earth', 'Mars'))
  nt = st.text_input("Enter years of sim", "16")
  nt = int(nt)
  fig, ax = plt.subplots()
  plt.xlabel("x/AU")
  plt.ylabel("y/AU")
  x_list = []
  y_list = []
  
  pls = []
  
  work = []
  ng = nt * 250 + 1
  arr = []
  for i in range(0, len(inner_ecc)):
    ghj = 1
    qwe = 0
    while ghj < ng:
      xd = ghj/250
      arr.append(xd)
      q = inner_a[i] * (1 - (inner_ecc[i]**2))
      j = q / (1 - (inner_ecc[i] * math.cos((theta * xd * time_step) / inner_p[i])))
      x_list.append(j * math.cos((theta * xd * time_step) / inner_p[i]))
      y_list.append(j * math.sin((theta * xd * time_step) / inner_p[i]))
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
  earth_x = []
  earth_y = []
  merc_x = []
  merc_y = []
  sun_x = []
  sun_y = []
  venus_x = []
  venus_y = []
  mars_x = []
  mars_y = []
  fig, ax = plt.subplots()
  if option == "Sun":
    pl_x = pls[4]
    pl_y = work[4]
    ax.scatter(0,0,c='yellow')
  if option == "Earth":
    pl_x = pls[2]
    pl_y = work[2]
    ax.scatter(0,0,c='blue')
  elif option == "Mercury":
    pl_x = pls[0]
    pl_y = work[0]
    ax.scatter(0,0,c='grey')
  elif option == "Venus":
    pl_x = pls[1]
    pl_y = work[1]
    ax.scatter(0,0,c='orange')
  elif option == "Mars":
    pl_x = pls[3]
    pl_y = work[3]
    ax.scatter(0,0,c='red')
  plt.xlabel("x/AU")
  plt.ylabel("y/AU")
  for gh in range(len(pls[0])):
    earth_x.append(pls[2][gh]-pl_x[gh])
    earth_y.append(work[2][gh] - pl_y[gh])
    merc_x.append(pls[0][gh]-pl_x[gh])
    merc_y.append(work[0][gh]-pl_y[gh])
    sun_x.append(pls[-1][gh]-pl_x[gh])
    sun_y.append(work[-1][gh]-pl_y[gh])
    venus_x.append(pls[1][gh]-pl_x[gh])
    venus_y.append(work[1][gh]-pl_y[gh])
    mars_x.append(pls[3][gh]-pl_x[gh])
    mars_y.append(work[3][gh]-pl_y[gh])
  ax.plot(merc_x,merc_y,'grey')
  ax.plot(sun_x, sun_y, 'yellow')
  ax.plot(venus_x, venus_y, 'orange')
  ax.plot(mars_x, mars_y, 'red')
  ax.plot(earth_x, earth_y, 'blue')
  plt.title("Orbits around " + option + " for " + str(round(arr[-1],2)) + " years")
  st.pyplot(fig)
