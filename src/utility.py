from PIL import Image
import numpy as np
from random import randint
import os


def convert_image_to_nparray(file_name):
    return np.asarray(Image.open(os.getcwd() + file_name))


def create_image_from_nparray(array, file_name, is_rgb):
    if is_rgb:
        Image.fromarray(np.uint8(array)).save(os.getcwd() + file_name)
    else:
        Image.fromarray(array, "L").save(os.getcwd() + file_name)


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


def construct_segment_map(segment_list, x, y):
    rgb_map = np.full((x, y, 3), fill_value=255, dtype=np.uint8)
    for segment in segment_list:
        new_color = (randint(0, 128), randint(0, 128), randint(0, 128))
        if segment.pose == "Horizontal":
            for i in range(segment.y, segment.y + segment.length):
                rgb_map[segment.x][i] = new_color
        else:
            for i in range(segment.x, segment.x + segment.length):
                rgb_map[i][segment.y] = new_color
    return rgb_map


def segment_list_to_file(segment_list, file_name):
    counter = 1
    file = open(os.path.abspath(os.getcwd()) + file_name + ".txt", "w")
    file.write("Segmentation List:\n")
    for segment in segment_list:
        file.write(str(counter) + ": X= " + str(segment.x) + " | Y= " + str(segment.y) + " | Pose= " + segment.pose + " | Length= " + str(segment.length) + "\n")
        counter = counter + 1
    file.close()
    return True


