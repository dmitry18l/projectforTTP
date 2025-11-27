"""
Модуль операций с матрицами.
Содержит функции для выполнения матричных операций.
"""


def rotate_matrix(matrix, direction):
    """
    Поворачивает матрицу на 90 градусов в указанном направлении.
    
    Args:
        matrix: Исходная матрица в виде списка списков
        direction: Направление поворота - 'clockwise' или 'counterclockwise'
    
    Returns:
        Повернутая матрица
    
    Raises:
        ValueError: Если направление поворота некорректно
    """
    if not matrix:
        return []
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    if direction == 'clockwise':
        # Поворот по часовой стрелке
        rotated = []
        for j in range(cols):
            new_row = []
            for i in range(rows-1, -1, -1):
                new_row.append(matrix[i][j])
            rotated.append(new_row)
        return rotated
    
    elif direction == 'counterclockwise':
        # Поворот против часовой стрелки
        rotated = []
        for j in range(cols-1, -1, -1):
            new_row = []
            for i in range(rows):
                new_row.append(matrix[i][j])
            rotated.append(new_row)
        return rotated
    
    else:
        raise ValueError("Некорректное направление поворота")