from django.db import connection
from django.http import HttpRequest, HttpResponse
from django.views.generic import TemplateView

from menu_app.models import MenuItem


class MenuView(TemplateView):
    """
    Класс представления для вывода main.html
    """

    template_name = "menu_app/main.html"
