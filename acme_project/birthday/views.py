# birthday/views.py
from django.shortcuts import get_object_or_404, redirect, render

from .forms import BirthdayForm
from .models import Birthday
# Импортируем из utils.py функцию для подсчёта дней.
from .utils import calculate_birthday_countdown


def birthday(request, pk=None):
    # Если в запросе указан pk
    if pk is not None:
        instance = get_object_or_404(Birthday, pk=pk)
    else:
        instance = None

    # Передаем в форму либо данные из запроса, либо None.
    # В случае редактирования прикрепляем объект модели.
    form = BirthdayForm(request.POST or None, instance=instance)
    # Создаём словарь контекста сразу после инициализации формы.
    context = {'form': form}
    # Если форма валидна...
    if form.is_valid():
        form.save()
        # ...вызовем функцию подсчёта дней:
        birthday_countdown = calculate_birthday_countdown(
            # ...и передаём в неё дату из словаря cleaned_data.
            form.cleaned_data['birthday']
        )
        # Обновляем словарь контекста: добавляем в него новый элемент.
        context.update({'birthday_countdown': birthday_countdown})
    return render(request, 'birthday/birthday.html', context)


def birthday_list(request):
    birthdays = Birthday.objects.all()
    context = {'birthdays': birthdays}
    return render(request, 'birthday/birthday_list.html', context=context)


def birthday_delete(request, pk):
    # Получаем объект модели или выбразываенм 404
    instance = get_object_or_404(Birthday, pk=pk)
    # В форму передаем только объект модели;
    # передавать в форму параметры запроса не нужно.
    form = BirthdayForm(instance=instance)
    context = {'form': form}
    # Если был получен POST-запрос
    if request.method == 'POST':
        instance.delete()
        return redirect('birthday:list')
    # Если был получен GET-запрос - отправляем форму
    return render(request, 'birthday/birthday.html', context=context)
