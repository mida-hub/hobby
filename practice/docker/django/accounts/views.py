import logging

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

logger = logging.getLogger(__name__)


class HomeView(View):
    def get(self, request, *args, **kwargs):
        # コールバックで入ってきた時に自分以外はログアウトさせる
        if request.user.is_authenticated and request.user.email != 'rusuden0106@gmail.com':
            auth_logout(request)
        return render(request, 'accounts/home.html')
home = HomeView.as_view()


class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'accounts/login.html')
login = LoginView.as_view()


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return render(request, 'accounts/logout.html')
logout = LogoutView.as_view()
