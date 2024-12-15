from django.apps import AppConfig

# Конфигурация приложения "main"
class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # Указывает, что по умолчанию используется BigAutoField для первичных ключей
    name = 'main'  # Имя приложения, которое будет использоваться в проекте