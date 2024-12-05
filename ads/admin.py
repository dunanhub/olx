from django.contrib import admin
from .models import Ad

@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price', 'category', 'is_paid', 'kaspi_name')
    list_editable = ('is_paid',)
    search_fields = ('title', 'description', 'kaspi_name')
# Register your models here.
