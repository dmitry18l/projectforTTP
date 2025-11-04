matrix = None
result1 = None
result2 = None


def main_menu():
    while True:
        print("\n--- Главное меню ---")
        print("1. Ввод данных")
        print("2. Выполнение алгоритма")
        print("3. Показ результата")
        print("4. Выход")

        choice = input("Выберите пункт: ")

        if choice == "1":
            input_data()
        elif choice == "2":
            run_algorithm()
        elif choice == "3":
            print_result()
        elif choice == "4":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор.")


def input_data():
    global matrix, result1, result2

    print("\n--- Ввод данных ---")
    print("1. Ввести вручную")
    print("2. Сгенерировать случайно")
    choice = input("Выберите способ: ")

    if choice == "1":
        matrix = manual_input()
    elif choice == "2":
        matrix = random_input()
    else:
        print("Неверный выбор")

    result1 = None
    result2 = None


def run_algorithm():
    global matrix, result1, result2

    if matrix is None:
        print("Сначала введите данные.")
        return

    result1 = sort_rows(matrix)
    result2 = sort_columns(result1)
    print("Алгоритм выполнен.")


def print_result():
    global result1, result2

    if result1 is None or result2 is None:
        print("Сначала выполните алгоритм.")
        return

    print("\n--- Результаты ---")
    print("Матрица после сортировки строк:")
    print_matrix(result1)
    print("Матрица после сортировки столбцов:")
    print_matrix(result2)


# --- ВСПОМОГАТЕЛЬНЫЕ функции (заглушки) ---

def manual_input():
    return [[1, 2], [3, 4]]  # заглушка


def random_input():
    return [[5, 6], [7, 8]]  # заглушка


def sort_rows(matrix):
    return matrix  # заглушка


def sort_columns(matrix):
    return matrix  # заглушка


def print_matrix(matrix):
    for row in matrix:
        print(row)


# Запуск
if __name__ == "__main__":
    main_menu()