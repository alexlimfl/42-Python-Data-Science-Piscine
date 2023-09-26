from load_image import ft_load
from PIL import Image
import numpy as np


def main():
    """zoom-in image"""
    pixel_arr = ft_load("animal.jpeg")
    img_shape = pixel_arr.shape
    img = Image.fromarray(pixel_arr)
    print(pixel_arr)
    print(img_shape)
    # resized_img = img.resize(5,5)
    zoom_factor = 0.5
    # resized_img.show()

if __name__ == "__main__":
    main()
