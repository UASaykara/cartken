from src import utility as util
from src import boundary as op
from src import segment as seg
import unittest


class TestStringMethods(unittest.TestCase):
    def test_open_image(self):
        image = util.convert_image_to_nparray("/test_cases/3.png")
        self.assertEqual(image.shape, (3, 3, 3))

    def test_save_image(self):
        image = util.convert_image_to_nparray("/test_cases/3_new.png")
        util.create_image_from_nparray(image, "/test_cases/3_new.png", True)
        image = util.convert_image_to_nparray("/test_cases/3_new.png")
        self.assertEqual(image.shape, (3, 3, 3))

    def test_binary_map(self):
        image = util.convert_image_to_nparray("/test_cases/3_new.png")
        binary_map = util.rgb_to_binary(image)
        self.assertEqual(binary_map.shape, (3, 3))

    def test_matrix_to_boundary_operation(self):
        image = util.convert_image_to_nparray("/test_cases/test_image_20.jpg")
        binary_map = util.rgb_to_binary(image)
        op.binary_matrix_to_boundaries(binary_map)
        rgb_map = util.binary_to_rgb(binary_map)
        self.assertEqual(rgb_map.shape, (20, 20, 3))

    def test_find_longer_pose(self):
        image = util.convert_image_to_nparray("/test_cases/boundary_test.png")
        binary_map = util.rgb_to_binary(image)
        pose, count = seg.find_longer_pose(binary_map, 1, 0)
        self.assertEqual(count, 20)
        self.assertEqual(pose, "Vertical")

    def test_segment_finder(self):
        image = util.convert_image_to_nparray("/test_cases/boundary_test.png")
        binary_map = util.rgb_to_binary(image)
        segment_list = seg.find_list_of_segment(binary_map)
        self.assertEqual(len(segment_list), 14)

    def test_segment_rgb(self):
        image = util.convert_image_to_nparray("/test_cases/boundary_test.png")
        binary_map = util.rgb_to_binary(image)
        segment_list = seg.find_list_of_segment(binary_map)
        rgb_map = util.construct_segment_map(segment_list, binary_map.shape[0], binary_map.shape[1])
        self.assertEqual(rgb_map.shape, (binary_map.shape[0], binary_map.shape[1], 3))

    def test_segment_file_list(self):
        image = util.convert_image_to_nparray("/test_cases/boundary_test.png")
        binary_map = util.rgb_to_binary(image)
        segment_list = seg.find_list_of_segment(binary_map)
        self.assertTrue(util.segment_list_to_file(segment_list, "/test_cases/segment_list"))


if __name__ == "__main__":
    unittest.main()
