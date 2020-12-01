# STAGE 1 (my PRIME solution!)
def matrix_size():
    dimension = input().split()
    m, n = [int(num) for num in dimension]
    return m, n


def creating_matrix(m):
    # creating a boilerplate for our matrix
    matrix = [[] for _ in range(m)]
    # filling the matrix with numbers
    for row in matrix:
        row_string = input().split()
        row_int = [int(num) for num in row_string]  # converting str to int data type
        row.extend(row_int)
    return matrix


# printing the matrix
def print_matrix(matrix):
    for row in matrix:
        print(*row, sep=' ')


# sum matrices
def sum_matrix(matrix_1, matrix_2):
    # summing elements of two matrices
    sum_m = []
    m = len(matrix_1)
    n = len(matrix_1[0])
    for i in range(m):
        for j in range(n):
            sum_m.append(matrix_1[i][j] + matrix_2[i][j])

    # forming the output matrix
    matrix_result = []
    start = 0
    end = n
    for k in range(m):
        matrix_result.append(sum_m[start:end])
        start += n
        end += n

    return matrix_result


# running the script
def main(number_of_matrices):
    matrices = []
    while number_of_matrices > 0:
        m, n = matrix_size()
        matrix = creating_matrix(m)
        matrices.append(matrix)
        number_of_matrices -= 1

    if len(matrices[0]) != len(matrices[1]) and len(matrices[0][0]) != len(matrices[1][0]):
        print('ERROR')
    else:
        result = sum_matrix(matrices[0], matrices[1])
        print_matrix(result)


main(2)


# STAGE 2
