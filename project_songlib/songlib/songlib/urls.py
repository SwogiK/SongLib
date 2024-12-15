from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Основные URL-шаблоны
urlpatterns = [
    path('admin/', admin.site.urls),  # Административная панель Django
    path('', include('main.urls')),  # Подключение URL-адресов из приложения main
]

# Добавляем маршруты для медиафайлов только в режиме отладки
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)