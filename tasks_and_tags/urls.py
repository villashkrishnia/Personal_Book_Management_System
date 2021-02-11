from django.urls import path
from . import views

urlpatterns = [
    path('add_task', views.add_task, name='add_task'),
    path('add_tag', views.add_tag, name='add_tag'),
    path('delete_task/<str:pk>/', views.delete_task, name='delete_task'),
    path('delete_tag/<str:pk>/', views.delete_tag, name='delete_tag'),
    path('edit_task/<str:pk>/', views.edit_task, name='edit_task'),
    path('mark_complete/<str:pk>/', views.mark_complete, name='mark_complete'),
    path('mark_pending/<str:pk>/', views.mark_pending, name='mark_pending'),

]