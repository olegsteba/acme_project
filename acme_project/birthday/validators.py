# Импортируем класс для работы с датами
from datetime import date

# Импортируем ошибку валидации
from django.core.exceptions import ValidationError


def real_age(value: date) -> None:
    """
        Проверает дату рождения на валидность.
        Параметры: value - дата рождения.
        Если возраст не в диапозоне от 1 до 120 то выбрасывает ошибку.
    """
    age = (date.today() - value).days / 365
    if age < 1 or age > 120:
        raise ValidationError(
            'Ожидается возраст от 1 до 120 лет.'
        )
