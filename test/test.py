from src import utility as util
from src import boundary as op


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


def test_matrix_to_boundary_operation():
    image = util.convert_image_to_nparray("/home/utku/cartken/images/test_image_20.jpg")
    binary_map = util.rgb_to_binary(image)
    op.binary_matrix_to_boundaries(binary_map)
    rgb_map = util.binary_to_rgb(binary_map)
    util.create_image_from_nparray(rgb_map, "images/boundary_test.jpg", True)


if __name__ == "__main__":
    img = test_open_image()
    test_save_image(img)
    test_binary_map(img)
    test_matrix_to_boundary_operation()
