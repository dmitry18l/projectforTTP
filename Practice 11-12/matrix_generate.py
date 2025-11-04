import random

def generate_matrix(n, m, min_val=0, max_val=9):
    """
    Генерирует матрицу размером n x m с случайными целыми числами
    от min_val до max_val включительно.
    """
    matrix = [[random.randint(min_val, max_val) for _ in range(m)] for _ in range(n)]
    return matrix
