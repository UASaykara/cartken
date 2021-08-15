from src import utilty as util
import numpy as np


def test_open_image():
    image = util.convert_image_to_nparray("/home/utku/Documents/3.png")
    print("Image type: ", type(image))
    print("Image shape: ", image.shape)
    return image


def test_save_image(image):
    util.create_image_from_nparray(image, "/home/utku/Documents/3_new.png", True)


def test_binary_map(image):
    binary_map = util.rgb_to_binary(image)
    print("Binary type: ", type(binary_map))
    print("Binary shape: ", binary_map.shape)
    print(binary_map)


if __name__ == "__main__":
    img = test_open_image()
    test_save_image(img)
    test_binary_map(img)