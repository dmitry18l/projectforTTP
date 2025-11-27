"""
Модуль пользовательских исключений для работы с матрицами.
"""


class MatrixError(Exception):
    """Базовое исключение для всех ошибок, связанных с работой с матрицами."""
    pass


class NoDataError(MatrixError):
    """Исключение для случаев, когда выбрано действие без введённых данных."""
    pass


class InvalidInputError(MatrixError):
    """Исключение для случаев ввода некорректных значений пользователем."""
    pass


class AlgorithmNotExecutedError(MatrixError):
    """Исключение для попытки вывода результата до выполнения алгоритма."""
    pass