"""
Модуль сервера для выполнения матричных операций.

Сервер обрабатывает запросы от клиентов на выполнение операций с матрицами.
Эмулирует длительные вычисления для демонстрации работы с I/O-bound
операциями в многопоточной среде.
"""

import logging
import time
import random
import threading
from matrix_operations import rotate_matrix


class MatrixServer:
    """
    Класс сервера для обработки матричных операций.
    
    Сервер работает в одном потоке и обрабатывает запросы от многопоточных
    клиентов. Эмулирует длительные вычисления (2-5 секунд) для демонстрации
    работы GIL при I/O операциях.
    
    Attributes:
        requests_processed (int): Счетчик успешно обработанных запросов
        lock (threading.Lock): Блокировка для потокобезопасности
    """
    
    def __init__(self):
        """
        Инициализирует сервер и настраивает систему логирования.
        """
        self.requests_processed = 0
        self.lock = threading.Lock()
        
        # Настройка логирования
        logging.basicConfig(
            filename="Practice 19-20/server.log",
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
            encoding='utf-8'
        )
        
        logging.info("Сервер матричных операций инициализирован")
        print("Сервер: инициализирован и готов к обработке запросов")
    
    def process_request(self, request, client_name):
        """
        Обрабатывает запрос на матричную операцию с эмуляцией вычислений.
        
        Args:
            request (dict): Словарь с данными запроса
            client_name (str): Идентификатор клиента
            
        Returns:
            dict: Результат операции или сообщение об ошибке
        """
        try:
            operation = request.get('operation')
            matrix = request.get('matrix')
            direction = request.get('direction')
            
            # Логирование начала обработки с деталями запроса
            logging.info(f"Сервер {client_name}: получен запрос на операцию '{operation}'")
            logging.info(f"Сервер {client_name}: направление поворота - {direction}")
            logging.info(f"Сервер {client_name}: размер матрицы - {len(matrix)}x{len(matrix[0])}")
            
            print(f"{time.strftime('%H:%M:%S')} {client_name}: получен запрос на поворот матрицы")
            
            # Эмуляция длительных вычислений (2-5 секунд)
            processing_time = random.uniform(2, 5)
            logging.info(f"Сервер {client_name}: эмуляция вычислений {processing_time:.2f} сек")
            time.sleep(processing_time)  # I/O операция - GIL освобождается
            
            if operation == 'rotate':
                # Валидация входных данных
                if not matrix:
                    error_msg = "Матрица не предоставлена"
                    logging.error(f"Сервер {client_name}: {error_msg}")
                    return {'error': error_msg}
                
                if direction not in ['clockwise', 'counterclockwise']:
                    error_msg = f"Неверное направление поворота: {direction}"
                    logging.error(f"Сервер {client_name}: {error_msg}")
                    return {'error': error_msg}
                
                # Логирование перед выполнением операции
                logging.info(f"Сервер {client_name}: выполнение операции поворота")
                
                # Выполнение матричной операции
                result = rotate_matrix(matrix, direction)
                
                # Потокобезопасное обновление счетчика
                with self.lock:
                    self.requests_processed += 1
                
                # Логирование успешного завершения с деталями
                logging.info(f"Сервер {client_name}: операция поворота завершена успешно")
                logging.info(f"Сервер {client_name}: размер результата - {len(result)}x{len(result[0])}")
                logging.info(f"Сервер {client_name}: общее время обработки - {processing_time:.2f} сек")
                logging.info(f"Сервер {client_name}: всего обработано запросов - {self.requests_processed}")
                
                print(f"{time.strftime('%H:%M:%S')} {client_name}: выполнен поворот матрицы")
                
                return {'result': result}
            else:
                error_msg = f'Неподдерживаемая операция: {operation}'
                logging.error(f"Сервер {client_name}: {error_msg}")
                return {'error': error_msg}
                
        except Exception as e:
            # Обработка и логирование непредвиденных ошибок
            error_msg = f"Ошибка выполнения операции: {e}"
            logging.error(f"Сервер {client_name}: {error_msg}")
            logging.exception(f"Сервер {client_name}: детали исключения")  # Добавляет traceback
            return {'error': error_msg}


# Глобальный экземпляр сервера
server_instance = MatrixServer()