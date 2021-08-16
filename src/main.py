import os
from src import utility as util
from src import boundary as op
from src import segment as seg
from datetime import datetime


def main():
    image_path = input("Enter image name inside image folder with extension (Ex. image.jpg): ")
    print("Boundaries are extracting...", end="\n")
    now = str(datetime.now())
    os.mkdir(os.getcwd() + "/results/" + now)
    binary_map = util.rgb_to_binary(util.convert_image_to_nparray("/images/" + image_path))
    op.binary_matrix_to_boundaries(binary_map)
    util.create_image_from_nparray(util.binary_to_rgb(binary_map), "/results/" + now + "/boundary_map.png", True)
    print("Boundaries extracted!", end="\n")
    print("Segments are creating...", end="\n")
    segment_list = seg.find_list_of_segment(binary_map)
    util.segment_list_to_file(segment_list, "/results/" + now + "/segmentation_list")
    print("Segment text file created.", end="\n")
    rgb_map = util.construct_segment_map(segment_list, binary_map.shape[0], binary_map.shape[1])
    util.create_image_from_nparray(rgb_map, "/results/" + now + "/segmentation_map.png", True)
    print("Segmentation map created.", end="\n")
    print("Boundary segments created!", end="\n")
    print("Results are inside [/results/" + now + " file.]" , end="\n")


if __name__ == "__main__":
    main()
