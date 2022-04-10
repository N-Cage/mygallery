from django import forms

from .models import ImageCard



class CreateImageCardForm(forms.ModelForm):

    class Meta:
        model = ImageCard
        fields = ['title', 'image', 'discription']