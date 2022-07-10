import numpy as np
import matplotlib.pyplot as plt
import mpmath as mp
import scipy

data = np.loadtxt('5_7.dat', dtype='double')
NUM = len(data)
A = np.linspace(0, 10, 41)
p_e_0 = data[:, 0]
p_e_1 = data[:, 1]
p_e = 0.5 * p_e_0 + 0.5 * p_e_1

def Q_function(x):
    return 0.5 * mp.erfc(x/(2**0.5))

vec_p_e = scipy.vectorize(Q_function, otypes=[float])

plt.plot(A, p_e, 'o', label='Empirical')
plt.plot(A, vec_p_e(A), label='Theoretical')
plt.grid()
plt.legend()
plt.xlabel('$A$')
plt.ylabel('$P_e$')
plt.savefig('5.7.png')
plt.show()