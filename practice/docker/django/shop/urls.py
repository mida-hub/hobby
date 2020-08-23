from django.urls import path
from django.views.generic import RedirectView

from . import views

app_name = 'shop'
urlpatterns = [
    path('list/', views.list, name='list'),
    path('register/', views.register, name='register'),
]
