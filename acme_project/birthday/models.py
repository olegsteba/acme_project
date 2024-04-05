from django.db import models
from django.urls import reverse
from .validators import real_age


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
        validators=(real_age,),
    )
    image = models.ImageField(
        verbose_name='Фото',
        upload_to='birthdays_images',
        blank=True,
    )

    class Meta:
        verbose_name = 'день рождения'
        verbose_name_plural = 'Дни рождения'

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse('birthday:detail', kwargs={'pk': self.pk})
