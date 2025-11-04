from matrix_generate import generate_matrix
from matrix_rotate import rotate_matrix

def main():
    """
    Тестирование функции поворота матрицы (итерация 3)
    """
    # Генерация случайной матрицы для проверки
    n = 3
    m = 4
    matrix = generate_matrix(n, m)
    
    print("Исходная матрица:")
    for row in matrix:
        print(row)

    # Поворот матрицы
    direction = input("Введите направление поворота ('clockwise' или 'counterclockwise'): ")
    rotated = rotate_matrix(matrix, direction)
    
    print("Повернутая матрица:")
    for row in rotated:
        print(row)

if __name__ == "__main__":
    main()
