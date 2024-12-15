from django import forms
from .models import UploadedFile

# Форма для загрузки файлов
class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadedFile  # Используем модель UploadedFile
        fields = ['file', 'title']  # Поля, которые будут отображаться в форме