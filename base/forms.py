from django.forms import ModelForm
from .models import Bookshelf


class Bookshelfform(ModelForm):
    class Meta:
        model = Bookshelf
        fields = '__all__'
