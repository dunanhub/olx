from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

# Получение пользовательской модели
User = get_user_model()

class Ad(models.Model):
    # Категории объявлений
    CATEGORY_CHOICES = [
        ('technics', 'Техника'),
        ('clothes', 'Одежда'),
        ('services', 'Услуги'),
        ('trend', 'Тренд'),
        ('tickets_and_others', 'Билеты и другое'),  # Привёл к корректному виду для slug
    ]

    # Поля модели
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default='tickets_and_others',
        verbose_name="Категория"
    )
    image = models.ImageField(
        upload_to='ad_images/', 
        blank=True, 
        null=True, 
        verbose_name="Изображение"
    )
    whatsapp_number = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        verbose_name="WhatsApp номер"
    )
    is_paid = models.BooleanField(default=False, verbose_name="Оплачено")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    kaspi_name = models.CharField(
        max_length=255, 
        blank=True, 
        null=True, 
        verbose_name="Имя в Kaspi"
    )
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='ads', 
        verbose_name="Пользователь"
    )

    # Для отображения в админке
    def _str_(self):
        return self.title

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
        ordering = ['-created_at']