from django.apps import AppConfig


class WomenConfig(AppConfig):  # класс для отображения приложения в проекте
    name = 'women'
    verbose_name = 'Женщины мира'  # в заголовке в админке и в любых частях, где будет отображаться название

