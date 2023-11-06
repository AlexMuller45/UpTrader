from django.db import models


class Menu(models.Model):
    """
    Модель меню, содержит название меню
    """

    title = models.CharField(max_length=50, unique=True, verbose_name="Menu title")
    url = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Название меню"
        verbose_name_plural = "Названия меню"


class MenuItem(models.Model):
    """
    Модель пунктов меню, содержит имя, адрес, ссылку на вышестоящий пункт меню
    """

    name = models.CharField(max_length=100, unique=True, null=False, blank=False)
    url = models.CharField(max_length=255)
    menu = models.ForeignKey(
        Menu,
        blank=True,
        on_delete=models.CASCADE,
        related_name="items",
    )
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="children",
    )

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Пункт меню"
        verbose_name_plural = "Пункты меню"
