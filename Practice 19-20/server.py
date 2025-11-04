import logging
import time
import random
from matrix_input import input_matrix
from matrix_generate import generate_matrix
from matrix_rotate import rotate_matrix

# Настройка логирования сервера
logging.basicConfig(
    filename="server.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Server:
    """Эмуляция сервера для обработки запросов"""

    def process_input_matrix(self, client_name):
        logging.info(f"{client_name}: запрошен ввод матрицы")
        print(f"{client_name}: запрошен ввод матрицы")
        data = input_matrix()
        time.sleep(random.uniform(0.5, 2))  # имитация долгой операции
        logging.info(f"{client_name}: матрица введена вручную")
        return data

    def process_generate_matrix(self, client_name, n, m):
        logging.info(f"{client_name}: запрошена генерация матрицы {n}x{m}")
        print(f"{client_name}: запрошена генерация матрицы {n}x{m}")
        data = generate_matrix(n, m)
        time.sleep(random.uniform(0.5, 2))
        logging.info(f"{client_name}: матрица сгенерирована")
        return data

    def process_rotate_matrix(self, client_name, data, direction):
        logging.info(f"{client_name}: запрошен поворот матрицы {direction}")
        print(f"{client_name}: запрошен поворот матрицы {direction}")
        result = rotate_matrix(data, direction)
        time.sleep(random.uniform(0.5, 2))
        logging.info(f"{client_name}: матрица повернута")
        return result
