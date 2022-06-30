from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),
    path('librarian/', views.librarian, name='librarian'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('student/', views.student, name='student'),
    path('', views.home, name='home'),
    path('bookshelf/<str:pk>/', views.bookshelf, name='bookshelf'),
    path('create-bookshelf/', views.createbookshelf, name='create-bookshelf'),
    path('updatebookshelf/<str:pk>/', views.updatebookshelf, name='updatebookshelf'),
    path('deletebookshelf/<str:pk>/', views.deletebookshelf, name='deletebookshelf'),

]

