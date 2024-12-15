from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Главная страница
    path('load-song/', views.load_song, name='load_song'),  # Страница загрузки файлов
    path('search/', views.search, name='search'),  # Страница поиска
    path('file/<int:file_id>/', views.file_detail, name='file_detail'),  # Страница деталей файла
    path('register/', views.register, name='register'),  # Страница регистрации
    path('login/', views.login_view, name='login'),  # Страница входа
    path('logout/', views.logout_view, name='logout'),  # Страница выхода
    path('profile/', views.profile, name='profile'),  # Страница профиля
    path('favorites/', views.favorites, name='favorites'),  # Страница избранных файлов
    path('add_to_favorites/<int:file_id>/', views.add_to_favorites, name='add_to_favorites'),  # Добавление в избранное
    path('remove_from_favorites/<int:file_id>/', views.remove_from_favorites, name='remove_from_favorites'),  # Удаление из избранного
    path('my_files/', views.my_files, name='my_files'),  # Страница моих файлов
    path('delete_file/<int:file_id>/', views.delete_file, name='delete_file'),  # Удаление файла
]