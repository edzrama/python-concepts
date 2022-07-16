#  Dot Product
import numpy as np
a = np.array([1, 2])
b = np.array([3, 4])
dot = 0

for e, f in zip(a, b):
    dot += e * f
print(dot)


dot = 0
for i in range(len(a)):
    dot += a[i] * b[i]
print(dot)

# this
print((a * b).sum())
# is same as
print(np.dot(a, b))
# or
print(a.dot(b))
# or
print(a @ b)
