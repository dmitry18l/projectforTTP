import logging

def rotate_matrix(matrix, direction):
    """
    Поворот матрицы с обработкой ошибок.
    """
    try:
        logging.info(f"Функция rotate_matrix(direction={direction}) вызвана")

        if not matrix:
            raise ValueError("Матрица пуста — нечего поворачивать")

        if direction == "clockwise":
            rotated = [list(row) for row in zip(*matrix[::-1])]
        elif direction == "counterclockwise":
            rotated = [list(row) for row in zip(*matrix)][::-1]
        else:
            raise ValueError("Некорректное направление поворота. Используйте 'clockwise' или 'counterclockwise'.")

        logging.info("Функция rotate_matrix() завершила выполнение")
        return rotated

    except Exception as e:
        logging.error(f"Ошибка в rotate_matrix: {e}")
        print(f"Ошибка при повороте матрицы: {e}")
        return None
