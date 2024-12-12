import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

filename = "./data/1_pima.csv"
column_names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = pd.read_csv(filename, names=column_names)
correlations = data.corr(method='pearson')
print(correlations)
correlations = data.corr(method='pearson')
correlations.to_csv("./results/correlation_coefficient.csv")

fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(correlations, cmap='coolwarm', vmin=-1, vmax=1)
fig.colorbar(cax)
ticks = np.arange(0,9,1)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_xticklabels(column_names)
ax.set_yticklabels(column_names)
for (i, j), value in np.ndenumerate(correlations):
	ax.text(j, i, f"{value:.2f}", ha="center", va="center", color="black")
plt.savefig("./results/correlation_plot.png")