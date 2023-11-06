from django.urls import path, re_path
from menu_app.views import MenuView

app_name = "menu_app"


urlpatterns = [
    path("", MenuView.as_view(), name="main_menu"),
    path("<path:item_url>/", MenuView.as_view(), name="sub_menu"),
]
