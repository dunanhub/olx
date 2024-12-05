from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Ad
from .forms import AdForm
from django.contrib import messages  # Хабарламалар үшін

@login_required
def create_ad(request):
    """
    Функция для создания объявления.
    """
    if request.method == 'POST':
        # Получение данных из формы
        title = request.POST.get('title')
        description = request.POST.get('description')
        price = request.POST.get('price')
        image = request.FILES.get('image')
        category = request.POST.get('category')
        whatsapp_number = request.POST.get('whatsapp_number')

        # Создание объекта объявления с is_paid=False
        ad = Ad.objects.create(
            title=title,
            description=description,
            price=price,
            image=image,
            category=category,
            whatsapp_number=whatsapp_number,
            user=request.user,
            is_paid=False  # Объявление создается неоплаченным
        )
        return redirect('submit_kaspi', ad_id=ad.id)  # Перенаправление на оплату
    return render(request, 'ads/create_ad.html')  # Отображение формы создания объявления


@login_required
def submit_kaspi(request, ad_id):
    """
    Функция для обработки платежа Kaspi.
    """
    ad = get_object_or_404(Ad, id=ad_id, user=request.user)
    if request.method == 'POST':
        kaspi_name = request.POST.get('kaspi_name')  # Получение имени с Kaspi
        if not kaspi_name:
            messages.error(request, "Пожалуйста, введите имя Kaspi.")
            return render(request, 'ads/kaspi_payment.html', {'ad': ad})

        # Обновление объявления как оплаченное
        ad.kaspi_name = kaspi_name
        ad.is_paid = False
        ad.save()
        messages.success(request, "Ваше объявление успешно оплачено!")
        return render(request, 'ads/thanks.html', {'ad': ad})  # Благодарность
    return render(request, 'ads/kaspi_payment.html', {'ad': ad})  # Инструкция по оплате


def home(request):
    """
    Главная страница, отображающая оплаченные объявления.
    """
    category = request.GET.get('category')  # Получаем выбранную категорию из GET-запроса
    query = request.GET.get('q')  # Получаем поисковый запрос из GET-запроса

    # Фильтрация объявлений по статусу оплаты
    ads = Ad.objects.filter(is_paid=True)

    # Фильтрация по категории, если категория указана
    if category:
        ads = ads.filter(category=category)

    # Фильтрация по поисковому запросу, если он указан
    if query:
        ads = ads.filter(title__icontains=query)

    categories = Ad.CATEGORY_CHOICES  # Список категорий для фильтрации
    return render(request, 'home.html', {'ads': ads, 'categories': categories})  # Отображение главной страницы


@login_required
def delete_ad(request, ad_id):
    """
    Удаление объявления.
    """
    ad = get_object_or_404(Ad, id=ad_id, user=request.user)
    ad.delete()
    messages.success(request, "Объявление успешно удалено!")
    return redirect('home')

