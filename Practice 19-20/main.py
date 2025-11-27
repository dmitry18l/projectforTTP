"""
Главный модуль для автоматической демонстрации многопоточного клиент-серверного взаимодействия.

Модуль реализует автоматическую демонстрацию работы многопоточности
с использованием клиент-серверной архитектуры для операций с матрицами.
Клиенты автоматически выполняют заранее определенные последовательности
операций, эмулируя работу пользователей без ручного ввода.

Основные возможности:
    - Автоматический запуск multiple клиентов в отдельных потоках
    - Предопределенные сценарии работы для каждого клиента
    - Демонстрация параллельной обработки запросов сервером
    - Визуализация работы GIL при I/O-bound операциях
    - Статистика эффективности многопоточности

Используемые модули:
    time - для управления временными задержками
    threading - для работы с потоками
    server - модуль сервера матричных операций
    client - базовый класс клиента матричных операций
"""

import time
import threading
from server import server_instance
from client import MatrixClient


class Client(MatrixClient):
    """
    Клиент с автоматическим выполнением команд.
    
    Наследует функциональность базового клиента и добавляет
    возможность автоматического выполнения заранее определенной
    последовательности матричных операций.
    
    Attributes:
        client_name (str): Уникальное имя клиента для идентификации
        server (MatrixServer): Ссылка на сервер для обработки запросов
        commands (list): Список команд для автоматического выполнения
        command_index (int): Текущий индекс выполняемой команды
    """
    
    def __init__(self, client_name, server, commands):
        """
        Инициализирует клиента с набором команд.
        
        Args:
            client_name (str): Уникальное имя клиента для логирования
            server (MatrixServer): Экземпляр сервера для обработки запросов
            commands (list): Список команд в формате словарей:
                - type (str): Тип операции ('generate', 'rotate', 'show')
                - rows/cols/direction: Параметры операции
        """
        super().__init__(client_name, server)
        self.commands = commands
        self.command_index = 0
    
    def run(self):
        """
        Главный метод потока с автоматическим выполнением команд.
        
        Последовательно выполняет все команды из commands
        с задержками между операциями для наглядности демонстрации.
        Каждая команда выполняется в отдельном временном интервале,
        что позволяет наблюдать параллельную работу клиентов.
        """
        print(f"{time.strftime('%H:%M:%S')} {self.client_name}: клиент запущен")
        
        for command in self.commands:
            # Пауза между командами для наглядности параллельной работы
            time.sleep(1)
            
            if command['type'] == 'generate':
                self.generate_matrix(command['rows'], command['cols'])
            elif command['type'] == 'rotate':
                self.rotate_matrix(command['direction'])
            elif command['type'] == 'show':
                self.show_result()
        
        print(f"{time.strftime('%H:%M:%S')} {self.client_name}: выполнение завершено")
    
    def generate_matrix(self, rows, cols):
        """
        Автоматически генерирует матрицу с последовательными значениями.
        
        Создает матрицу указанного размера с последовательными числовыми
        значениями для удобства визуальной проверки правильности операций.
        
        Args:
            rows (int): Количество строк генерируемой матрицы
            cols (int): Количество столбцов генерируемой матрицы
        """
        # Генерация матрицы с последовательными значениями 1, 2, 3...
        self.data = [
            [i * cols + j + 1 for j in range(cols)]
            for i in range(rows)
        ]
        self.result = None
        print(f"{time.strftime('%H:%M:%S')} {self.client_name}: сгенерированы данные")
        self.print_matrix(self.data, "Сгенерированная матрица")
    
    def rotate_matrix(self, direction):
        """
        Автоматически отправляет запрос на поворот матрицы серверу.
        
        Формирует и отправляет запрос на поворот текущей матрицы
        в указанном направлении, обрабатывает ответ сервера.
        
        Args:
            direction (str): Направление поворота ('clockwise' или 'counterclockwise')
        """
        if self.data is None:
            print(f"{time.strftime('%H:%M:%S')} {self.client_name}: ошибка - нет данных")
            return
        
        # Формирование запроса к серверу
        request = {
            'operation': 'rotate',
            'matrix': self.data,
            'direction': direction,
            'client_name': self.client_name
        }
        
        print(f"{time.strftime('%H:%M:%S')} {self.client_name}: отправлен запрос на поворот матрицы")
        
        # Отправка запроса и обработка ответа
        response = self.server.process_request(request, self.client_name)
        
        if 'error' in response:
            print(f"{time.strftime('%H:%M:%S')} {self.client_name}: ошибка сервера - {response['error']}")
        else:
            self.result = response['result']
            print(f"{time.strftime('%H:%M:%S')} {self.client_name}: получен результат поворота")
            self.print_matrix(self.result, "Результат поворота")
    
    def show_result(self):
        """
        Автоматически отображает результат последней операции.
        
        Выводит в консоль матрицу-результат предыдущей операции.
        Если операция не выполнялась, выводит сообщение об ошибке.
        """
        if self.result is None:
            print(f"{time.strftime('%H:%M:%S')} {self.client_name}: ошибка - нет результата")
            return
        
        self.print_matrix(self.result, "Результат операции")
    
    def print_matrix(self, matrix, title="Матрица"):
        """
        Выводит матрицу в консоль в форматированном виде.
        
        Args:
            matrix (list): Матрица для отображения
            title (str): Заголовок для вывода
        """
        print(f"\n{title}:")
        for row in matrix:
            print(row)


