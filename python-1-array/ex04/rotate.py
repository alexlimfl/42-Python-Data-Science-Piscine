from load_image import ft_load
from PIL import Image
import numpy as np
import sys
import matplotlib.pyplot as plt


def transpose(before):
    """transpose pixel_arr"""
    height, width, channel = before.shape
    print("1", height, width, channel)

    new = np.zeros((width, height, channel), dtype=np.uint8)
    print(before.shape, new.shape)
    # return after
    # print(before[767, 1023])
    print(range(height))
    print(range(width))
    for y in range(height):
        # print(y)
        # sys.exit(1)
        for x in range(width):
            new[x, y] = before[y, x]
    print("//////////////////")
    print(new)
    return new


def main():
    """main"""
    pixel_arr = ft_load("animal.jpeg")
    print(pixel_arr)
    pixel_arr = transpose(pixel_arr)
    img = Image.fromarray(pixel_arr)
    img.show()







if __name__ == "__main__":
    main()