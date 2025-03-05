from django.urls import path
from . import views

urlpatterns = [
    path('index.html', views.index),
    path('resume.html', views.resume),
    # path('portfolio.html', views.portfolio),
    path('contact.html', views.contact)
]