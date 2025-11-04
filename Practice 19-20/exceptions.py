class NoDataError(Exception):
    """Ошибка при попытке выполнить операцию без данных."""
    pass

class NoResultError(Exception):
    """Ошибка при попытке вывести результат до выполнения алгоритма."""
    pass

class InvalidInputError(Exception):
    """Ошибка при неверном вводе пользователя."""
    pass
