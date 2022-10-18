import numpy as np
import matplotlib.pyplot as plt

def zero_pot(x):
	return x**x

x = np.linspace(0,1,10000)
y = []
for i in range(len(x)):
	y.append(zero_pot(x[i]))

fig, ax = plt.subplots(1,1, figsize=(15,15), dpi=80)
ax.scatter(x,y, marker='o', color='blue')
fig.show()