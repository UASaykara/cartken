from PIL import Image
import numpy as np


def convert_image_to_nparray(file_name):
    return np.asarray(Image.open(file_name))


def create_image_from_nparray(array, file_name, is_rgb):
    if is_rgb:
        Image.fromarray(array, "RGB").save(file_name)
    else:
        Image.fromarray(array, "L").save(file_name)