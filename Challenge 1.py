import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
df = pd.DataFrame()
x = np.array([9.58,
19.29,
5.2,
30.25,
39.51,
1.523,
0.723,
0.387,
1])

x = x ** (3/2)
df['a^3/2'] = x
y = [29.43,
84.75,
11.86,
166.34,
248.35,
1.88,
0.62,
0.24,
1]
df['T/Yr'] = y
fig, ax = plt.subplots()
plt.title("Kepler's Third Law")
plt.xlabel("(a/AU)^(3/2)")
plt.ylabel("T/yr")
ax.scatter(x,y,marker='+')
f = np.linspace(0.0,250,10)
g = np.linspace(0.0,250,10)
ax.plot(f,g, c='red')
plt.show()