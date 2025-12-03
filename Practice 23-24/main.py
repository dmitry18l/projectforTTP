"""
Главный модуль приложения для работы с матрицами с использованием автоматного программирования через корутины.

Модуль реализует конечный автомат через корутины (генераторы) для управления состоянием приложения.
Каждое состояние представлено отдельной корутиной, которая сохраняет контекст выполнения между вызовами.

Состояния автомата:
    NO_DATA: Матрица не введена
    HAS_DATA: Матрица введена, результат операции отсутствует
    HAS_RESULT: Есть и матрица и результат операции
"""

import logging
from exceptions import NoDataError, InvalidInputError, AlgorithmNotExecutedError
from messages import MESSAGES
from matrix_input import input_matrix
from matrix_generate import generate_matrix
from matrix_rotate import rotate_matrix


# Настройка логирования
logging.basicConfig(
    filename="Practice 23-24/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def show_menu():
    """
    Отображает главное меню приложения в консоли.
    
    Использует текстовые сообщения из словаря MESSAGES для обеспечения
    единообразия интерфейса.
    """
    print("\n" + "="*20 + " Главное меню " + "="*20)
    for menu_item in MESSAGES["menu"]:
        print(menu_item)
    print("="*55)


def print_matrix(matrix, title="Матрица"):
    """
    Выводит матрицу в консоль с форматированием и заголовком.
    
    Args:
        matrix: Матрица для вывода в виде списка списков
        title: Заголовок для отображения над матрицей
    """
    print(f"\n{title}:")
    for row in matrix:
        print(row)


def state_no_data():
    """
    Корутина состояния NO_DATA - матрица не введена.
    
    Ожидает команду пользователя, обрабатывает ее и возвращает следующее состояние.
    
    Yields:
        Ожидает команду пользователя (через yield)
            
    Raises:
        NoDataError: При попытке выполнить операцию без данных (команда 3)
        AlgorithmNotExecutedError: При попытке вывода несуществующего результата (команда 4)
        InvalidInputError: При некорректном вводе размеров матрицы
    """
    logging.info("Состояние: NO_DATA")
    
    while True:
        # Ждем команду от пользователя
        command = yield
        
        if command == '1':
            # Ручной ввод матрицы
            data = input_matrix()
            logging.info("Матрица введена вручную")
            print_matrix(data, "Введенная матрица")
            # Переход в состояние HAS_DATA с введенными данными
            yield ('HAS_DATA', data, None)
            return
            
        elif command == '2':
            # Генерация случайной матрицы
            try:
                n = int(input("Введите количество строк: "))
                m = int(input("Введите количество столбцов: "))
                
                if n <= 0 or m <= 0:
                    raise InvalidInputError("Размеры матрицы должны быть положительными числами")
                
                data = generate_matrix(n, m)
                logging.info(f"Сгенерирована случайная матрица {n}x{m}")
                print_matrix(data, "Сгенерированная матрица")
                # Переход в состояние HAS_DATA с сгенерированными данными
                yield ('HAS_DATA', data, None)
                return
                
            except ValueError:
                raise InvalidInputError("Введите целые числа для размеров матрицы")
                
        elif command == '3':
            # Поворот матрицы - ошибка, нет данных
            raise NoDataError(MESSAGES["no_data"])
            
        elif command == '4':
            # Вывод результата - ошибка, нет результата
            raise AlgorithmNotExecutedError(MESSAGES["algorithm_not_executed"])
            
        elif command == '5':
            # Выход из программы
            print(MESSAGES["exit"])
            logging.info("Программа завершена пользователем")
            yield ('EXIT', None, None)
            return
            
        else:
            # Некорректный ввод
            print(MESSAGES["invalid_choice"])
            logging.warning(f"Неверный выбор меню: {command}")
            # Остаемся в текущем состоянии
            yield ('NO_DATA', None, None)
            return


def state_has_data(data):
    """
    Корутина состояния HAS_DATA - матрица введена, результат отсутствует.
    
    Ожидает команду пользователя для работы с существующей матрицей.
    
    Args:
        data: Текущая матрица для операций
        
    Yields:
        Ожидает команду пользователя (через yield)
    """
    logging.info("Состояние: HAS_DATA")
    current_data = data
    
    while True:
        # Ждем команду от пользователя
        command = yield
        
        if command == '1':
            # Ручной ввод новой матрицы (сброс данных)
            new_data = input_matrix()
            logging.info("Матрица введена вручную")
            print_matrix(new_data, "Введенная матрица")
            # Переход в состояние HAS_DATA с новыми данными
            yield ('HAS_DATA', new_data, None)
            return
            
        elif command == '2':
            # Генерация новой случайной матрицы (сброс данных)
            try:
                n = int(input("Введите количество строк: "))
                m = int(input("Введите количество столбцов: "))
                
                if n <= 0 or m <= 0:
                    raise InvalidInputError("Размеры матрицы должны быть положительными числами")
                
                new_data = generate_matrix(n, m)
                logging.info(f"Сгенерирована случайная матрица {n}x{m}")
                print_matrix(new_data, "Сгенерированная матрица")
                # Переход в состояние HAS_DATA с новыми данными
                yield ('HAS_DATA', new_data, None)
                return
                
            except ValueError:
                raise InvalidInputError("Введите целые числа для размеров матрицы")
                
        elif command == '3':
            # Поворот текущей матрицы
            try:
                direction = input("Введите направление поворота ('clockwise' или 'counterclockwise'): ").strip().lower()
                
                if direction not in ['clockwise', 'counterclockwise']:
                    raise InvalidInputError("Направление поворота должно быть 'clockwise' или 'counterclockwise'")
                
                result = rotate_matrix(current_data, direction)
                logging.info(f"Матрица повернута в направлении: {direction}")
                print_matrix(result, "Повернутая матрица")
                # Переход в состояние HAS_RESULT с данными и результатом
                yield ('HAS_RESULT', current_data, result)
                return
                
            except InvalidInputError as e:
                # Ошибка ввода направления - остаемся в текущем состоянии
                print(f"Ошибка: {e}")
                logging.warning(f"Ошибка при вводе направления: {e}")
                yield ('HAS_DATA', current_data, None)
                return
                
        elif command == '4':
            # Вывод результата - ошибка, результат еще не вычислен
            raise AlgorithmNotExecutedError(MESSAGES["algorithm_not_executed"])
            
        elif command == '5':
            # Выход из программы
            print(MESSAGES["exit"])
            logging.info("Программа завершена пользователем")
            yield ('EXIT', None, None)
            return
            
        else:
            # Некорректный ввод
            print(MESSAGES["invalid_choice"])
            logging.warning(f"Неверный выбор меню: {command}")
            yield ('HAS_DATA', current_data, None)
            return


def state_has_result(data, result):
    """
    Корутина состояния HAS_RESULT - есть и матрица и результат операции.
    
    Ожидает команду пользователя для работы с матрицей и результатом.
    
    Args:
        data: Текущая матрица
        result: Результат последней операции
    """
    logging.info("Состояние: HAS_RESULT")
    current_data = data
    current_result = result
    
    while True:
        # Ждем команду от пользователя
        command = yield
        
        if command == '1':
            # Ручной ввод новой матрицы (сброс результата)
            new_data = input_matrix()
            logging.info("Матрица введена вручную")
            print_matrix(new_data, "Введенная матрица")
            # Переход в состояние HAS_DATA с новыми данными
            yield ('HAS_DATA', new_data, None)
            return
            
        elif command == '2':
            # Генерация новой случайной матрицы (сброс результата)
            try:
                n = int(input("Введите количество строк: "))
                m = int(input("Введите количество столбцов: "))
                
                if n <= 0 or m <= 0:
                    raise InvalidInputError("Размеры матрицы должны быть положительными числами")
                
                new_data = generate_matrix(n, m)
                logging.info(f"Сгенерирована случайная матрица {n}x{m}")
                print_matrix(new_data, "Сгенерированная матрица")
                # Переход в состояние HAS_DATA с новыми данными
                yield ('HAS_DATA', new_data, None)
                return
                
            except ValueError:
                raise InvalidInputError("Введите целые числа для размеров матрицы")
                
        elif command == '3':
            # Поворот текущей матрицы
            try:
                direction = input("Введите направление поворота ('clockwise' или 'counterclockwise'): ").strip().lower()
                
                if direction not in ['clockwise', 'counterclockwise']:
                    raise InvalidInputError("Направление поворота должно быть 'clockwise' или 'counterclockwise'")
                
                new_result = rotate_matrix(current_data, direction)
                logging.info(f"Матрица повернута в направлении: {direction}")
                print_matrix(new_result, "Повернутая матрица")
                # Остаемся в состоянии HAS_RESULT с новым результатом
                yield ('HAS_RESULT', current_data, new_result)
                return
                
            except InvalidInputError as e:
                # Ошибка ввода направления - остаемся в текущем состоянии
                print(f"Ошибка: {e}")
                logging.warning(f"Ошибка при вводе направления: {e}")
                yield ('HAS_RESULT', current_data, current_result)
                return
                
        elif command == '4':
            # Вывод текущего результата
            print_matrix(current_result, "Результат операции")
            logging.info("Результат выведен на экран")
            # Остаемся в состоянии HAS_RESULT
            yield ('HAS_RESULT', current_data, current_result)
            return
            
        elif command == '5':
            # Выход из программы
            print(MESSAGES["exit"])
            logging.info("Программа завершена пользователем")
            yield ('EXIT', None, None)
            return
            
        else:
            # Некорректный ввод
            print(MESSAGES["invalid_choice"])
            logging.warning(f"Неверный выбор меню: {command}")
            yield ('HAS_RESULT', current_data, current_result)
            return


def main():
    """
    Главная функция программы с автоматным управлением через корутины.
    
    Управляет жизненным циклом приложения, создает и переключает корутины состояний,
    обрабатывает пользовательский ввод и исключения.
    """
    # Инициализация состояния и данных
    state = 'NO_DATA'
    data = None
    result = None
    
    logging.info("Программа запущена")

    while True:
        try:
            show_menu()
            choice = input("Выберите пункт меню: ").strip()
            logging.info(f"Пользователь выбрал пункт меню: {choice}")
            
            # Создание и запуск корутины для текущего состояния
            if state == 'NO_DATA':
                coroutine = state_no_data()
                next(coroutine)  # Инициализация корутины
                
                # Отправка команды и получение результата
                next_state, new_data, new_result = coroutine.send(choice)
                
            elif state == 'HAS_DATA':
                coroutine = state_has_data(data)
                next(coroutine)
                next_state, new_data, new_result = coroutine.send(choice)
                
            elif state == 'HAS_RESULT':
                coroutine = state_has_result(data, result)
                next(coroutine)
                next_state, new_data, new_result = coroutine.send(choice)
            
            # Обработка результата от корутины
            if next_state == 'EXIT':
                # Завершение программы
                break
                
            # Обновление состояния и данных
            state = next_state
            if new_data is not None:
                data = new_data
            if new_result is not None:
                result = new_result
        
        except (NoDataError, InvalidInputError, AlgorithmNotExecutedError) as e:
            # Обработка ожидаемых ошибок
            print(f"Ошибка: {e}")
            logging.warning(f"{type(e).__name__}: {e}")
            
        except StopIteration:
            # Корутина завершилась (нормальное завершение)
            continue
            
        except KeyboardInterrupt:
            # Пользователь прервал выполнение
            print("\nПрограмма прервана пользователем")
            logging.critical("Программа прервана через KeyboardInterrupt")
            break
        

if __name__ == "__main__":
    main()