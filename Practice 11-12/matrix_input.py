import logging

def input_matrix():
    """
    Ручной ввод матрицы пользователем с обработкой ошибок.
    """
    try:
        logging.info("Функция input_matrix() вызвана")
        n = int(input("Введите количество строк: "))
        m = int(input("Введите количество столбцов: "))

        if n <= 0 or m <= 0:
            raise ValueError("Размеры матрицы должны быть положительными числами")

        matrix = []
        for i in range(n):
            try:
                row = list(map(int, input(f"Введите {m} чисел через пробел для строки {i+1}: ").split()))
                if len(row) != m:
                    raise ValueError("Количество элементов не совпадает с числом столбцов")
                matrix.append(row)
            except ValueError as e:
                logging.error(f"Ошибка ввода строки {i+1}: {e}")
                print("Ошибка ввода! Повторите попытку.")
                return input_matrix()  # повторный ввод

        logging.info("Функция input_matrix() завершила ввод матрицы")
        return matrix

    except ValueError as e:
        logging.error(f"Ошибка при вводе размеров матрицы: {e}")
        print("Ошибка ввода! Попробуйте снова.")
        return input_matrix()
