from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('bookshelf/<str:pk>/', views.bookshelf, name='bookshelf'),
]

