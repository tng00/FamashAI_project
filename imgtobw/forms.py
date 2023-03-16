from django import forms
from .models import UserImage


class ImageForm(forms.ModelForm):
    """Form for the image model"""

    class Meta:
        model = UserImage
        fields = ('image',)
