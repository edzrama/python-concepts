import numpy as np
from matplotlib import pyplot as plt

x = np.random.randn(10000)
# x = np.random.rand(10000)

# plt.hist(x)
plt.hist(x, bins=50)
plt.show()