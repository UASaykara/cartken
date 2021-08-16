from src import utility as util
from src import boundary as op
from src import segment as seg


def test_open_image():
    image = util.convert_image_to_nparray("/test/test_cases/3.png")
    print("Image type: ", type(image))
    print("Image shape: ", image.shape)
    return image


def test_save_image(image):
    util.create_image_from_nparray(image, "/test/test_cases/3_new.png", True)


def test_binary_map(image):
    binary_map = util.rgb_to_binary(image)
    print("Binary type: ", type(binary_map))
    print("Binary shape: ", binary_map.shape)
    print(binary_map)


def test_matrix_to_boundary_operation():
    image = util.convert_image_to_nparray("/test/test_cases/test_image_20.jpg")
    binary_map = util.rgb_to_binary(image)
    op.binary_matrix_to_boundaries(binary_map)
    rgb_map = util.binary_to_rgb(binary_map)
    util.create_image_from_nparray(rgb_map, "/test/test_cases/boundary_test.png", True)


def test_find_longer_pose():
    image = util.convert_image_to_nparray("/test/test_cases/boundary_test.png")
    binary_map = util.rgb_to_binary(image)
    print(seg.find_longer_pose(binary_map, 1, 0))


def test_segment_finder():
    image = util.convert_image_to_nparray("/test/test_cases/boundary_test.png")
    binary_map = util.rgb_to_binary(image)
    seg.find_list_of_segment(binary_map)


def test_segment_rgb():
    image = util.convert_image_to_nparray("/test/test_cases/boundary_test.png")
    binary_map = util.rgb_to_binary(image)
    list = seg.find_list_of_segment(binary_map)
    rgb_map = util.construct_segment_map(list, binary_map.shape[0], binary_map.shape[1])
    util.create_image_from_nparray(rgb_map, "/test/test_cases/segment_test.png", True)


def test_segment_file_list():
    image = util.convert_image_to_nparray("/test/test_cases/boundary_test.png")
    binary_map = util.rgb_to_binary(image)
    list = seg.find_list_of_segment(binary_map)
    util.segment_list_to_file(list, "/test/test_cases/segment_list")


if __name__ == "__main__":
    img = test_open_image()
    test_save_image(img)
    test_binary_map(img)
    test_matrix_to_boundary_operation()
    test_find_longer_pose()
    test_segment_finder()
    test_segment_rgb()
    test_segment_file_list()