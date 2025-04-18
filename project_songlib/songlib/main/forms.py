from django import forms
from .models import UploadedFile

# Форма для загрузки файлов
class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['file', 'title']

    def clean_file(self):
        
        # Валидация файла на стороне формы.
        
        file = self.cleaned_data.get('file')
        if not file.name.endswith('.pdf'):
            raise forms.ValidationError('Only PDF files are allowed.')
        return file
    
