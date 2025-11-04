import logging
from matrix_input import input_matrix
from matrix_generate import generate_matrix
from matrix_rotate import rotate_matrix
from exceptions import NoDataError, AlgorithmNotExecutedError, InvalidInputError
from messages import MESSAGES

# Настройка логирования
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger()

def show_menu():
    print("=== Главное меню ===")
    for item in MESSAGES["menu"]:
        print(item)

def main():
    data = None
    result = None

    logger.info("Программа запущена")

    try:
        while True:
            show_menu()
            choice = input("Выберите пункт меню: ")
            logger.info(f"Пользователь выбрал пункт меню: {choice}")

            if choice == "1":
                data = input_matrix()
                result = None
            elif choice == "2":
                try:
                    n = int(input("Введите количество строк: "))
                    m = int(input("Введите количество столбцов: "))
                    data = generate_matrix(n, m)
                    result = None
                except ValueError:
                    logger.error("Введено нечисловое значение")
                    raise InvalidInputError("Размеры матрицы должны быть числами")
            elif choice == "3":
                if data is None:
                    logger.warning("Попытка выполнить алгоритм без данных")
                    raise NoDataError(MESSAGES["no_data"])
                direction = input("Введите направление поворота ('clockwise' или 'counterclockwise'): ")
                result = rotate_matrix(data, direction)
            elif choice == "4":
                if result is None:
                    logger.warning("Попытка вывода результата без выполнения алгоритма")
                    raise AlgorithmNotExecutedError(MESSAGES["algorithm_not_executed"])
                print("Результат:")
                for row in result:
                    print(row)
            elif choice == "5":
                print(MESSAGES["exit"])
                logger.critical("Программа завершена пользователем")
                break
            else:
                print(MESSAGES["invalid_choice"])

    except KeyboardInterrupt:
        logger.critical("Программа прервана пользователем (Ctrl+C)")
        print("\nПрограмма завершена принудительно.")

    except (NoDataError, AlgorithmNotExecutedError, InvalidInputError) as e:
        print(f"Ошибка: {e}")
        logger.error(e)

if __name__ == "__main__":
    main()
