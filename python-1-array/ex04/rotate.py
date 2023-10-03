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


def ft_transpose(before):
    """transpose pixel_arr"""
    try:
        height, width = before.shape
        new = np.zeros((width, height), dtype=np.uint8)
        # print(before.shape, new.shape)
        # print(before[767, 1023])
        # print(range(height))
        # print(range(width))
        for y in range(height):
            for x in range(width):
                new[x, y] = before[y, x]
        return new
    except Exception as e:
        print("Error: ", str(e))
        return None


def main():
    """main"""
    pixel_arr = ft_load("animal.jpeg")
    if pixel_arr is None:
        return
    pixel_arr = ft_zoom(pixel_arr)
    if pixel_arr is None:
        return
    img = Image.fromarray(pixel_arr)
    img_gscale = img.convert("L")
    img_gscale_arr = np.array(img_gscale)
    img_gscale_arr_exp = np.expand_dims(img_gscale_arr, axis=-1)
    a = img_gscale_arr_exp.shape
    b = img_gscale_arr.shape
    print(f"The shape of the image is: {a} or {b}")
    print(img_gscale_arr_exp)
    img_gscale_arr_t = ft_transpose(img_gscale_arr)
    if img_gscale_arr_t is None:
        return
    print(f"New shape after Transpose: {img_gscale_arr_t.shape}")
    print(img_gscale_arr_t)
    img_gscale_t = Image.fromarray(img_gscale_arr_t)
    plt.imshow(img_gscale_t, cmap="gray")
    plt.show()


if __name__ == "__main__":
    main()
