from django.conf import settings
from django.conf.urls.static import static

# Добавьте новые строчки с импортами классов.
from users.forms import RegisterForm
from django.views.generic.edit import CreateView

from django.contrib import admin
from django.contrib.auth import views
from django.urls import include, path, reverse_lazy

urlpatterns = [
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
    path('birthday/', include('birthday.urls')),
    # Подключаем urls.py приложения для работы с пользователями.
    path('auth/', include('django.contrib.auth.urls')),
    path(
        'reset/<uidb64>/<token>/',
        views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'
    ),
    path(
        'auth/registration/',
        CreateView.as_view(
            template_name='registration/registration_form.html',
            form_class=RegisterForm,
            success_url=reverse_lazy('pages:homepage'),
        ),
        name='registration',
    ),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
