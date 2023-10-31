import multiprocessing
import sys


def sum_col(matr, col_index):
    col_sum = 0
    for row in matr:
        col_sum += row[col_index]
    return col_sum


def sum_row(row):
    return sum(row)


if __name__ == '__main__':
    print("Задайте в коммандной строке матрицу с помощью: python multiprocessing.py <число строк> <число столбцов> <значения матрицы>")
    matrix_d = int(sys.argv[1])
    matrix_v = sys.argv[2:]


    matrix = [list(map(int, matrix_v[i:i+matrix_d])) for i in range(0, len(matrix_v), matrix_d)]

    pool = multiprocessing.Pool()

    row_sums = pool.map(sum_row, matrix)

    col_sums = pool.map(lambda i: sum_col(matrix, i), range(matrix_d))

    pool.close()
    pool.join()

    t_sum = sum(row_sums)

    print("Сумма элементов по строкам:", row_sums)
    print("Сумма элементов по столбцам:", col_sums)
    print("Итоговая сумма:", t_sum)
