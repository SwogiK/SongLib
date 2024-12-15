from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import UploadedFile, FavoriteFile
from .forms import UploadFileForm

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

# Главная страница
def home(request):
    files = UploadedFile.objects.all()  # Получаем все загруженные файлы
    paginator = Paginator(files, 10)  # Показываем 10 файлов на странице
    page_number = request.GET.get('page')  # Получаем номер текущей страницы
    page_obj = paginator.get_page(page_number)  # Получаем объект страницы
    return render(request, 'home.html', {'page_obj': page_obj})  # Рендерим шаблон с данными

# Страница загрузки файлов
def load_song(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)  # Создаем форму с данными из запроса
        if form.is_valid():
            uploaded_file = form.save(commit=False)  # Сохраняем форму, но не записываем в базу данных
            uploaded_file.user = request.user  # Устанавливаем текущего пользователя
            uploaded_file.save()  # Сохраняем файл в базу данных
            return redirect('home')  # Перенаправляем на главную страницу
    else:
        form = UploadFileForm()  # Создаем пустую форму
    return render(request, 'load_song.html', {'form': form})  # Рендерим шаблон с формой

# Страница поиска
def search(request):
    query = request.GET.get('q')  # Получаем запрос из GET-параметра
    if query:
        files = UploadedFile.objects.filter(title__icontains=query)  # Фильтруем файлы по заголовку
    else:
        files = UploadedFile.objects.all()  # Получаем все файлы
    paginator = Paginator(files, 10)  # Показываем 10 файлов на странице
    page_number = request.GET.get('page')  # Получаем номер текущей страницы
    page_obj = paginator.get_page(page_number)  # Получаем объект страницы
    return render(request, 'search.html', {'page_obj': page_obj, 'query': query})  # Рендерим шаблон с данными

# Страница деталей файла
def file_detail(request, file_id):
    file = get_object_or_404(UploadedFile, id=file_id)  # Получаем файл по ID или возвращаем 404
    return render(request, 'file_detail.html', {'file': file})  # Рендерим шаблон с данными

# Страница регистрации
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)  # Создаем форму с данными из запроса
        if form.is_valid():
            form.save()  # Сохраняем пользователя в базу данных
            username = form.cleaned_data.get('username')  # Получаем имя пользователя
            raw_password = form.cleaned_data.get('password1')  # Получаем пароль
            user = authenticate(username=username, password=raw_password)  # Аутентифицируем пользователя
            login(request, user)  # Входим в систему
            return redirect('home')  # Перенаправляем на главную страницу
    else:
        form = UserCreationForm()  # Создаем пустую форму
    return render(request, 'register.html', {'form': form})  # Рендерим шаблон с формой

# Страница входа
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)  # Создаем форму с данными из запроса
        if form.is_valid():
            username = form.cleaned_data.get('username')  # Получаем имя пользователя
            password = form.cleaned_data.get('password')  # Получаем пароль
            user = authenticate(username=username, password=password)  # Аутентифицируем пользователя
            if user is not None:
                login(request, user)  # Входим в систему
                return redirect('home')  # Перенаправляем на главную страницу
    else:
        form = AuthenticationForm()  # Создаем пустую форму
    return render(request, 'login.html', {'form': form})  # Рендерим шаблон с формой

# Страница выхода
def logout_view(request):
    logout(request)  # Выходим из системы
    return redirect('home')  # Перенаправляем на главную страницу

# Страница профиля
def profile(request):
    return render(request, 'profile.html')  # Рендерим шаблон профиля

# Добавление файла в избранное
@login_required
def add_to_favorites(request, file_id):
    file = get_object_or_404(UploadedFile, id=file_id)  # Получаем файл по ID или возвращаем 404
    FavoriteFile.objects.get_or_create(user=request.user, file=file)  # Добавляем файл в избранное
    return redirect('file_detail', file_id=file_id)  # Перенаправляем на страницу деталей файла

# Удаление файла из избранного
@login_required
def remove_from_favorites(request, file_id):
    file = get_object_or_404(UploadedFile, id=file_id)  # Получаем файл по ID или возвращаем 404
    FavoriteFile.objects.filter(user=request.user, file=file).delete()  # Удаляем файл из избранного
    return redirect('file_detail', file_id=file_id)  # Перенаправляем на страницу деталей файла

# Страница избранных файлов
@login_required
def favorites(request):
    favorites = FavoriteFile.objects.filter(user=request.user)  # Получаем избранные файлы пользователя
    paginator = Paginator(favorites, 10)  # Показываем 10 файлов на странице
    page_number = request.GET.get('page')  # Получаем номер текущей страницы
    page_obj = paginator.get_page(page_number)  # Получаем объект страницы
    return render(request, 'favorites.html', {'page_obj': page_obj})  # Рендерим шаблон с данными

# Страница моих файлов
@login_required
def my_files(request):
    files = UploadedFile.objects.filter(user=request.user)  # Получаем файлы пользователя
    paginator = Paginator(files, 10)  # Показываем 10 файлов на странице
    page_number = request.GET.get('page')  # Получаем номер текущей страницы
    page_obj = paginator.get_page(page_number)  # Получаем объект страницы
    return render(request, 'my_files.html', {'page_obj': page_obj})  # Рендерим шаблон с данными

# Удаление файла
@login_required
def delete_file(request, file_id):
    file = get_object_or_404(UploadedFile, id=file_id)  # Получаем файл по ID или возвращаем 404
    if file.user == request.user:
        file.delete()  # Удаляем файл
    return redirect('home')  # Перенаправляем на главную страницу