def demonstrate_threading():
    """
    Демонстрирует основные концепции многопоточности в Python.
    
    Выводит информацию о текущем состоянии потоков и объясняет
    архитектуру демонстрируемой системы для лучшего понимания
    принципов работы многопоточности.
    """
    print("=" * 60)
    print("ДЕМОНСТРАЦИЯ МНОГОПОТОЧНОСТИ В PYTHON")
    print("=" * 60)
    print("Сервер: один поток")
    print("Клиенты: каждый в отдельном потоке") 
    print("=" * 60)
    
    # Отображение информации о текущих потоках
    print(f"Основной поток: ID {threading.get_ident()}")
    print(f"Активные потоки: {threading.active_count()}\n")


def main():
    """
    Главная функция автоматической демонстрации многопоточности.
    
    Организует полный цикл демонстрации:
    1. Создание клиентов с predefined сценариями
    2. Параллельный запуск клиентов в отдельных потоках
    3. Наблюдение за параллельной обработкой запросов
    4. Сбор и отображение статистики выполнения
    
    Демонстрирует эффективность многопоточности при обработке
    I/O-bound операций с длительными задержками.
    """
    demonstrate_threading()
    
    # Предопределенные сценарии работы для каждого клиента
    client1_commands = [
        {'type': 'generate', 'rows': 2, 'cols': 2},
        {'type': 'rotate', 'direction': 'clockwise'},
        {'type': 'show'}
    ]
    
    client2_commands = [
        {'type': 'generate', 'rows': 3, 'cols': 3},
        {'type': 'rotate', 'direction': 'counterclockwise'},
        {'type': 'show'}
    ]
    
    client3_commands = [
        {'type': 'generate', 'rows': 4, 'cols': 2},
        {'type': 'rotate', 'direction': 'clockwise'},
        {'type': 'show'}
    ]
    
    # Создание клиентов
    clients = [
        Client("Клиент1", server_instance, client1_commands),
        Client("Клиент2", server_instance, client2_commands),
        Client("Клиент3", server_instance, client3_commands)
    ]
    
    print("Запуск автоматической демонстрации...")
    print("Клиенты будут выполнять команды автоматически\n")
    
    # Параллельный запуск клиентов в отдельных потоках
    for client in clients:
        client.start()
        time.sleep(0.5)  # Задержка для стабильного запуска
    
    print(f"Запущено клиентов: {len(clients)}")
    print(f"Всего активных потоков: {threading.active_count()}")
    print("\nНаблюдайте за параллельной работой клиентов!\n")
    
    # Ожидание завершения всех клиентов
    try:
        for client in clients:
            client.join()
    except KeyboardInterrupt:
        print("\nДемонстрация прервана...")
    
    # Отображение финальной статистики
    print(f"\nСервер обработал {server_instance.requests_processed} запросов")


if __name__ == "__main__":
    main()