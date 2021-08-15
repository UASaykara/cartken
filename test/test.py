from src import utilty as util


def test_open_image():
    image = util.convert_image_to_nparray("/home/utku/Documents/3.png")
    print("Image type: ", type(image))
    print("Image shape: ", image.shape)


if __name__ == "__main__":
    test_open_image()