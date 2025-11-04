import logging
from matrix_input import input_matrix
from matrix_generate import generate_matrix
from matrix_rotate import rotate_matrix

# Настройка логирования
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,  # можно изменить на CRITICAL, чтобы отключить логирование
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def menu():
    """
    Функция отображения меню
    """
    print("\n=== Главное меню ===")
    print("1. Ручной ввод матрицы")
    print("2. Генерация случайной матрицы")
    print("3. Поворот матрицы")
    print("4. Вывод результата")
    print("5. Выход")

def main():
    """
    Главная функция консольного приложения
    """
    data = None
    result = None

    logging.info("Программа запущена")

    while True:
        try:
            menu()
            choice = input("Выберите пункт меню: ").strip()
            logging.info(f"Пользователь выбрал пункт меню: {choice}")

            if choice == '1':
                data = input_matrix()
                result = None  # сброс результата при новом вводе

            elif choice == '2':
                try:
                    n = int(input("Введите количество строк: "))
                    m = int(input("Введите количество столбцов: "))
                    data = generate_matrix(n, m)
                    result = None
                    print("Сгенерированная матрица:")
                    for row in data:
                        print(row)
                except ValueError as e:
                    logging.error(f"Ошибка при вводе размеров: {e}")
                    print("Ошибка! Введите целые числа.")

            elif choice == '3':
                if data is None:
                    print("Сначала введите или сгенерируйте матрицу!")
                    logging.warning("Попытка поворота без данных")
                else:
                    direction = input("Введите направление поворота ('clockwise' или 'counterclockwise'): ").strip()
                    result = rotate_matrix(data, direction)
                    if result:
                        print("Повернутая матрица:")
                        for row in result:
                            print(row)

            elif choice == '4':
                if result is None:
                    print("Сначала выполните алгоритм!")
                    logging.warning("Попытка вывода без результата")
                else:
                    print("Результат выполнения алгоритма:")
                    for row in result:
                        print(row)

            elif choice == '5':
                print("Выход из программы.")
                logging.info("Пользователь завершил программу.")
                break

            else:
                print("Неверный выбор. Попробуйте снова.")
                logging.warning(f"Некорректный ввод пункта меню: {choice}")

        except Exception as e:
            logging.error(f"Необработанная ошибка в main: {e}")
            print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nПрограмма прервана пользователем.")
        logging.critical("Программа прервана пользователем (Ctrl+C).")
