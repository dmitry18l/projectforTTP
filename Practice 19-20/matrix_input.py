"""
Модуль для ручного ввода матриц.
"""


def input_matrix():
    """
    Обеспечивает ручной ввод матрицы от пользователя.
    
    Returns:
        Матрица в виде списка списков чисел
        
    Raises:
        ValueError: При вводе некорректных числовых значений
    """
    print("\nРучной ввод матрицы")
    rows = int(input("Введите количество строк: "))
    cols = int(input("Введите количество столбцов: "))
    
    matrix = []
    print("Введите элементы матрицы построчно:")
    
    for i in range(rows):
        while True:
            try:
                row_input = input(f"Строка {i+1} (через пробел): ")
                row = list(map(int, row_input.split()))
                
                if len(row) != cols:
                    print(f"Ошибка: должно быть {cols} элементов")
                    continue
                    
                matrix.append(row)
                break
            except ValueError:
                print("Ошибка: введите целые числа через пробел")
    
    return matrix