import random


def main():
    """
    Главная функция программы. Управляет циклом меню и взаимодействием с пользователем.
    """
    matrix = None
    result1 = None
    result2 = None

    while True:
        print("\n--- Главное меню ---")
        print("1. Ввод данных")
        print("2. Выполнение алгоритма")
        print("3. Показ результата")
        print("4. Выход")

        choice = input("Выберите пункт: ")

        if choice == "1":
            # Ввод исходной матрицы
            matrix = input_data()
            result1, result2 = None, None  # сбрасываем предыдущие результаты
        elif choice == "2":
            # Запуск алгоритма сортировки
            if matrix is None:
                print("Сначала введите данные.")
            else:
                result1, result2 = run_algorithm(matrix)
                print("Алгоритм выполнен.")
        elif choice == "3":
            # Показ результатов выполнения
            if result1 is None or result2 is None:
                print("Сначала выполните алгоритм.")
            else:
                print_result(result1, result2)
        elif choice == "4":
            # Завершение программы
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор.")

# Ввод исходных данных
def input_data():
    """
    Подменю для выбора способа ввода матрицы.
    """
    print("\n--- Ввод данных ---")
    print("1. Ввести вручную")
    print("2. Сгенерировать случайно")
    choice = input("Выберите способ: ")

    if choice == "1":
        return manual_input()
    elif choice == "2":
        return random_input()
    else:
        print("Неверный выбор.")
        return None


def manual_input():
    """
    Ручной ввод матрицы пользователем.
    """
    rows = int(input("Введите количество строк: "))
    cols = int(input("Введите количество столбцов: "))
    matrix = []

    for i in range(rows):
        while True:
            try:
                row = list(map(int, input(f"Введите {cols} чисел через пробел для строки {i + 1}: ").split()))
                if len(row) != cols:
                    raise ValueError
                matrix.append(row)
                break
            except ValueError:
                print("Ошибка: введите правильное количество целых чисел.")
    return matrix


def random_input():
    """
    Генерация случайной матрицы заданных размеров.
    """
    rows = int(input("Введите количество строк: "))
    cols = int(input("Введите количество столбцов: "))
    min_val = int(input("Минимальное значение элемента: "))
    max_val = int(input("Максимальное значение элемента: "))

    matrix = [[random.randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)]

    print("Сгенерирована матрица:")
    print_matrix(matrix)
    return matrix

# Алгоритм обработки
def run_algorithm(matrix):
    """
    Выполняет два шага обработки матрицы:
    1. Сортировка строк по убыванию среднего арифметического.
    2. Сортировка столбцов по убыванию среднего арифметического.
    """
    result1 = sort_rows(matrix)
    result2 = sort_columns(result1)
    return result1, result2


def sort_rows(matrix):
    """
    Сортирует строки матрицы по убыванию среднего арифметического их элементов.
    """
    return sorted(matrix, key=lambda row: sum(row) / len(row), reverse=True)


def sort_columns(matrix):
    """
    Сортирует столбцы матрицы по убыванию среднего арифметического их элементов.

    Алгоритм:
    1. Транспонируем матрицу (строки -> столбцы).
    2. Сортируем столбцы по убыванию среднего значения.
    3. Транспонируем обратно для получения исходного вида.
    """
    # транспонирование (строки → столбцы)
    cols = [list(col) for col in zip(*matrix)]

    # сортировка по среднему арифметическому каждого столбца
    sorted_cols = sorted(cols, key=lambda col: sum(col) / len(col), reverse=True)

    # обратное транспонирование
    sorted_matrix = [list(row) for row in zip(*sorted_cols)]
    return sorted_matrix

# Вывод результатов
def print_result(result1, result2):
    """
    Печатает результаты выполнения алгоритма:
    - матрицу после сортировки строк;
    - матрицу после сортировки столбцов.
    """
    print("\n--- Результаты ---")
    print("Матрица после сортировки строк:")
    print_matrix(result1)
    print("Матрица после сортировки столбцов:")
    print_matrix(result2)


def print_matrix(matrix):
    """
    Красивый вывод матрицы в консоль.
    """
    for row in matrix:
        print(' '.join(map(str, row)))

# Точка входа
if __name__ == "__main__":
    main()
