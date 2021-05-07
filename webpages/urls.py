from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='webpages/home.html'), name='home'),
    path('about', TemplateView.as_view(template_name='webpages/about.html'), name='about'),
    path('contact', views.contact, name='contact'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('side_navbar', views.side_navbar, name='side_navbar'),
]