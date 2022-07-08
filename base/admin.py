from django.contrib import admin
from .models import Book, Borrowstatus, Bookshelf
from .models import User

admin.site.register(Bookshelf)
admin.site.register(Book)
admin.site.register(Borrowstatus)
