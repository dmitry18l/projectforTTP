"""
Модуль для генерации случайных матриц.
"""

import random


def generate_matrix(rows, cols, min_val=1, max_val=100):
    """
    Генерирует случайную матрицу указанного размера.
    
    Args:
        rows: Количество строк
        cols: Количество столбцов
        min_val: Минимальное значение элемента
        max_val: Максимальное значение элемента
        
    Returns:
        Случайная матрица указанного размера
    """
    return [
        [random.randint(min_val, max_val) for _ in range(cols)]
        for _ in range(rows)
    ]