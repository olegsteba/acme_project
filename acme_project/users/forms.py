# users/forms.py
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

# Получаем модель пользователя:


class RegisterForm(UserCreationForm):
    # Наследуем класс Meta от соответствующего класса родительской формы.
    # Так этот класс будет не перезаписан, а расширен.
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ('bio',)
