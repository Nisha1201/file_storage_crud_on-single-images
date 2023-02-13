# image_app/forms.py
from django import forms
from .models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['id', 'title', 'image']