from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from ads.models import Ad
from django.contrib import messages

def register(request):
    """
    Представление для регистрации нового пользователя.
    """
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Вход нового пользователя
            messages.success(request, 'Ваш аккаунт был успешно создан!')
            return redirect('home')
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме.')
    else:
        form = CustomUserCreationForm()

    return render(request, 'users/register.html', {'form': form})

def login_user(request):
    """
    Представление для авторизации пользователя.
    """
    if request.method == 'POST':
        username = request.POST.get('username')  # Получение имени пользователя
        password = request.POST.get('password')  # Получение пароля
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)  # Вход пользователя
            messages.success(request, 'Вы успешно вошли в систему!')
            return redirect('home')
        else:
            messages.error(request, 'Неправильное имя пользователя или пароль.')

    return render(request, 'users/login.html')

@login_required
def profile(request):
    """
    Представление профиля пользователя, отображает его объявления.
    """
    user_ads = Ad.objects.filter(user=request.user)  # Фильтр объявлений по пользователю
    return render(request, 'users/profile.html', {'user_ads': user_ads})
