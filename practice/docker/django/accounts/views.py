# from django.contrib.auth import login as auth_login
from django.shortcuts import render
# from django.urls import reverse
from django.views import View
#
# from .forms import LoginForm
#

from django.http import HttpResponse

class HelloView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'message': "Hello World!",
        }
        return render(request, 'accounts/index.html', context)

# path('', views.index, name='index')
# name と 変数名が一致している必要があるらしい
index = HelloView.as_view()
