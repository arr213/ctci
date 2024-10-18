def rotate_matrix(matrix):
    n = len(matrix)
    for layer in range(n // 2):
        print("Layer: ", layer, n)
        first = layer
        last = n - 1 - layer
        for i in range(first, last):
            offset = i - first
            top = matrix[first][i]
            matrix[first][i] = matrix[last - offset][first]
            matrix[last - offset][first] = matrix[last][last - offset]
            matrix[last][last - offset] = matrix[i][last]
            matrix[i][last] = top
    return matrix


# Example usage:
if __name__ == "__main__":
    print(rotate_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    # Output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]