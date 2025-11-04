import logging
from matrix_input import input_matrix
from matrix_generate import generate_matrix
from matrix_rotate import rotate_matrix

# Настройка логирования
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,  # Можно поменять на CRITICAL, чтобы отключить логирование
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def menu():
    """Главное меню приложения."""
    print("\n=== Главное меню ===")
    print("1. Ввод матрицы вручную")
    print("2. Генерация случайной матрицы")
    print("3. Поворот матрицы")
    print("4. Вывод результата")
    print("5. Завершение программы")


def print_matrix(matrix, title="Матрица"):
    """Красивый вывод матрицы."""
    print(f"\n=== {title} ===")
    for row in matrix:
        print(" ".join(map(str, row)))


def main():
    """Финальная программа с логированием."""
    data = None
    result = None

    logging.info("Программа запущена")

    while True:
        menu()
        choice = input("Выберите пункт меню (1–5): ").strip()
        logging.info(f"Пользователь выбрал пункт меню: {choice}")

        if choice == "1":
            data = input_matrix()
            result = None
            print_matrix(data, "Введённая матрица")
            logging.info("Вызвана функция input_matrix()")

        elif choice == "2":
            try:
                n = int(input("Введите количество строк: "))
                m = int(input("Введите количество столбцов: "))
                data = generate_matrix(n, m)
                result = None
                print_matrix(data, "Сгенерированная матрица")
                logging.info(f"Вызвана функция generate_matrix({n}, {m})")
            except ValueError:
                print("Ошибка: размеры должны быть целыми числами.")
                logging.warning("Ошибка при вводе размеров матрицы")

        elif choice == "3":
            if data is None:
                print("Ошибка: сначала введите или сгенерируйте матрицу!")
                logging.warning("Попытка поворота без данных")
            else:
                direction = input("Введите направление ('clockwise' или 'counterclockwise'): ").strip().lower()
                if direction not in ("clockwise", "counterclockwise"):
                    print("Ошибка: допустимые значения — 'clockwise' или 'counterclockwise'.")
                    logging.warning("Неверное направление поворота")
                else:
                    result = rotate_matrix(data, direction)
                    print_matrix(result, "Повернутая матрица")
                    logging.info(f"Вызвана функция rotate_matrix(direction={direction})")

        elif choice == "4":
            if result is None:
                print("Ошибка: результат отсутствует. Сначала выполните алгоритм.")
                logging.warning("Попытка вывода результата без выполнения алгоритма")
            else:
                print_matrix(result, "Результат")
                logging.info("Результат успешно выведен пользователю")

        elif choice == "5":
            print("Программа завершена.")
            logging.info("Программа завершена пользователем")
            break

        else:
            print("Ошибка: выберите пункт от 1 до 5.")
            logging.warning(f"Введён некорректный пункт меню: {choice}")


if __name__ == "__main__":
    main()
