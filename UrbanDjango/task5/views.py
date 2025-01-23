from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister
# Create your views here.

def sign_up_by_django(req):
    users = {
        'user1': '123456',
        'user2': 'qwerty'
    }
    info = {}
    if req.method == "POST":
        form = UserRegister(req.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif username in users:
                info['error'] = 'Пользователь уже существует'
            else:
                info['message'] = f'Приветствуем, {username}!'
        else:
            info['form'] = form
    else:
        form = UserRegister()
    info['form'] = form
    return render(req, 'fifth_task/registration_page.html', info)


def sign_up_by_html(req):
    return sign_up_by_django(req)
# Реализация представления sign_up_by_html аналогична sign_up_by_django