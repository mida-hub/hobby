from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.core.exceptions import ObjectDoesNotExist

from .models import Book


class RegisterForm(forms.ModelForm):
    """ユーザー登録画面用のフォーム"""

    class Meta:
        # 利用するモデルクラスを指定
        model = Book
        # 利用するモデルのフィールドを指定
        fields = ('title', 'price',)
        # ウィジェットを上書き
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'タイトル'}),
            'price': forms.TextInput(attrs={'placeholder': '価格'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # フィールドの属性を書き換え
        self.fields['title'].required = True
        self.fields['price'].required = True

    def clean_title(self):
        value = self.cleaned_data['title']
        """
            バリデーション
        """
        return value

    def clean_price(self):
        value = self.cleaned_data['price']
        """
            バリデーション
        """
        return value

    def clean(self):
        """
            バリデーション
        """
        super().clean()
