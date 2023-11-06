from django.contrib import admin
from menu_app.models import MenuItem

"""
Добавление элементов меню в админ-панель
"""
admin.site.register(MenuItem)
