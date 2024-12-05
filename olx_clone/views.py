from django.shortcuts import render
from ads.models import Ad

def home(request):
    ads = Ad.objects.filter(is_paid=True)
    return render(request, 'home.html', {'ads': ads})
# Обработчик для ошибки 404 (страница не найдена)
def page_not_found(request, exception):
    return render(request, '404.html', status=404)

# Обработчик для ошибки 500 (внутренняя ошибка сервера)
def server_error(request):
    return render(request, '500.html', status=500)