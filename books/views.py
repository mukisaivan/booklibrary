
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('LETS DO THIS')


def next_page(request)
    return HttpResponse('NEW BOOKS')