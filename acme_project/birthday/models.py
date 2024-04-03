from django.db import models


class Birthday(models.Model):
    first_name = models.CharField(
        verbose_name='Имя',
        max_length=20,
    )
    last_name = models.CharField(
        verbose_name='Фамилия',
        blank=True,
        help_text='Не обязательное поле',
        max_length=20,
    )
    birthday = models.DateField(
        verbose_name='Дата рождения',
    )

    class Meta:
        verbose_name = 'день рождения'
        verbose_name_plural = 'Дни рождения'

    def __str__(self):
        return self.first_name
