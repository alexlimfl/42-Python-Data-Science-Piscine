from load_image import ft_load
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def ft_zoom(pixel_arr):
    """crops image from pixel array"""
    try:
        img = Image.fromarray(pixel_arr)
        width, height = img.size
        # print(width, height)
        crop_size = 400
        x_coor = 140
        y_coor = -85
        left = (width // 2 - crop_size//2) + x_coor
        top = (height // 2 - crop_size//2) + y_coor
        right = left + crop_size
        bottom = top + crop_size
        # print(left, top, right, bottom)
        img2 = img.crop((left, top, right, bottom))
        img2_arr = np.array(img2)
        return img2_arr
    except Exception as e:
        print("Error: ", str(e))
        return None


def main():
    """main"""
    pixel_arr = ft_load("animal.jpeg")
    if pixel_arr is None:
        return
    print(pixel_arr)
    img2_arr = ft_zoom(pixel_arr)
    if img2_arr is None:
        return
    img2 = Image.fromarray(img2_arr)
    img3 = img2.convert("L")
    img3_arr = np.array(img3)
    img3_shape2D = img3_arr.shape
    img3_arr_exp = np.expand_dims(img3_arr, axis=-1)
    img3_shape3D = img3_arr_exp.shape

    print(f"New shape after slicing: {img3_shape3D} or {img3_shape2D}")
    print(img3_arr_exp)
    plt.imshow(img3, cmap="gray")
    plt.show()


# 1024 768
# 262 134 762 634
# x_coor = 140
# y_coor = -85

if __name__ == "__main__":
    main()
