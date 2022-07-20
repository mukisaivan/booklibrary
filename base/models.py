from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# class User(AbstractUser):
#
#     is_admin = models.BooleanField(default=False)
#     is_librarian = models.BooleanField(default=True)
#     is_student = models.BooleanField(default=False)
#
#     class Meta:
#         swappable = 'AUTH_USER_MODEL'


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
    book_image_url = models.ImageField(max_length=2083, null=True, blank=True)
    borrowed = models.DateTimeField(auto_now=True)
    description = models.TextField(max_length=200, null=True, blank=True)


    class Meta:
        ordering = ['-borrowed']

    def __str__(self):
        return self.name


class Borrowstatus(models.Model):
    updated = models.DateTimeField(auto_now=True)  # this is used to take stamps each time a student saves a book
    borrowdate = models.CharField(max_length=100)

    # (auto_now_add=True)  # this takes time stamp only when the user save the first time

    def __str__(self):
        return self.borrowdate


class Borrower(models.Model):
    student = ()
    book = ()
    date_borrowed = ()
    expected_date_of_return = ()
    return_date = ()


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

