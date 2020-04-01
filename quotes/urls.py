from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.quotes_page),
    path('quotes_filter', views.quotes_filter),
]
