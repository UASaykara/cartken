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


def binary_to_grayscale(map):
    map[map == 0] = 255
    map[map == 1] = 0
    return map


def binary_to_rgb(map):
    rgb_map = np.zeros((map.shape[0], map.shape[1], 3), dtype=np.uint8)
    for i in range(map.shape[0]):
        for j in range(map.shape[1]):
            if map[i][j] == 0:
                rgb_map[i][j] = (255, 255, 255)
            else:
                rgb_map[i][j] = (0, 0, 0)
    return rgb_map

