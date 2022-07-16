import numpy as np
from matplotlib import pyplot as plt

# x = np.random.rand(100, 2)
# plt.scatter(x[:, 0], x[:, 1])
# plt.show()

x = np.random.randn(200, 2)
x[:50] += 3
y = np.zeros(200)
y[:50] = 1
plt.scatter(x[:, 0], x[:, 1], c=y)
plt.show()
