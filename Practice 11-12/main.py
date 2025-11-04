# main.py
from matrix_input import input_matrix
from matrix_generate import generate_matrix
from matrix_rotate import rotate_matrix

def main():
    """
    Главная функция для тестирования трёх пунктов:
    1) Ручной ввод матрицы
    2) Генерация случайной матрицы
    3) Поворот матрицы на 90 градусов
    """

    # === Пункт 1: Ручной ввод матрицы ===
    print("=== Пункт 1: Ручной ввод матрицы ===")
    matrix_manual = input_matrix()  # функция из matrix_input.py
    print("Введённая матрица:")
    for row in matrix_manual:
        print(row)

    # === Пункт 2: Генерация случайной матрицы ===
    print("\n=== Пункт 2: Генерация случайной матрицы ===")
    n = int(input("Введите количество строк для случайной матрицы: "))
    m = int(input("Введите количество столбцов для случайной матрицы: "))
    matrix_random = generate_matrix(n, m)
    print("Сгенерированная матрица:")
    for row in matrix_random:
        print(row)

    # === Пункт 3: Поворот матрицы ===
    print("\n=== Пункт 3: Поворот матрицы ===")
    # Для примера используем сгенерированную матрицу
    matrix_to_rotate = matrix_random
    direction = input("Введите направление поворота ('clockwise' или 'counterclockwise'): ")
    rotated = rotate_matrix(matrix_to_rotate, direction)
    print("Повернутая матрица:")
    for row in rotated:
        print(row)

if __name__ == "__main__":
    main()
