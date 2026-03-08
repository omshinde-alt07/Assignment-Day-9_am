def matrix_add(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        print("Matrix dimensions must match for addition.")
        return None

    result = [
        [A[i][j] + B[i][j] for j in range(len(A[0]))]
        for i in range(len(A))
    ]

    return result

def matrix_transpose(matrix):
    return [list(row) for row in zip(*matrix)]


def matrix_multiply(A, B):
    if len(A[0]) != len(B):
        print("Matrix multiplication not possible due to dimension mismatch.")
        return None

    result = [
        [
            sum(a * b for a, b in zip(row_a, col_b))
            for col_b in zip(*B)
        ]
        for row_a in A
    ]

    return result


if __name__ == "__main__":


    a = [[1, 2], [3, 4]]
    b = [[5, 6], [7, 8]]

    print("Matrix Addition:")
    print(matrix_add(a, b))

    print("\nMatrix Transpose:")
    print(matrix_transpose(a))

    print("\nMatrix Multiplication:")
    print(matrix_multiply(a, b))


    c = [[1, 2, 3],
         [4, 5, 6]]

    d = [[7, 8],
         [9, 10],
         [11, 12]]

    print("\nSecond Test Case:")

    print("\nMatrix Multiplication:")
    print(matrix_multiply(c, d))