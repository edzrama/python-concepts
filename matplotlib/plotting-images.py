import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

# im = Image.open("pikachu.png")
im = Image.open("lena.png")
# print(type(im))

arr = np.array(im)
# print(arr)
# print(arr.shape)

# plt.imshow(arr)
# plt.show()

gray = arr.mean(axis=2)
print(gray.shape)

# plt.imshow(gray)
plt.imshow(gray, cmap='gray')
plt.show()
