from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone  # Импортируем модуль для работы с временем
from django.core.exceptions import ValidationError

# Модель для загруженных файлов
def validate_pdf_file(value):
    
    #Валидатор для проверки, что файл имеет формат PDF.

    if not value.name.endswith('.pdf'):
        raise ValidationError('Only PDF files are allowed.')

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/', validators=[validate_pdf_file])  # Добавляем валидатор
    title = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title
    
    
# Модель для избранных файлов
class FavoriteFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Связь с пользователем
    file = models.ForeignKey(UploadedFile, on_delete=models.CASCADE)  # Связь с файлом
    added_at = models.DateTimeField(auto_now_add=True)  # Дата и время добавления в избранное

    def str(self):
        return f"{self.user.username} - {self.file.title}"  # Строковое представление объекта