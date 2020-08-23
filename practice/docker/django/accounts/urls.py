from django.urls import path
from django.views.generic import RedirectView

from . import views

app_name = 'accounts'
urlpatterns = [
    path('home/', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('', RedirectView.as_view(url='/accounts/home/')),
    path('register/', views.register, name='register'),
]
