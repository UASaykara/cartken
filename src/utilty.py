from PIL import Image
import numpy as np


def convert_image_to_nparray(file_name):
    return np.asarray(Image.open(file_name))


def create_image_from_nparray(array, file_name, is_rgb):
    if is_rgb:
        Image.fromarray(array, "RGB").save(file_name)
    else:
        Image.fromarray(array, "L").save(file_name)


def rgb_to_binary(array):
    binary_map = np.dot(array[..., :3], [0.2989, 0.5870, 0.1140])
    binary_map[binary_map < 128] = 1
    binary_map[binary_map >= 128] = 0
    return binary_map
