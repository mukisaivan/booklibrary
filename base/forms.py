from django.forms import ModelForm
from .models import Bookshelf
# from django import forms


class Bookshelfform(ModelForm):
    class Meta:
        model = Bookshelf
        fields = '__all__'


