def input_matrix():
    """
    Ввод матрицы пользователем вручную.
    Пользователь вводит размеры N и M, затем элементы построчно.
    Возвращает матрицу (список списков).
    """
    n = int(input("Введите количество строк (N): "))
    m = int(input("Введите количество столбцов (M): "))

    matrix = []
    print("Введите элементы матрицы построчно:")
    for i in range(n):
        row = list(map(int, input(f"Строка {i + 1}: ").split()))
        while len(row) != m:
            print(f"Ошибка: должно быть {m} элементов!")
            row = list(map(int, input(f"Строка {i + 1}: ").split()))
        matrix.append(row)
    return matrix
