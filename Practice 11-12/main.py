import logging
from matrix_input import input_matrix
from matrix_generate import generate_matrix
from matrix_rotate import rotate_matrix

# Настройка логирования
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Пользовательские исключения
class NoDataError(Exception):
    """Исключение для отсутствующих данных"""
    pass

class NoResultError(Exception):
    """Исключение для отсутствующего результата"""
    pass

def show_menu():
    """Печатает главное меню приложения"""
    print("\n=== Главное меню ===")
    print("1. Ручной ввод матрицы")
    print("2. Генерация случайной матрицы")
    print("3. Поворот матрицы")
    print("4. Вывод результата")
    print("5. Выход")

def main():
    """Главная функция программы"""
    data = None
    result = None
    
    logging.info("Программа запущена")

    while True:
        try:
            show_menu()
            choice = input("Выберите пункт меню: ")
            logging.info(f"Пользователь выбрал пункт меню: {choice}")
            
            if choice == '1':
                data = input_matrix()
                result = None
                logging.info("Введена матрица вручную")
                print("Введённая матрица:")
                for row in data:
                    print(row)

            elif choice == '2':
                n = int(input("Введите количество строк: "))
                m = int(input("Введите количество столбцов: "))
                data = generate_matrix(n, m)
                result = None
                logging.info(f"Сгенерирована матрица {n}x{m}")
                
                # Вывод сгенерированной матрицы
                print("Сгенерированная матрица:")
                for row in data:
                    print(row)

            elif choice == '3':
                if data is None:
                    raise NoDataError("Сначала введите или сгенерируйте матрицу!")
                direction = input("Введите направление поворота ('clockwise' или 'counterclockwise'): ")
                result = rotate_matrix(data, direction)
                logging.info(f"Матрица повернута: {direction}")
                print("Повернутая матрица:")
                for row in result:
                    print(row)

            elif choice == '4':
                if result is None:
                    raise NoResultError("Сначала выполните алгоритм!")
                print("Результат:")
                for row in result:
                    print(row)
                logging.info("Результат выведен")

            elif choice == '5':
                print("Выход из программы.")
                logging.info("Программа завершена пользователем")
                break

            else:
                print("Неверный выбор, попробуйте снова.")
        
        except NoDataError as nde:
            print(f"Ошибка: {nde}")
            logging.warning(f"Попытка выполнить операцию без данных: {nde}")
        except NoResultError as nre:
            print(f"Ошибка: {nre}")
            logging.warning(f"Попытка вывести результат до выполнения алгоритма: {nre}")
        except KeyboardInterrupt:
            print("\nПрограмма прервана пользователем (Ctrl+C)")
            logging.critical("Программа прервана пользователем (Ctrl+C)")
            break
        except Exception as e:
            print(f"Произошла ошибка: {e}")
            logging.error(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()
