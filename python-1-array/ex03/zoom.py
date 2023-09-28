from load_image import ft_load
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt



def main():
    """zoom-in image"""
    pixel_arr = ft_load("animal.jpeg")
    img_shape = pixel_arr.shape
    img = Image.fromarray(pixel_arr)
    print(pixel_arr)
    print(img_shape)

    width, height = img.size
    print(width, height)

    crop_size = 400
    x_coor = 140
    y_coor = -85
    left = (width // 2 - crop_size//2) + x_coor
    top = (height // 2 - crop_size//2) + y_coor
    right = left + crop_size
    bottom = top + crop_size
    print(left, top, right, bottom)
    img2 = img.crop((left, top, right, bottom))
    img3 = img2.convert("L")
    # gray_s.show()
    # img2.show()
    plt.imshow(img3, cmap="gray")
    plt.show()


# 1024 768
# 262 134 762 634
# x_coor = 140
# y_coor = -85

if __name__ == "__main__":
    main()
