from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone  # Импортируем модуль для работы с временем

# Модель для загруженных файлов
class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')  # Поле для загрузки файла
    title = models.CharField(max_length=255)  # Заголовок файла
    uploaded_at = models.DateTimeField(default=timezone.now)  # Дата и время загрузки
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # Связь с пользователем

    def str(self):
        return self.title  # Строковое представление объекта

# Модель для избранных файлов
class FavoriteFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Связь с пользователем
    file = models.ForeignKey(UploadedFile, on_delete=models.CASCADE)  # Связь с файлом
    added_at = models.DateTimeField(auto_now_add=True)  # Дата и время добавления в избранное

    def str(self):
        return f"{self.user.username} - {self.file.title}"  # Строковое представление объекта