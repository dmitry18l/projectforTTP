from matrix_input import input_matrix
from matrix_generate import generate_matrix
from matrix_rotate import rotate_matrix


def menu():
    """Главное меню приложения."""
    print("\n=== Главное меню ===")
    print("1. Ввод матрицы вручную")
    print("2. Генерация случайной матрицы")
    print("3. Поворот матрицы")
    print("4. Вывод результата")
    print("5. Завершение программы")


def print_matrix(matrix, title="Матрица"):
    """Вспомогательная функция для красивого вывода матрицы."""
    print(f"\n=== {title} ===")
    for row in matrix:
        print(" ".join(map(str, row)))


def main():
    """Финальная программа с консольным меню."""
    data = None
    result = None

    while True:
        menu()
        choice = input("Выберите пункт меню (1–5): ").strip()

        if choice == "1":
            data = input_matrix()
            result = None
            print_matrix(data, "Введённая матрица")

        elif choice == "2":
            try:
                n = int(input("Введите количество строк: "))
                m = int(input("Введите количество столбцов: "))
                data = generate_matrix(n, m)
                result = None
                print_matrix(data, "Сгенерированная матрица")
            except ValueError:
                print("Ошибка: размеры должны быть целыми числами.")

        elif choice == "3":
            if data is None:
                print("Ошибка: сначала введите или сгенерируйте матрицу!")
            else:
                direction = input("Введите направление поворота ('clockwise' или 'counterclockwise'): ").strip().lower()
                if direction not in ("clockwise", "counterclockwise"):
                    print("Ошибка: допустимые значения — 'clockwise' или 'counterclockwise'.")
                else:
                    result = rotate_matrix(data, direction)
                    print_matrix(result, "Повернутая матрица")

        elif choice == "4":
            if result is None:
                print("Ошибка: результат отсутствует. Сначала выполните алгоритм.")
            else:
                print_matrix(result, "Результат")

        elif choice == "5":
            print("Программа завершена.")
            break

        else:
            print("Ошибка: выберите пункт от 1 до 5.")


if __name__ == "__main__":
    main()
