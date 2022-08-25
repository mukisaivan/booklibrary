from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone
from django.contrib.auth.models import User
from uuid import uuid4


class Book(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Bookshelf(models.Model):
    librarian = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    user_id = models.CharField(max_length=200, null=True, blank=True)
    bookCategory = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)  # changed from book to bookCategory
    name = models.CharField(max_length=255, null=True, blank=True)
    author = models.CharField(max_length=200, null=True, blank=True)
    book_image_url = models.CharField(max_length=2083, null=True, blank=True)
    borrowed = models.DateTimeField(auto_now=True)
    description = models.TextField(max_length=200, null=True, blank=True)
    borrow_time = models.DateTimeField(auto_now_add=True)
    return_time = models.DateTimeField(auto_now=True)

    # date_created = models.DateTimeField(blank=True, null=True)
    # last_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['-borrow_time', '-return_time']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.user_id = str(uuid4()).split('-')[4]




    # def save(self, *args, **kwargs):
    #     if self.date_created is None:
    #         self.date_created = timezone.localtime(timezone.now())
    #     if self.last_updated is None:
    #         self.last_updated = timezone.localtime(timezone.now())


class Borrowstatus(models.Model):
    updated = models.DateTimeField(auto_now=True)
    borrowdate = models.CharField(max_length=100)

    def __str__(self):
        return self.borrowdate


class Borrow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bookshelf = models.ForeignKey(Bookshelf, on_delete=models.CASCADE)
    borrow_time = models.DateTimeField(auto_now_add=True)
    return_time = models.DateTimeField(auto_now=True)


class Fine(models.Model):
    student = ()
    book = ()
    days = ()


class Payments(models.Model):
    fine = ()
    payment = ()
    date = ()
    book = ()
    student = ()

