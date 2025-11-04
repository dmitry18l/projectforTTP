def rotate_matrix(matrix, direction='clockwise'):
    """
    Поворачивает матрицу на 90 градусов.
    direction: 'clockwise' или 'counterclockwise'
    """
    if not matrix or not matrix[0]:
        return []

    if direction == 'clockwise':
        # Поворот по часовой стрелке
        return [list(reversed(col)) for col in zip(*matrix)]
    elif direction == 'counterclockwise':
        # Поворот против часовой стрелки
        return [list(col) for col in reversed(list(zip(*matrix)))]
    else:
        raise ValueError("direction должен быть 'clockwise' или 'counterclockwise'")
