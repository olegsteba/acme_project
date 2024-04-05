from django import forms
from django.core.exceptions import ValidationError

from .models import Birthday


BEATLES = {'Джон Леннон', 'Пол Маккартни', 'Джордж Харрисон', 'Ринго Старр'}


class BirthdayForm(forms.ModelForm):

    class Meta:
        model = Birthday
        fields = (
            'first_name',
            'last_name',
            'birthday',
            'image',
        )
        widgets = {
            'birthday': forms.DateInput(
                attrs={'type': 'date'}
            )
        }

    def clean_first_name(self):
        """Очищаем от мусора данные в first_name."""
        first_name = self.cleaned_data['first_name']
        return first_name.split()[0]

    def clean(self):
        """Проверка на взаимную зависимость first_name и last_name."""
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        # Проверяем вхождение сочетания имя и фамилия во множество BEATELS
        if f'{first_name} {last_name}' in BEATLES:
            raise ValidationError(
                'Мы тоже любим Битлс, но вветите настоящее имя!'
            )
