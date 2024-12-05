from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from .views import home  # Импорт функции для главной страницы


# Главные маршруты проекта
urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),  # Административная панель Django
    path('users/', include('users.urls')),  # Маршруты приложения пользователей
    path('ads/', include('ads.urls')),  # Маршруты приложения объявлений
    path('', home, name='home'),  # Главная страница
)
urlpatterns += [
    path('i18n/', include('django.conf.urls.i18n')),
]

# Обработка медиафайлов в режиме DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Дополнительная обработка ошибок (опционально)
handler404 = 'olx_clone.views.page_not_found'
handler500 = 'olx_clone.views.server_error'
