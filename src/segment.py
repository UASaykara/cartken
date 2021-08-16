class Segment:
    def __init__(self, x, y, pose, width):
        self.x = x
        self.y = y
        self.pose = pose
        self.width = width


def find_list_of_segment():
    pass


def find_longer_pose(binary_map, x, y):
    vertical = 0
    horizontal = 0
    # Right counter
    for i in range(x + 1, binary_map.shape[1]):
        if binary_map[i][y] == 1:
            vertical = vertical + 1
        else:
            break

    # Left counter
    for i in range(x - 1, -1, -1):
        if binary_map[i][y] == 1:
            vertical = vertical + 1
        else:
            break

    # Lower counter
    for i in range(y + 1, binary_map.shape[0]):
        if binary_map[x][i] == 1:
            horizontal = horizontal + 1
        else:
            break

    # Upper counter
    for i in range(y - 1, -1, -1):
        if binary_map[x][i] == 1:
            horizontal = horizontal + 1
        else:
            break

    if vertical >= horizontal:
        return "Vertical", vertical
    else:
        return "Horizontal", horizontal


def extract_segment():
    pass


def check_equal_parallel_segment():
    pass
