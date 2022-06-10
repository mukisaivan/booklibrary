from django.shortcuts import render
from django.http import HttpResponse

bookshelfs = [
    {'id': 1, 'name': 'lets learn python'},
    {'id': 2, 'name': 'design with me'},
    {'id': 3, 'name': 'front end developer'},
]


def home(request):
    context = {'bookshelfs': bookshelfs}
    return render(request, 'base/home.html', context)

def bookshelf(request,pk):
    bookshelf = None
    for i in bookshelfs:
        if i['id'] == int(pk):
            bookshelf = i
    context = {'bookshelf': bookshelf}
    return render(request, 'base/bookshelf.html', context)
# Create your views here.
