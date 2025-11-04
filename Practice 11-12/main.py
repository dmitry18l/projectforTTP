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
    
    # === Пункт 1 и 2 ===
    # Генерируем матрицу для теста поворота
    n = 3
    m = 4
    matrix = generate_matrix(n, m)  # Генерация случайной матрицы
    print("Исходная матрица:")
    for row in matrix:
        print(row)

    # === Пункт 3 ===
    # Запрашиваем направление поворота у пользователя
    direction = input("Введите направление поворота ('clockwise' или 'counterclockwise'): ")
    rotated = rotate_matrix(matrix, direction)  # Поворот матрицы
    print("Повернутая матрица:")
    for row in rotated:
        print(row)

if __name__ == "__main__":
    main()
