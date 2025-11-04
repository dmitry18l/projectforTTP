# exceptions.py

class MatrixError(Exception):
    """Базовое исключение для работы с матрицами"""
    pass

class NoDataError(MatrixError):
    """Выбрано действие без введённых данных"""
    pass

class InvalidInputError(MatrixError):
    """Введено некорректное значение"""
    pass

class AlgorithmNotExecutedError(MatrixError):
    """Попытка вывода результата до выполнения алгоритма"""
    pass
