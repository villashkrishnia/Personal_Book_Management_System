from django.urls import path
from . import views

urlpatterns = [
    path('', views.dash, name='dash'),
    path('add_book', views.add_book, name='add_book'),
    path('delete_book/<str:pk>/', views.delete_book, name='delete_book'),
    path('edit_book/<str:pk>/', views.edit_book, name='edit_book'),
]