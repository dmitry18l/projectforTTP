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
    Позволяет пользователю выбирать действия и отправляет запросы на сервер.
    """
    client_name = "Клиент1"
    data = None
    result = None

    logging.info(f"{client_name}: программа запущена")

    while True:
        try:
            show_menu()
            choice = input("Выберите пункт меню: ")
            logging.info(f"{client_name}: выбрал пункт {choice}")

            if choice == '1':
                data = handle_client_request(client_name, "input")
                result = None

            elif choice == '2':
                n = int(input("Введите количество строк: "))
                m = int(input("Введите количество столбцов: "))
                data = handle_client_request(client_name, "generate", n=n, m=m)
                result = None

            elif choice == '3':
                if data is None:
                    raise NoDataError("Сначала введите или сгенерируйте матрицу!")
                direction = input("Введите направление поворота ('clockwise' или 'counterclockwise'): ")
                result = handle_client_request(client_name, "rotate", matrix=data, direction=direction)

            elif choice == '4':
                if result is None:
                    raise NoResultError("Сначала выполните алгоритм!")
                print("Результат:")
                for row in result:
                    print(row)
                logging.info(f"{client_name}: результат выведен")

            elif choice == '5':
                print("Выход из программы.")
                logging.info(f"{client_name}: завершил работу")
                break

            else:
                print("Неверный выбор, попробуйте снова.")

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
