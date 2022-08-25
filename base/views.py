from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Book, Bookshelf, Borrow

from django.contrib.auth.models import User

from .forms import Bookshelfform
from django.db.models import Q
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from . import models


# bookshelfs = [
#     {'id': 1, 'name': 'lets learn python'},
#     {'id': 2, 'name': 'design with me'},
#     {'id': 3, 'name': 'front end developer'},
# ]


def picture(request):
    return render(request, 'base/pic.html')


def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User Does not Exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            messages.error(request, 'Username OR Password does not Exist')

    context = {'page': page}
    return render(request, 'base/login_register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')


def registerPage(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(
                commit=False)  # this freezes the form in time to ensure that if the user is valid the form is gona be crated right away
            # therefore, we commit it to false so that we can get the user object

            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')

        else:
            messages.error(request, 'An error occurred during registration')

    return render(request, 'base/login_register.html', {'form': form})


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    books = Book.objects.all()

    bookshelfs = Bookshelf.objects.filter(
        Q(bookCategory__name__icontains=q) |
        Q(name__icontains=q) |
        Q(borrowed__icontains=q)
    )

    bookshelf_count = bookshelfs.count()

    context = {'bookshelfs': bookshelfs, 'books': books, 'bookshelf_count': bookshelf_count}
    return render(request, 'base/home.html', context)


def bookshelf(request, pk):
    bookshelf = Bookshelf.objects.get(id=pk)
    bookshelf_borrows = bookshelf.borrow_set.all().order_by('-borrow_time')


    if request.method == 'POST':
        borrow = Borrow.objects.create(
            user=request.user,
            bookshelf=bookshelf,
        )
        return redirect('bookshelf', pk=bookshelf.id)

    context = {'bookshelf': bookshelf, 'bookshelf_borrows': bookshelf_borrows}
    return render(request, 'base/bookshelf.html', context)


@login_required(login_url='login')
def addbookshelf(request):
    form = Bookshelfform()
    if request.method == 'POST':
        form = Bookshelfform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/bookshelf_form.html', context)


@login_required(login_url='login')
def editbookshelf(request, pk):
    bookshelf = Bookshelf.objects.get(id=pk)

    form = Bookshelfform(instance=bookshelf)

    if request.user != bookshelf.librarian:
        return HttpResponse('This book was not uploaded by you')

    if request.method == 'POST':
        form = Bookshelfform(request.POST, instance=bookshelf)

        if form.is_valid():
            form.save()
        return redirect('home')

    context = {'form': form}
    return render(request, 'base/bookshelf_form.html', context)


@login_required(login_url='login')
def deletebookshelf(request, pk):  # pk makes sure that you are dealing with certain items
    bookshelf = Bookshelf.objects.get(id=pk)

    if request.user != bookshelf.librarian:
        return HttpResponse('This bookshelf is not yours')

    if request.method == 'POST':
        bookshelf.delete()
        redirect('home')
    return render(request, 'base/delete.html', {'obj': bookshelf})


def dashboard(request):
    return render(request, 'base/dashboard.html')
