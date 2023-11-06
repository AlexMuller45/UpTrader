from django import template
from django.urls import reverse
from django.template import Context
from django.db import connection

from menu_app.models import MenuItem

register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context: Context, menu_name: str) -> str:
    """
    template tag для вывода дерева меню
    :param context: (Context)
    :param menu_name: (str) название меню, которое необходимо загрузить
    :return:
    """
    request = context["request"]
    current_url = request.path

    menu_items = MenuItem.objects.filter(menu__title=menu_name)
    menu_items_list = [item for item in menu_items.values()]
    menu_tree = build_tree_menu(menu_items_list[:], current_url)

    print("Количество обращений к БД: ", len(connection.queries))

    return _render_menu(menu_tree, current_url)


def _render_menu(menu_items: list[dict], current_url: str) -> str:
    """
    Вспомогательная функция, генерирует HTML для отображения меню
    :param menu_items: (list[dict]) список пунктов меню (дерево меню)
    :param current_url: (str) url открытой страницы
    :return: (str) текст в формате html
    """
    html = "<ul>"
    for item in menu_items:
        html += "<li>"
        item_url = _get_menu_item_url(item)

        if current_url == item_url:
            html += (
                f'<a style="text-decoration: none; '
                f"font-family: monospace; "
                f"border-top; "
                f"border-width: thin; "
                f"border-style: dotted; "
                f'color: red" '
                f'href="{item_url} ">'
                f"{item['name']}"
                f"</a>"
            )
        else:
            html += (
                f'<a style="text-decoration: none; '
                f'font-family: monospace;" '
                f'href="{item_url}">{item["name"]}</a>'
            )

        if "sub_menu" in item:
            html += _render_menu(item["sub_menu"], current_url)
        html += "</li>"

    html += "</ul>"

    return html


def _get_menu_item_url(menu_item: dict) -> str:
    """
    Вспомогательная функция возвращает адрес на который направляет пункт меню
    :param menu_item: (dict) элемент меню
    :return: (str) адрес url
    """
    if menu_item["url"].startswith("/"):
        return menu_item["url"]
    else:
        return reverse(menu_item["url"])


def build_tree_menu(
    data_list: list[dict], current_url: str, parent_id: int = None
) -> list[dict]:
    """
    Функция построения дерева меню до текущего пункта (определяется адресом открытой страницы)
    :param data_list: (list[dict]) список пунктов меню
    :param current_url: (str) адрес открытой страницы
    :param parent_id: (int) идентификатор вышестоящего уровня меню
    :return: (list[dict]) дерево меню
    """
    menu_tree = list()
    for item in data_list:
        if item["parent_id"] == parent_id:
            children = build_tree_menu(data_list, current_url, item["id"])
            if children and (item["url"] in current_url):
                item["sub_menu"] = children
            menu_tree.append(item)
    return menu_tree
