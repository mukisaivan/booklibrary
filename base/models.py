from django.db import models
from django.contrib.auth.models import User


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


    class Meta:
        ordering = ['-borrow_time', '-return_time']

    def __str__(self):
        return self.name


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

