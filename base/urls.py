from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),
    path('', views.home, name='home'),
    path('bookshelf/<str:pk>/', views.bookshelf, name='bookshelf'),
    path('add-bookshelf/', views.addbookshelf, name='add-bookshelf'),
    path('editbookshelf/<str:pk>/', views.editbookshelf, name='editbookshelf'),
    path('deletebookshelf/<str:pk>/', views.deletebookshelf, name='deletebookshelf'),
    path('picture/', views.picture, name='picture'),
    path('dashboard/', views.dashboard, name='dashboard')

]

