def binary_matrix_to_boundaries(binary_map):
    for i in range(binary_map.shape[0]):
        for j in range(binary_map.shape[1]):
            if binary_map[i][j] == 0:
                if is_boundary(i, j, binary_map):
                    binary_map[i][j] = 2
    binary_map[binary_map == 1] = 0
    binary_map[binary_map == 2] = 1


def is_boundary(i, j, b_map):
    if j + 1 < b_map.shape[1]:
        if b_map[i][j + 1] == 1:  # Checking Right
            return True
        elif i - 1 >= 0 and b_map[i - 1][j + 1] == 1:  # Checking Upper Right
            return True
        elif i + 1 < b_map.shape[0] and b_map[i + 1][j + 1] == 1:  # Checking Lower Right
            return True

    if j - 1 >= 0:
        if b_map[i][j - 1] == 1:  # Checking Left
            return True
        elif i - 1 >= 0 and b_map[i - 1][j - 1] == 1:  # Checking Upper Left
            return True
        elif i + 1 < b_map.shape[0] and b_map[i + 1][j - 1] == 1:  # Checking Lower Left
            return True

    if i + 1 < b_map.shape[0] and b_map[i + 1][j] == 1:  # Checking Lower
        return True

    if i - 1 >= 0 and b_map[i - 1][j] == 1:  # Checking Upper
        return True

    return False

