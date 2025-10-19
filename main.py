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
    return "заглушка: ввод данных"


def run_algorithm():
    return "заглушка: выполнение алгоритма"


def print_result():
    return "заглушка: вывод результата"


if __name__ == "__main__":
    main_menu()
