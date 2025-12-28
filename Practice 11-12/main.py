"""
Главный модуль приложения для работы с матрицами.

Обеспечивает консольный интерфейс для операций с матрицами:
- Ручной ввод матриц
- Генерация случайных матриц  
- Поворот матриц на 90 градусов
- Логирование операций
- Обработка пользовательских исключений

Основной поток выполнения:
    1. Инициализация переменных данных и результатов
    2. Бесконечный цикл отображения меню
    3. Обработка пользовательского ввода
    4. Вызов соответствующих матричных операций
    5. Обработка исключений и логирование событий

Используемые модули:
    exceptions - пользовательские исключения для матричных операций
    messages - текстовые сообщения для интерфейса
    matrix_input - функции для ручного ввода матриц
    matrix_generate - функции для генерации случайных матриц  
    matrix_rotate - функции для поворота матриц
"""

import logging
from exceptions import NoDataError, InvalidInputError, AlgorithmNotExecutedError
from messages import MESSAGES
from matrix_input import input_matrix
from matrix_generate import generate_matrix
from matrix_rotate import rotate_matrix


# Настройка логирования
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def show_menu():
    """
    Отображает главное меню приложения в консоли.
    
    Использует текстовые сообщения из словаря MESSAGES для обеспечения
    единообразия интерфейса и возможности легкой локализации.
    
    Меню включает следующие пункты:
        - Ручной ввод матрицы
        - Генерация случайной матрицы
        - Поворот матрицы
        - Вывод результата
        - Выход из программы
    
    Example:
        >>> show_menu()
        ==================== Главное меню ====================
        1. Ручной ввод матрицы
        2. Генерация случайной матрицы
        3. Поворот матрицы
        4. Вывод результата
        5. Выход
        =======================================================
    """
    print("\n" + "="*20 + " Главное меню " + "="*20)
    for menu_item in MESSAGES["menu"]:
        print(menu_item)
    print("="*55)


def print_matrix(matrix, title="Матрица"):
    """
    Выводит матрицу в консоль с форматированием и заголовком.
    
    Args:
        matrix: Матрица для вывода в виде списка списков элементов
        title: Заголовок, который будет отображен над матрицей
    
    Функция обеспечивает читабельный вывод матрицы, где каждая
    строка матрицы выводится на отдельной строке консоли.
    
    Example:
        >>> matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        >>> print_matrix(matrix, "Квадратная матрица 3x3")
        Квадратная матрица 3x3:
        [1, 2, 3]
        [4, 5, 6]
        [7, 8, 9]
    """
    print(f"\n{title}:")
    for row in matrix:
        print(row)


def main():
    """
    Главная функция программы, управляющая основным циклом приложения.
    
    Логика работы:
        1. Инициализация переменных data и result значением None
        2. Запуск бесконечного цикла отображения меню
        3. Обработка выбора пользователя и вызов соответствующих функций
        4. Управление состоянием данных и результатов
        5. Обработка исключений через пользовательские классы
        6. Логирование всех значимых событий в файл app.log
    
    Переменные состояния:
        data: Текущая матрица для операций. 
              None - матрица не инициализирована
              list - текущая матрица для операций
        
        result: Результат последней операции.
                None - операция не выполнялась или данные изменились
                list - результат последней успешной операции поворота
    
    Обрабатываемые исключения:
        NoDataError: При попытке выполнить операцию с отсутствующей матрицей
        InvalidInputError: При вводе некорректных данных пользователем
        AlgorithmNotExecutedError: При попытке доступа к несуществующему результату
        KeyboardInterrupt: При прерывании программы пользователем (Ctrl+C)
        Exception: При других непредвиденных ошибках
    
    Взаимодействие с пользователем:
        - Пункт 1: Ручной ввод матрицы через matrix_input.input_matrix()
        - Пункт 2: Генерация случайной матрицы через matrix_generate.generate_matrix()
        - Пункт 3: Поворот матрицы через matrix_rotate.rotate_matrix()
        - Пункт 4: Вывод текущего результата операций
        - Пункт 5: Корректный выход из программы
    
    Логирование:
        - Все действия пользователя логируются в файл app.log
        - Ошибки и исключения записываются с соответствующим уровнем важности
        - Время каждого события фиксируется с точностью до секунды
    """
    data = None
    result = None
    
    logging.info("Программа запущена")

    while True:
        try:
            show_menu()
            choice = input("Выберите пункт меню: ").strip()
            logging.info(f"Пользователь выбрал пункт меню: {choice}")
            
            if choice == '1':
                # Ручной ввод матрицы
                data = input_matrix()
                result = None  # Сброс результата при изменении исходных данных
                logging.info("Матрица введена вручную")
                print_matrix(data, "Введенная матрица")

            elif choice == '2':
                # Генерация случайной матрицы
                try:
                    n = int(input("Введите количество строк: "))
                    m = int(input("Введите количество столбцов: "))
                    
                    if n <= 0 or m <= 0:
                        raise InvalidInputError("Размеры матрицы должны быть положительными числами")
                    
                    data = generate_matrix(n, m)
                    result = None  # Сброс результата при изменении исходных данных
                    logging.info(f"Сгенерирована случайная матрица {n}x{m}")
                    print_matrix(data, "Сгенерированная матрица")
                    
                except ValueError:
                    raise InvalidInputError("Введите целые числа для размеров матрицы")

            elif choice == '3':
                # Поворот матрицы
                if data is None:
                    raise NoDataError(MESSAGES["no_data"])
                
                direction = input("Введите направление поворота ('clockwise' или 'counterclockwise'): ").strip().lower()
                
                if direction not in ['clockwise', 'counterclockwise']:
                    raise InvalidInputError("Направление поворота должно быть 'clockwise' или 'counterclockwise'")
                
                result = rotate_matrix(data, direction)
                logging.info(f"Матрица повернута в направлении: {direction}")
                print_matrix(result, "Повернутая матрица")

            elif choice == '4':
                # Вывод результата
                if result is None:
                    raise AlgorithmNotExecutedError(MESSAGES["algorithm_not_executed"])
                
                print_matrix(result, "Результат операции")
                logging.info("Результат выведен на экран")

            elif choice == '5':
                # Выход из программы
                print(MESSAGES["exit"])
                logging.info("Программа завершена пользователем")
                break

            else:
                print(MESSAGES["invalid_choice"])
                logging.warning(f"Неверный выбор меню: {choice}")
        
        except (NoDataError, InvalidInputError, AlgorithmNotExecutedError) as e:
            print(f"Ошибка: {e}")
            logging.warning(f"{type(e).__name__}: {e}")
        except KeyboardInterrupt:
            print("\nПрограмма прервана пользователем")
            logging.critical("Программа прервана через KeyboardInterrupt")
            break
        except Exception as e:
            print(f"Произошла непредвиденная ошибка: {e}")
            logging.error(f"Необработанное исключение: {e}", exc_info=True)


if __name__ == "__main__":
    main()