import logging
from server import handle_client_request
from exceptions import NoDataError, NoResultError, InvalidInputError

# Настройка логирования клиента
logging.basicConfig(
    filename="client.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def show_menu():
    """Выводит главное меню для пользователя."""
    print("\n=== Главное меню ===")
    print("1. Ручной ввод матрицы")
    print("2. Генерация случайной матрицы")
    print("3. Поворот матрицы")
    print("4. Вывод результата")
    print("5. Выход")


def main():
    """
    Главная функция клиента.

    Клиентский интерфейс:
    1. Ввод матрицы вручную
    2. Генерация случайной матрицы
    3. Поворот матрицы
    4. Вывод результата
    5. Выход

    Использует серверную функцию handle_client_request для выполнения операций.
    Логирует действия пользователя и ошибки.
    """
    client_name = "Клиент1"
    data = None
    result = None

    logging.info(f"{client_name}: программа запущена")

    while True:
        try:
            show_menu()
            choice = input("Выберите пункт меню: ").strip()
            logging.info(f"{client_name}: выбрал пункт {choice}")

            if choice == '1':
                # Ручной ввод матрицы
                data = handle_client_request(client_name, "input")
                result = None
                print("Введённая матрица:")
                for row in data:
                    print(row)
                logging.info(f"{client_name}: введена матрица вручную")

            elif choice == '2':
                # Генерация случайной матрицы
                n = int(input("Введите количество строк: "))
                m = int(input("Введите количество столбцов: "))
                data = handle_client_request(client_name, "generate", n=n, m=m)
                result = None
                print("Сгенерированная матрица:")
                for row in data:
                    print(row)
                logging.info(f"{client_name}: сгенерирована матрица {n}x{m}")

            elif choice == '3':
                # Поворот матрицы
                if data is None:
                    raise NoDataError("Сначала введите или сгенерируйте матрицу!")
                direction = input("Введите направление поворота ('clockwise' или 'counterclockwise'): ").strip().lower()
                if direction not in ['clockwise', 'counterclockwise']:
                    raise InvalidInputError("Направление должно быть 'clockwise' или 'counterclockwise'")
                result = handle_client_request(client_name, "rotate", matrix=data, direction=direction)
                logging.info(f"{client_name}: матрица повернута {direction}")

            elif choice == '4':
                # Вывод результата
                if result is None:
                    raise NoResultError("Сначала выполните алгоритм!")
                print("Результат:")
                for row in result:
                    print(row)
                logging.info(f"{client_name}: результат выведен")

            elif choice == '5':
                # Выход
                print("Выход из программы.")
                logging.info(f"{client_name}: завершил работу")
                break

            else:
                print("Неверный выбор, попробуйте снова.")
                logging.warning(f"{client_name}: неверный пункт меню {choice}")

        # Обработка пользовательских исключений
        except (NoDataError, NoResultError, InvalidInputError) as e:
            print(f"Ошибка: {e}")
            logging.warning(f"{client_name}: {e}")
        except ValueError:
            print("Ошибка: введите число от 1 до 5")
            logging.warning(f"{client_name}: введено некорректное значение")
        except KeyboardInterrupt:
            print("\nПрограмма прервана пользователем (Ctrl+C)")
            logging.critical(f"{client_name}: программа прервана пользователем")
            break
        except Exception as e:
            print(f"Произошла ошибка: {e}")
            logging.error(f"{client_name}: {e}")


if __name__ == "__main__":
    main()
