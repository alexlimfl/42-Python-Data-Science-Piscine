from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img = np.array(Image.open('landscape.jpg'))
img_R, img_G, img_B = img.copy(), img.copy(), img.copy()
img_R[:, :, (1, 2)] = 0
img_G[:, :, (0, 2)] = 0
img_B[:, :, (0, 1)] = 0
img_rgb = np.concatenate((img_R, img_G, img_B), axis=1)
plt.figure(figsize=(15, 15))
plt.imshow(img_rgb)
plt.show()


iR = Image.fromarray(img_R)
iG = Image.fromarray(img_G)
iB = Image.fromarray(img_B)
iR.show()
iG.show()
iB.show()
