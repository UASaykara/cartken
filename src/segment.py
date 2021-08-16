class Segment:
    def __init__(self, x, y, pose, length):
        self.x = x
        self.y = y
        self.pose = pose
        self.length = length


def find_list_of_segment(binary_map):
    segment_list = []
    for i in range(binary_map.shape[0]):
        for j in range(binary_map.shape[1]):
            if binary_map[i][j] == 1:
                pose, length = find_longer_pose(binary_map, i, j)
                # Create a segment
                segment = Segment(x=i, y=j, pose=pose, length=length)
                extract_segment(binary_map, segment)
                segment_list.append(segment)
    return segment_list


def find_longer_pose(binary_map, x, y):
    vertical = 0
    horizontal = 0
    # Lower counter
    for i in range(x + 1, binary_map.shape[1]):
        if binary_map[i][y] == 1:
            vertical = vertical + 1
        else:
            break

    # Upper counter
    for i in range(x, -1, -1):
        if binary_map[i][y] == 1:
            vertical = vertical + 1
        else:
            break

    # Right counter
    for i in range(y + 1, binary_map.shape[0]):
        if binary_map[x][i] == 1:
            horizontal = horizontal + 1
        else:
            break

    # Left counter
    for i in range(y, -1, -1):
        if binary_map[x][i] == 1:
            horizontal = horizontal + 1
        else:
            break

    if vertical >= horizontal:
        return "Vertical", vertical
    else:
        return "Horizontal", horizontal


def extract_segment(binary_map, segment):
    if segment.pose == "Horizontal":
        for i in range(segment.y, segment.y + segment.length):
            binary_map[segment.x][i] = 0
    else:
        for i in range(segment.x, segment.x + segment.length):
            binary_map[i][segment.y] = 0


def check_equal_parallel_segment():
    pass

