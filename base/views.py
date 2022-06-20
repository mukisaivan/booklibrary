from django.shortcuts import render, redirect
from .models import Bookshelf, Book
from .forms import Bookshelfform
from django.db.models import Q
from django.http import HttpResponse

# bookshelfs = [
#     {'id': 1, 'name': 'lets learn python'},
#     {'id': 2, 'name': 'design with me'},
#     {'id': 3, 'name': 'front end developer'},
# ]


def home(request):
    books = Book.objects.all()
    q = request.GET.get('q') if request.GET.get('q') != None else ''


    bookshelfs = Bookshelf.objects.filter(
        Q(book__name__icontains=q) |
        Q(name__icontains=q) |
        Q(borrowed__icontains=q)
    )

    bookshelf_count = bookshelfs.count()

    context = {'bookshelfs': bookshelfs, 'books': books, 'bookshelf_count': bookshelf_count}
    return render(request, 'base/home.html', context)


def bookshelf(request, pk):
    bookshelf = Bookshelf.objects.get(id=pk)
    context = {'bookshelf': bookshelf}
    return render(request, 'base/bookshelf.html', context)


def createbookshelf(request):
    form = Bookshelfform()
    if request.method == 'POST':
        form = Bookshelfform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/bookshelf_form.html', context)


def updatebookshelf(request, pk):
    bookshelf = Bookshelf.objects.get(id=pk)
    form = Bookshelfform(instance=bookshelf)
    if request.method == 'POST':
        form = Bookshelfform(request.POST, instance=bookshelf)
        if form.is_valid():
            form.save()
        return redirect('home')

    context = {'form': form}
    return render(request, 'base/bookshelf_form.html', context)


def deletebookshelf(request, pk):  # pk makes sure that you are dealing with certain items
    bookshelf = Bookshelf.objects.get(id=pk)
    if request.method == 'POST':
        bookshelf.delete()
        redirect('home')
    return render(request, 'base/delete.html', {'obj': bookshelf})