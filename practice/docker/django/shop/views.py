import logging

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .models import Book
from .forms import RegisterForm

logger = logging.getLogger(__name__)


class RegisterView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        context = {
            'form': RegisterForm(),
        }
        return render(request, 'shop/register.html', context)

    def post(self, request, *args, **kwargs):
        logger.info("You're in post!!!")
        # リクエストからフォームを作成
        form = RegisterForm(request.POST)

        # バリデーション
        if not form.is_valid():
            # バリデーションNGの場合はアカウント登録画面のテンプレートを再表示
            return render(request, 'shop/register.html', {'form': form})

        form.save()

        # フラッシュメッセージを画面に表示
        messages.info(request, "登録しました。")

        # list画面にリダイレクト
        return redirect(reverse('shop:list'))


register = RegisterView.as_view()


class ListView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        queryset = Book.objects.all()
        context = {
            'book_list': queryset,
        }
        print(queryset)
        return render(request, 'shop/list.html', context)

    def post(self, request, *args, **kwargs):
        logger.info("You're in post!!!")

        if 'delete' in request.POST:
            book_id = request.POST['delete']
            book_item = Book.objects.get(id=book_id)
            book_item.delete()

            # フラッシュメッセージを画面に表示
            messages.info(request, "削除しました。")

        elif 'update' in request.POST:
            book_id = request.POST['update']
            book_title = request.POST[f'title_{book_id}']
            book_price = request.POST[f'price_{book_id}']

            book_item = Book.objects.get(id=book_id)
            book_item.title = book_title
            book_item.price = book_price
            book_item.save()

            # フラッシュメッセージを画面に表示
            messages.info(request, "更新しました。")

        # list画面にリダイレクト
        return redirect(reverse('shop:list'))


list = ListView.as_view()

