# main.py
from matrix_input import input_matrix  # первый этап: ручной ввод
from matrix_generate import generate_matrix  # второй этап: генерация случайной матрицы

def main():
    print("=== Пункт 1: Ручной ввод матрицы ===")
    matrix_manual = input_matrix()  # функция из matrix_input.py
    print("\nВведённая матрица:")
    for row in matrix_manual:
        print(row)

    print("\n=== Пункт 2: Генерация случайной матрицы ===")
    # Можно задать размеры вручную или через input
    n = int(input("Введите количество строк для случайной матрицы: "))
    m = int(input("Введите количество столбцов для случайной матрицы: "))
    matrix_random = generate_matrix(n, m)
    print("\nСгенерированная матрица:")
    for row in matrix_random:
        print(row)

if __name__ == "__main__":
    main()
