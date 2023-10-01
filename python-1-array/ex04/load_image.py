from PIL import Image
import numpy as np


def ft_load(path: str) -> list:
    """loads image"""
    try:
        img = Image.open(path)
    except Exception as e:
        print("Error: ", str(e))
        return []
    # img_format = img.format
    pixels_arr = np.array(img)
    # img.show()
    # print(f"The image format is: {img_format}")
    print("The shape of the image is:", pixels_arr.shape)
    return pixels_arr
