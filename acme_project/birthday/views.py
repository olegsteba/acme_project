# from django.shortcuts import get_object_or_404, redirect, render
# from django.core.paginator import Paginator
from django.views.generic import (
    ListView, DetailView,
    CreateView, UpdateView, DeleteView
)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .forms import BirthdayForm
from .models import Birthday
# Импортируем из utils.py функцию для подсчёта дней.
from .utils import calculate_birthday_countdown


class BirthdayMixin:
    model = Birthday


class BirthdayFormMixin:
    form_class = BirthdayForm


class OnlyAuthorMixin(UserPassesTestMixin):

    def test_func(self):
        object = self.get_object()
        return object.author == self.request.user


class BirthdayDetailView(BirthdayMixin, DetailView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['birthday_countdown'] = calculate_birthday_countdown(
            self.object.birthday
        )
        return context


class BirthdayCreateView(LoginRequiredMixin, BirthdayMixin, BirthdayFormMixin, CreateView):

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BirthdayUpdateView(OnlyAuthorMixin, LoginRequiredMixin, BirthdayMixin, BirthdayFormMixin, UpdateView):
    pass


class BirthdayDeleteView(OnlyAuthorMixin, LoginRequiredMixin, BirthdayMixin, DeleteView):
    success_url = reverse_lazy('birthday:list')


class BirthdayListView(ListView):
    model = Birthday
    ordering = 'id'
    paginate_by = 2


# def birthday(request, pk=None):
#     # Если в запросе указан pk
#     if pk is not None:
#         instance = get_object_or_404(Birthday, pk=pk)
#     else:
#         instance = None

#     # Передаем в форму либо данные из запроса, либо None.
#     # В случае редактирования прикрепляем объект модели.
#     form = BirthdayForm(
#         request.POST or None,
#         files=request.FILES or None,
#         instance=instance,
#     )
#     # Создаём словарь контекста сразу после инициализации формы.
#     context = {'form': form}
#     # Если форма валидна...
#     if form.is_valid():
#         form.save()
#         # ...вызовем функцию подсчёта дней:
#         birthday_countdown = calculate_birthday_countdown(
#             # ...и передаём в неё дату из словаря cleaned_data.
#             form.cleaned_data['birthday']
#         )
#         # Обновляем словарь контекста: добавляем в него новый элемент.
#         context.update({'birthday_countdown': birthday_countdown})
#     return render(request, 'birthday/birthday.html', context)


# def birthday_list(request):
#     birthdays = Birthday.objects.order_by('id')
#     paginator = Paginator(birthdays, 2)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     context = {'page_obj': page_obj}
#     return render(request, 'birthday/birthday_list.html', context=context)


# def birthday_delete(request, pk):
#     # Получаем объект модели или выбразываенм 404
#     instance = get_object_or_404(Birthday, pk=pk)
#     # В форму передаем только объект модели;
#     # передавать в форму параметры запроса не нужно.
#     form = BirthdayForm(instance=instance)
#     context = {'form': form}
#     # Если был получен POST-запрос
#     if request.method == 'POST':
#         instance.delete()
#         return redirect('birthday:list')
#     # Если был получен GET-запрос - отправляем форму
#     return render(request, 'birthday/birthday.html', context=context)
