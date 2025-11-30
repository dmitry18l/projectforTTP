"""
Главный модуль приложения для работы с матрицами с использованием автоматного программирования.

States:
    NO_DATA: Начальное состояние - матрица не введена
    HAS_DATA: Матрица введена, но операция не выполнена  
    HAS_RESULT: Матрица введена и операция выполнена
    EXIT: Финальное состояние - завершение работы

Пример использования:
    >>> python main.py
    ==================== Главное меню ====================
    1. Ручной ввод матрицы
    2. Генерация случайной матрицы
    3. Поворот матрицы
    4. Вывод результата
    5. Выход
    ======================================================
"""

import logging
from exceptions import NoDataError, InvalidInputError, AlgorithmNotExecutedError
from messages import MESSAGES
from matrix_input import input_matrix
from matrix_generate import generate_matrix
from matrix_rotate import rotate_matrix


# Настройка логирования
logging.basicConfig(
    filename="Practice 21-22/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class AppState:
    """
    Класс для управления состоянием приложения в рамках конечного автомата.
    
    Инкапсулирует текущее состояние приложения и данные, обеспечивая
    целостность переходов между состояниями.
    
    Attributes:
        state: Текущее состояние автомата. Возможные значения:
            - 'NO_DATA': матрица не введена
            - 'HAS_DATA': матрица введена, результат отсутствует  
            - 'HAS_RESULT': есть и матрица и результат
        data: Текущая матрица для операций или None если не инициализирована
        result: Результат последней операции или None если операция не выполнялась
    """
    
    def __init__(self):
        """Инициализирует приложение в начальном состоянии NO_DATA."""
        self.state = "NO_DATA"
        self.data = None
        self.result = None
    
    def get_state_dict(self):
        """
        Возвращает текущее состояние в виде словаря для автомата.
        
        Returns:
            Словарь с ключами:
                - 'data': текущая матрица
                - 'result': результат последней операции
                
        Note:
            Используется автоматом для принятия решений о переходах.
        """
        return {
            'data': self.data,
            'result': self.result
        }
    
    def update_state(self, new_state, data=None, result=None):
        """
        Обновляет состояние приложения.
        
        Args:
            new_state: Новое состояние автомата
            data: Новая матрица (опционально)
            result: Новый результат операции (опционально)
            
        Note:
            Если data или result не указаны, сохраняются предыдущие значения.
            При смене данных сбрасывается результат предыдущих операций.
        """
        self.state = new_state
        if data is not None:
            self.data = data
        if result is not None:
            self.result = result


def show_menu():
    """
    Отображает главное меню приложения в консоли.
    
    Использует текстовые сообщения из словаря MESSAGES для обеспечения
    единообразия интерфейса. Меню включает все доступные операции с матрицами.
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
    """
    print(f"\n{title}:")
    for row in matrix:
        print(row)


def handle_manual_input():
    """
    Обрабатывает ручной ввод матрицы пользователем.
    
    Returns:
        Введенная пользователем матрица в виде списка списков
        
    Side effects:
        - Запрашивает ввод у пользователя через консоль
        - Логирует операцию в файл app.log
        - Выводит результат в консоль
        
    Example:
        >>> matrix = handle_manual_input()
        Введите количество строк: 2
        Введите количество столбцов: 2
        Введите элемент [0, 0]: 1
        Введите элемент [0, 1]: 2
        Введите элемент [1, 0]: 3
        Введите элемент [1, 1]: 4
    """
    matrix = input_matrix()
    logging.info("Матрица введена вручную")
    print_matrix(matrix, "Введенная матрица")
    return matrix


def handle_generate_matrix():
    """
    Обрабатывает генерацию случайной матрицы заданного размера.
    
    Returns:
        Сгенерированная матрица заданного размера со случайными значениями
        
    Raises:
        InvalidInputError: Если размеры матрицы не положительные числа
        InvalidInputError: Если введены не целые числа для размеров
        
    Side effects:
        - Запрашивает размеры матрицы у пользователя
        - Логирует операцию с указанием размеров
        - Выводит результат в консоль
    """
    try:
        n = int(input("Введите количество строк: "))
        m = int(input("Введите количество столбцов: "))
        
        if n <= 0 or m <= 0:
            raise InvalidInputError("Размеры матрицы должны быть положительными числами")
        
        matrix = generate_matrix(n, m)
        logging.info(f"Сгенерирована случайная матрица {n}x{m}")
        print_matrix(matrix, "Сгенерированная матрица")
        return matrix
        
    except ValueError:
        raise InvalidInputError("Введите целые числа для размеров матрицы")


def handle_rotate_matrix(data):
    """
    Обрабатывает поворот матрицы на 90 градусов в указанном направлении.
    
    Args:
        data: Исходная матрица для поворота
        
    Returns:
        Повернутая матрица
        
    Raises:
        InvalidInputError: Если направление поворота некорректно
        
    Side effects:
        - Запрашивает направление поворота у пользователя
        - Логирует операцию с указанием направления
        - Выводит результат в консоль
    """
    direction = input("Введите направление поворота ('clockwise' или 'counterclockwise'): ").strip().lower()
    
    if direction not in ['clockwise', 'counterclockwise']:
        raise InvalidInputError("Направление поворота должно быть 'clockwise' или 'counterclockwise'")
    
    result = rotate_matrix(data, direction)
    logging.info(f"Матрица повернута в направлении: {direction}")
    print_matrix(result, "Повернутая матрица")
    return result


def handle_show_result(result):
    """
    Обрабатывает вывод результата последней операции.
    """
    print_matrix(result, "Результат операции")
    logging.info("Результат выведен на экран")


def handle_exit():
    """
    Обрабатывает корректный выход из программы.
    
    Side effects:
        - Выводит сообщение о выходе
        - Логирует завершение программы
        - Завершает выполнение главного цикла
    """
    print(MESSAGES["exit"])
    logging.info("Программа завершена пользователем")


# Конечный автомат приложения(ВСЯ ЛОГИКА В ОДНОМ СЛОВАРЕ)
APP_AUTOMATON = {
    # Состояние: NO_DATA - матрица не введена
    "NO_DATA": {
        "1": {  # Ручной ввод матрицы
            "action": "manual_input",
            "next_state": "HAS_DATA"
        },
        "2": {  # Генерация случайной матрицы
            "action": "generate_matrix", 
            "next_state": "HAS_DATA"
        },
        "3": {  # Поворот матрицы - НЕВОЗМОЖЕН
            "error": "no_data"
        },
        "4": {  # Вывод результата - НЕВОЗМОЖЕН
            "error": "algorithm_not_executed"
        },
        "5": {  # Выход
            "action": "exit",
            "next_state": "EXIT"
        }
    },
    
    # Состояние: HAS_DATA - матрица введена, результат не вычислен
    "HAS_DATA": {
        "1": {  # Ручной ввод матрицы
            "action": "manual_input",
            "next_state": "HAS_DATA"
        },
        "2": {  # Генерация случайной матрицы
            "action": "generate_matrix",
            "next_state": "HAS_DATA"
        },
        "3": {  # Поворот матрицы
            "action": "rotate_matrix",
            "next_state": "HAS_RESULT"
        },
        "4": {  # Вывод результата - НЕВОЗМОЖЕН
            "error": "algorithm_not_executed"
        },
        "5": {  # Выход
            "action": "exit", 
            "next_state": "EXIT"
        }
    },
    
    # Состояние: HAS_RESULT - есть и матрица и результат
    "HAS_RESULT": {
        "1": {  # Ручной ввод матрицы (сбрасывает результат)
            "action": "manual_input",
            "next_state": "HAS_DATA"
        },
        "2": {  # Генерация случайной матрицы (сбрасывает результат)
            "action": "generate_matrix",
            "next_state": "HAS_DATA"
        },
        "3": {  # Поворот матрицы
            "action": "rotate_matrix",
            "next_state": "HAS_RESULT"
        },
        "4": {  # Вывод результата
            "action": "show_result",
            "next_state": "HAS_RESULT"
        },
        "5": {  # Выход
            "action": "exit",
            "next_state": "EXIT"
        }
    }
}


# Словарь обработчиков действий
ACTION_HANDLERS = {
    "manual_input": handle_manual_input,
    "generate_matrix": handle_generate_matrix,
    "rotate_matrix": handle_rotate_matrix,
    "show_result": handle_show_result,
    "exit": handle_exit
}


def process_choice(app_state, choice):
    """
    Обрабатывает выбор пользователя на основе текущего состояния автомата.
    Вызывает соответствующие обработчики действий и обновляет состояние приложения.
    
    Args:
        app_state: Текущее состояние приложения
        choice: Выбор пользователя (строка от '1' до '5')
    
    Returns:
        True если нужно продолжить выполнение, False для выхода
        
    Raises:
        NoDataError: При попытке выполнить операцию без данных
        AlgorithmNotExecutedError: При попытке вывода несуществующего результата
        InvalidInputError: При некорректном выборе пункта меню
    """
    current_state = app_state.state
    
    # Получаем возможные действия для текущего состояния
    state_actions = APP_AUTOMATON.get(current_state, {})
    action_config = state_actions.get(choice)
    
    if not action_config:
        print(MESSAGES["invalid_choice"])
        logging.warning(f"Неверный выбор меню: {choice}")
        return True
    
    # Обработка ошибок
    if "error" in action_config:
        error_key = action_config["error"]
        if error_key == "no_data":
            raise NoDataError(MESSAGES["no_data"])
        elif error_key == "algorithm_not_executed":
            raise AlgorithmNotExecutedError(MESSAGES["algorithm_not_executed"])
    
    # Выполнение действия
    if "action" in action_config:
        action_name = action_config["action"]
        handler = ACTION_HANDLERS[action_name]
        
        # Вызываем соответствующий обработчик
        if action_name == "manual_input":
            new_data = handler()
            app_state.update_state(action_config["next_state"], data=new_data, result=None)
            
        elif action_name == "generate_matrix":
            new_data = handler()
            app_state.update_state(action_config["next_state"], data=new_data, result=None)
            
        elif action_name == "rotate_matrix":
            new_result = handler(app_state.data)
            app_state.update_state(action_config["next_state"], result=new_result)
            
        elif action_name == "show_result":
            handler(app_state.result)
            # Состояние не меняется при выводе результата
            
        elif action_name == "exit":
            handler()
            return False
    
    return True


def main():
    """
    Главная функция программы с автоматным управлением состоянием.
    
    Реализует основной цикл приложения, обрабатывает пользовательский ввод
    и управляет переходами между состояниями через конечный автомат.
    """
    app_state = AppState()
    logging.info("Программа запущена")

    while True:
        try:
            show_menu()
            choice = input("Выберите пункт меню: ").strip()
            logging.info(f"Пользователь выбрал пункт меню: {choice}")
            
            # Обработка выбора через автомат
            should_continue = process_choice(app_state, choice)
            if not should_continue:
                break
        
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