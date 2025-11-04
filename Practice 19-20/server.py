import logging
import time
import random
from matrix_operations import generate_matrix, rotate_matrix, input_matrix
from exceptions import NoDataError, NoResultError, InvalidInputError

# Настройка логирования
logging.basicConfig(
    filename="server.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def handle_client_request(client_name, action, **kwargs):
    """
    Обрабатывает запрос клиента.

    Args:
        client_name (str): имя клиента
        action (str): действие ('input', 'generate', 'rotate')
        kwargs: дополнительные параметры для действия

    Returns:
        list: результат действия (матрица или повернутая матрица)
    """
    try:
        logging.info(f"{client_name}: отправлен запрос '{action}'")
        time.sleep(random.uniform(0.5, 1.5))  # эмуляция длительных расчетов

        if action == "input":
            matrix = input_matrix()
            logging.info(f"{client_name}: матрица введена вручную")
            return matrix

        elif action == "generate":
            n = kwargs.get("n")
            m = kwargs.get("m")
            if n is None or m is None:
                raise InvalidInputError("Не указаны размеры матрицы для генерации")
            matrix = generate_matrix(n, m)
            logging.info(f"{client_name}: сгенерирована матрица {n}x{m}")
            return matrix

        elif action == "rotate":
            matrix = kwargs.get("matrix")
            direction = kwargs.get("direction")
            if matrix is None:
                raise NoDataError("Матрица не задана для поворота")
            if direction not in ('clockwise', 'counterclockwise'):
                raise InvalidInputError("Неверное направление поворота")
            rotated = rotate_matrix(matrix, direction)
            logging.info(f"{client_name}: матрица повернута {direction}")
            return rotated

        else:
            raise InvalidInputError(f"Неизвестное действие: {action}")

    except Exception as e:
        logging.error(f"{client_name}: ошибка при обработке запроса '{action}': {e}")
        raise
