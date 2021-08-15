from PIL import Image
import numpy as np


def convert_image_to_nparray(file_name):
    return np.asarray(Image.open(file_name))

