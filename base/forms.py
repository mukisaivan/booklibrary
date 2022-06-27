from django.forms import ModelForm
from .models import Bookshelf, Book, User
from django import forms


class Bookshelfform(forms.ModelForm):
    class Meta:
        model = Bookshelf
        fields = '__all__'


class Bookform(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'