from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from .validators import real_age

User = get_user_model()


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
    author = models.ForeignKey(
        User,
        verbose_name='Автор записи',
        on_delete=models.CASCADE,
        null=True,
    )

    class Meta:
        verbose_name = 'день рождения'
        verbose_name_plural = 'Дни рождения'

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse('birthday:detail', kwargs={'pk': self.pk})


class Congratulation(models.Modedl):
    text = models.TextField(
        verbose_name='Текст поздравления',
    )
    birthday = models.ForeingKey(
        Birthday,
        on_delete=models.CASCADE,
        related_name='congratulations',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('created_at',)
