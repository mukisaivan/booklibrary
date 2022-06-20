from django.contrib import admin
from .models import Bookshelf, Book, Borrowstatus


admin.site.register(Bookshelf)
admin.site.register(Book)
admin.site.register(Borrowstatus)