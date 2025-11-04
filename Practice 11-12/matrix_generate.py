import random
import logging

def generate_matrix(n, m):
    """
    Генерация случайной матрицы с обработкой ошибок.
    """
    try:
        logging.info(f"Функция generate_matrix({n}, {m}) вызвана")

        if n <= 0 or m <= 0:
            raise ValueError("Размеры матрицы должны быть положительными")

        matrix = [[random.randint(0, 9) for _ in range(m)] for _ in range(n)]
        logging.info("Функция generate_matrix() завершила генерацию")
        return matrix

    except Exception as e:
        logging.error(f"Ошибка в generate_matrix: {e}")
        print("Произошла ошибка при генерации матрицы. Попробуйте снова.")
        return []
