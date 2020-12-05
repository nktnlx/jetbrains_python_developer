# STAGE 1 (my PRIME solution!)
# def matrix_size():
#     dimension = input().split()
#     m, n = [int(num) for num in dimension]
#     return m, n
#
#
# def creating_matrix(m):
#     # creating a boilerplate for our matrix
#     matrix = [[] for _ in range(m)]
#     # filling the matrix with numbers
#     for row in matrix:
#         row_string = input().split()
#         row_int = [int(num) for num in row_string]  # converting str to int data type
#         row.extend(row_int)
#     return matrix
#
#
# # printing the matrix
# def print_matrix(matrix):
#     for row in matrix:
#         print(*row, sep=' ')
#
#
# # sum matrices
# def sum_matrix(matrix_1, matrix_2):
#     # summing elements of two matrices
#     sum_m = []
#     m = len(matrix_1)
#     n = len(matrix_1[0])
#     for i in range(m):
#         for j in range(n):
#             sum_m.append(matrix_1[i][j] + matrix_2[i][j])
#
#     # forming the output matrix
#     matrix_result = []
#     start = 0
#     end = n
#     for k in range(m):
#         matrix_result.append(sum_m[start:end])
#         start += n
#         end += n
#
#     return matrix_result
#
#
# # running the script
# def main(number_of_matrices):
#     matrices = []
#     while number_of_matrices > 0:
#         m, n = matrix_size()
#         matrix = creating_matrix(m)
#         matrices.append(matrix)
#         number_of_matrices -= 1
#
#     if len(matrices[0]) != len(matrices[1]) and len(matrices[0][0]) != len(matrices[1][0]):
#         print('ERROR')
#     else:
#         result = sum_matrix(matrices[0], matrices[1])
#         print_matrix(result)
#
#
# main(2)


# STAGE 2
# inputting matrix size
# def matrix_size():
#     dimension = input().split()
#     m, n = [int(num) for num in dimension]
#     return m, n
#
#
# def creating_matrix(m):
#     # creating a boilerplate for our matrix
#     matrix = [[] for _ in range(m)]
#     # filling the matrix with numbers
#     for row in matrix:
#         row_string = input().split()
#         row_int = [int(num) for num in row_string]  # converting str to int data type
#         row.extend(row_int)
#     return matrix
#
#
# # printing the matrix
# def print_matrix(matrix):
#     for row in matrix:
#         print(*row, sep=' ')
#
#
# # multiplication by number
# def mmult(matrix):
#     constant = int(input())
#
#     mult_m = []
#     m = len(matrix)
#     n = len(matrix[0])
#     for i in range(m):
#         for j in range(n):
#             mult_m.append(matrix[i][j] * constant)
#
#     # forming the output matrix
#     matrix_result = []
#     start = 0
#     end = n
#     for k in range(m):
#         matrix_result.append(mult_m[start:end])
#         start += n
#         end += n
#
#     return matrix_result
#
#
# # running the script
# def main():
#     m, n = matrix_size()
#     matrix = creating_matrix(m)
#     result = mmult(matrix)
#     print_matrix(result)
#
#
# main()


# STAGE 3
# menu of our matrix calculator
def menu():
    choice = input('''1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
0. Exit
Your choice: ''')
    return choice


# printing result (nested form of matrix with a result)
def print_matrix(matrix):
    print('The result is:')
    for row in matrix:
        print(*row, sep=' ')
    print('')


# matrix creation template
def creating_matrix(m):
    # creating a boilerplate for our matrix
    matrix = [[] for _ in range(m)]
    # filling the matrix with numbers
    for row in matrix:
        row_string = input().split()
        row_int = [float(num) for num in row_string]  # converting str to int data type
        row.extend(row_int)
    return matrix


# defining number of matrices, their size and creating them
def matrix_size(number_of_matrices):  # argument is number of matrices (integer)
    if number_of_matrices == 1:
        dimension = input('Enter size of matrix: ').split()
        m, n = [int(num) for num in dimension]
        print('Enter matrix:')
        return creating_matrix(m)

    elif number_of_matrices == 2:
        vocabulary = ['first', 'second']
        matrices = []
        while number_of_matrices > 0:
            dimension = input(f'Enter size of {vocabulary[number_of_matrices * -1]} matrix: ').split()
            m, n = [int(num) for num in dimension]
            print(f'Enter {vocabulary[number_of_matrices * -1]} matrix:')
            matrices.append(creating_matrix(m))
            number_of_matrices -= 1
        return matrices


# sum matrices
def sum_matrix(matrix_1, matrix_2):
    # summing elements of two matrices
    sum_m = []
    m = len(matrix_1)  # number of rows
    n = len(matrix_1[0])  # number of columns
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


# multiplication by constant
def mmult_c(matrix):
    constant = float(input('Enter constant: '))
    mult_m = []
    m = len(matrix)
    n = len(matrix[0])
    for i in range(m):
        for j in range(n):
            mult_m.append(matrix[i][j] * constant)
    # forming the output matrix
    matrix_result = []
    start = 0
    end = n
    for k in range(m):
        matrix_result.append(mult_m[start:end])
        start += n
        end += n
    return matrix_result


# matrix multiplication
def mmult(matrix_1, matrix_2):
    if len(matrix_1[0]) != len(matrix_2):
        print('The operation cannot be performed.\n')
    else:
        m = len(matrix_1)  # rows
        n = len(matrix_2[0])  # columns
        result = [[0 for _ in range(n)] for _ in range(m)]  # forming a template for result

        for i in range(m):  # iterating by row of matrix_1
            for j in range(n):  # iterating by column of matrix_2
                for k in range(len(matrix_2)):  # iterating by rows of matrix_2
                    result[i][j] += matrix_1[i][k] * matrix_2[k][j]
        return result


def main():
    while True:
        user_choice = menu()
        # exit
        if user_choice == '0':
            break

        # add matrices
        elif user_choice == '1':
            matrices = matrix_size(2)  # returns two matrices
            if len(matrices[0]) != len(matrices[1]) and len(matrices[0][0]) != len(matrices[1][0]):
                print('The operation cannot be performed.\n')
            else:
                result = sum_matrix(matrices[0], matrices[1])
                print_matrix(result)

        # multiply matrix by a constant
        elif user_choice == '2':
            matrix = matrix_size(1)
            matrix_result = mmult_c(matrix)
            print_matrix(matrix_result)

        # multiply matrices
        elif user_choice == '3':
            matrices = matrix_size(2)
            matrix_result = mmult(matrices[0], matrices[1])
            print_matrix(matrix_result)


main()
