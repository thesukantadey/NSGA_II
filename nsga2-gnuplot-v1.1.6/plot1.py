import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('plot.out','r') as csvfile:
    plots = csv.reader(csvfile, delimiter='	')
    for row in plots:
        x.append(float(row[0]))
        y.append(float(row[1]))

plt.scatter(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.savefig('pareto_py1.eps', format='eps', dpi=1000)
