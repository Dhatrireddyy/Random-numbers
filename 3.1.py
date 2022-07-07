import numpy as np
import matplotlib.pyplot as plt

values = np.loadtxt('uni.dat', dtype='double')
NUM = len(values)
X1 = np.linspace(-2, 5, 30)
X2 = np.linspace(-2, 5, 100)
emp_cdf = []
the_cdf = []

for x in X1:
    count = 0
    for value in values:
        if value <= x:
            count += 1
    emp_cdf.append(count/NUM)

for x in X2:
    if x < 0:
        the_cdf.append(0)
    else:
        the_cdf.append(1 - np.exp(-0.5 * x))

plt.plot(X2, the_cdf, label='Theoretical')
plt.plot(X1, emp_cdf, 'o', label='Empirical')
plt.grid()
plt.legend()
plt.show()