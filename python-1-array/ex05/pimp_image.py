from PIL import Image
import numpy as np


def ft_invert(array):
    """inverts the color of the image received"""
    try:
        invert = 255 - array
        img = Image.fromarray(invert)
        img.show()
        return invert
    except Exception as e:
        print("Error: ", str(e))
        return None


def ft_red(array):
    """converts img to redscale"""
    try:
        img_R = array.copy()
        img_R[:, :, (1, 2)] = 0
        img = Image.fromarray(img_R)
        img.show()
        return img_R
    except Exception as e:
        print("Error: ", str(e))
        return None


def ft_green(array):
    """converts img to greenscale"""
    try:
        img_G = array.copy()
        img_G[:, :, (0, 2)] = 0
        img = Image.fromarray(img_G)
        img.show()
        return img_G
    except Exception as e:
        print("Error: ", str(e))
        return None


def ft_blue(array):
    """converts img to bluescale"""
    try:
        img_B = array.copy()
        img_B[:, :, (0, 1)] = 0
        img = Image.fromarray(img_B)
        img.show()
        return img_B
    except Exception as e:
        print("Error: ", str(e))
        return None


def ft_grey(array):
    """converts img to greyscale"""
    try:
        gray_img = array.copy()
        gray_img = np.mean(gray_img, axis=2).astype(np.uint8)
        img = Image.fromarray(gray_img)
        img.show()
        return gray_img
    except Exception as e:
        print("Error: ", str(e))
        return None
