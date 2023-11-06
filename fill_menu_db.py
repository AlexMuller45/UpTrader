import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "UpTrader.settings")

import django

django.setup()

from django.db import connection
from menu_app.models import MenuItem, Menu


white_label = ["Forex CRM", "MT Labels", "Web terminal"]
about = ["Our Contacts", "News", "Articles", "Events", "Our partners"]
services = ["Legal services", "Forex liquidity", "Custom development"]
contacts = []
news_items = ["yesterday", "today", "tomorrow"]

main_menu_items = {
    "White Label": white_label,
    "About": about,
    "Services": services,
    "Contacts": contacts,
}


def reset_autoincrement(model_name):
    table_name = f"menu_app_{model_name.lower()}"
    query = f"UPDATE sqlite_sequence SET seq = 0 WHERE name = '{table_name}';"
    with connection.cursor() as cursor:
        cursor.execute(query)


def create_item(item_list, parent, main_menu):
    if isinstance(item_list, list):
        for item in item_list:
            item_name = item.lower().replace(" ", "_")
            if parent:
                url = f"{parent.url}{item_name}/"
            else:
                url = f"/{item_name}/"

            MenuItem.objects.create(
                name=item,
                url=url,
                menu=main_menu,
                parent=parent,
            )


def fill_db():
    Menu.objects.all().delete()
    MenuItem.objects.all().delete()
    reset_autoincrement("Menu")
    reset_autoincrement("MenuItem")

    main_menu = Menu.objects.create(title="main_menu", url="")

    create_item(item_list=list(main_menu_items), parent=None, main_menu=main_menu)

    for menu_item in main_menu_items.keys():
        parent = MenuItem.objects.get(name=menu_item)
        create_item(main_menu_items[menu_item], parent, main_menu)

    parent = MenuItem.objects.get(name="News")
    create_item(news_items, parent, main_menu)


if __name__ == "__main__":
    print("Заполняем БД....")
    fill_db()
    print("Данные внесены")
