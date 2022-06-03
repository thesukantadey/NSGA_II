import matplotlib.pyplot as plt
import numpy as np

x, y = np.loadtxt('plot.out', delimiter='	', unpack=True)
print(x)
plt.scatter(x,y, alpha=0.5, color='yellow', edgecolors='red', s=20)

plt.xlabel('Total metal area of subcircuit ($A_{subcircuit}$) in $\mu m^2$')
plt.ylabel('Total IR drop of subcircuit')
plt.title('Pareto plot')
plt.legend()
#ax.set_rasterized(True)
plt.savefig('pareto_py.eps', format='eps', dpi=1000)
