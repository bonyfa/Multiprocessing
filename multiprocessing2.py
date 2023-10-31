import concurrent.futures

def sum_r(row):
    return sum(row)

def sum_col(matr, col_index):
    col_sum = 0
    for row in matr:
        col_sum += row[col_index]
    return col_sum

if __name__ == '__main__':
    import sys

    print("Задайте в коммандной строке матрицу с помощью: python multiprocessing.py <число строк> <число столбцов> <значения матрицы>")
    matrix_d = int(sys.argv[1])
    matrix_v = sys.argv[2:]

    matrix = [list(map(int, matrix_v[i:i+matrix_d])) for i in range(0, len(matrix_v), matrix_d)]

    executor = concurrent.futures.ProcessPoolExecutor()

    r_sums = executor.map(sum_r, matrix)

    col_sums = executor.map(lambda i: sum_col(matrix, i), range(matrix_d))

    executor.shutdown()

    t_sum = sum(r_sums)

    print("Сумма элементов по строкам:", list(r_sums))
    print("Сумма элементов по столбцам:", list(col_sums))
    print("Итоговая сумма:", t_sum)


