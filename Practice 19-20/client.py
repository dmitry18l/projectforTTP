"""
Модуль клиента для взаимодействия с сервером матричных операций.

Предоставляет функциональность клиента для работы с матричными операциями
в многопоточной среде. Каждый клиент работает в отдельном потоке и 
предоставляет пользовательский интерфейс для выполнения операций с матрицами.

Основные возможности:
    - Ручной ввод матриц с валидацией данных
    - Генерация случайных матриц заданного размера
    - Отправка запросов на поворот матриц серверу
    - Просмотр результатов выполненных операций
    - Синхронизированный вывод в консоль для многопоточной работы

Используемые модули:
    threading - для работы с потоками и синхронизации
    time - для временных меток операций
    matrix_input - функции для ручного ввода матриц
    matrix_generate - функции для генерации случайных матриц
"""

import threading
import time
from matrix_input import input_matrix
from matrix_generate import generate_matrix


class MatrixClient(threading.Thread):
    """
    Класс клиента для работы с матричными операциями в многопоточной среде.
    
    Каждый экземпляр клиента работает в отдельном потоке и предоставляет
    пользовательский интерфейс для выполнения операций с матрицами.
    Клиент взаимодействует с сервером для выполнения ресурсоемких операций.
    
    Attributes:
        client_name (str): Уникальное имя клиента для идентификации в логах
        data (list): Текущая матрица клиента в виде списка списков
        result (list): Результат последней выполненной операции
        server (MatrixServer): Ссылка на сервер для обработки запросов
        lock (threading.Lock): Блокировка для синхронизации вывода в консоль
    """
    
    def __init__(self, client_name, server):
        """
        Инициализирует клиента с указанным именем и ссылкой на сервер.
        
        Args:
            client_name (str): Уникальное имя клиента для идентификации
            server (MatrixServer): Экземпляр сервера для обработки запросов
        """
        super().__init__()
        self.client_name = client_name
        self.data = None
        self.result = None
        self.server = server
        self.daemon = True
        self.lock = threading.Lock()  # Блокировка для синхронизации вывода
    
    def run(self):
        """
        Главный метод потока, запускающий интерактивный режим клиента.
        
        Обеспечивает бесконечный цикл взаимодействия с пользователем,
        обрабатывает команды меню и управляет жизненным циклом клиента.
        Все операции защищены обработкой исключений для устойчивой работы.
        """
        print(f"{time.strftime('%H:%M:%S')} {self.client_name}: клиент запущен")
        
        while True:
            try:
                with self.lock:
                    self.show_menu()
                    choice = input(f"Введите команду для {self.client_name}: ").strip()
                
                if choice == '1':
                    self.handle_manual_input()
                elif choice == '2':
                    self.handle_generate_matrix()
                elif choice == '3':
                    self.handle_rotate_matrix()
                elif choice == '4':
                    self.handle_show_result()
                elif choice == '5':
                    print(f"{time.strftime('%H:%M:%S')} {self.client_name}: выход из программы")
                    break
                else:
                    with self.lock:
                        print("Неверный выбор, попробуйте снова.")
                    
            except Exception as e:
                with self.lock:
                    print(f"Ошибка в клиенте {self.client_name}: {e}")
    
    def show_menu(self):
        """
        Отображает главное меню клиента с доступными операциями.
        
        Выводит форматированное меню с номерами операций и их описаниями.
        Меню включает все основные операции работы с матрицами.
        """
        print(f"\n=== Клиент {self.client_name} ===")
        print("1. Ручной ввод матрицы")
        print("2. Генерация случайной матрицы")
        print("3. Поворот матрицы")
        print("4. Вывод результата")
        print("5. Выход")
        print("=" * 25)
    
    def handle_manual_input(self):
        """
        Обрабатывает ручной ввод матрицы от пользователя.
        
        Запрашивает у пользователя размеры матрицы и поэлементный ввод,
        выполняет валидацию вводимых данных и сохраняет матрицу для
        последующих операций.
        """
        with self.lock:
            self.data = input_matrix()
            self.result = None
            print(f"{time.strftime('%H:%M:%S')} {self.client_name}: матрица введена вручную")
            self.print_matrix(self.data, "Введенная матрица")
    
    def handle_generate_matrix(self):
        """
        Обрабатывает генерацию случайной матрицы заданного размера.
        
        Запрашивает у пользователя размеры матрицы, генерирует матрицу
        со случайными значениями и сохраняет ее для последующих операций.
        Выполняет валидацию вводимых размеров матрицы.
        """
        with self.lock:
            try:
                n = int(input("Введите количество строк: "))
                m = int(input("Введите количество столбцов: "))
                
                if n <= 0 or m <= 0:
                    print("Ошибка: Размеры матрицы должны быть положительными числами")
                    return
                
                self.data = generate_matrix(n, m)
                self.result = None
                print(f"{time.strftime('%H:%M:%S')} {self.client_name}: сгенерированы данные")
                self.print_matrix(self.data, "Сгенерированная матрица")
                
            except ValueError:
                print("Ошибка: Введите целые числа для размеров матрицы")
    
    def handle_rotate_matrix(self):
        """
        Отправляет запрос на поворот матрицы серверу.
        
        Проверяет наличие данных матрицы, запрашивает направление поворота
        и отправляет асинхронный запрос на сервер. Обрабатывает ответ
        сервера и сохраняет результат операции.
        """
        if self.data is None:
            with self.lock:
                print("Ошибка: Сначала введите или сгенерируйте матрицу!")
            return
        
        with self.lock:
            direction = input("Введите направление поворота ('clockwise' или 'counterclockwise'): ").strip().lower()
        
        if direction not in ['clockwise', 'counterclockwise']:
            with self.lock:
                print("Ошибка: Направление поворота должно быть 'clockwise' или 'counterclockwise'")
            return
        
        # Формирование запроса для сервера
        request = {
            'operation': 'rotate',
            'matrix': self.data,
            'direction': direction,
            'client_name': self.client_name
        }
        
        with self.lock:
            print(f"{time.strftime('%H:%M:%S')} {self.client_name}: отправлен запрос на поворот матрицы")
        
        # Асинхронная отправка запроса серверу
        response = self.server.process_request(request, self.client_name)
        
        # Обработка ответа от сервера
        if 'error' in response:
            with self.lock:
                print(f"Ошибка сервера: {response['error']}")
        else:
            self.result = response['result']
            with self.lock:
                print(f"{time.strftime('%H:%M:%S')} {self.client_name}: получен результат поворота")
                self.print_matrix(self.result, "Результат поворота")
    
    def handle_show_result(self):
        """
        Отображает результат последней выполненной операции.
        
        Выводит матрицу-результат предыдущей операции поворота.
        Если операция не выполнялась, выводит соответствующее сообщение.
        """
        if self.result is None:
            with self.lock:
                print("Ошибка: Сначала выполните операцию поворота!")
            return
        
        with self.lock:
            self.print_matrix(self.result, "Результат операции")
    
    def print_matrix(self, matrix, title="Матрица"):
        """
        Выводит матрицу в консоль в читаемом формате.
        
        Args:
            matrix (list): Матрица для вывода в виде списка списков
            title (str): Заголовок для отображения над матрицей
        """
        print(f"\n{title}:")
        for row in matrix:
            print(row)