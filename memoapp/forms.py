
from django import forms
from django.utils import timezone
from django.core.exceptions import ValidationError
from .models import Memos,Tags
import datetime


class MemoAddForm(forms.ModelForm):
    class Meta:
        model = Memos
        fields = ('title', 'body', 'tags')  # ← updateDate を外す

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].widget.attrs = {
            'placeholder': 'タスク名',
            'class': 'w-full p-2 border border-gray-300 rounded-md'
        }
        self.fields["tags"].widget_attrs={
            'class': 'w-full p-2 border border-gray-300 rounded-md'
        }
        self.fields["body"].widget.attrs = {
            'placeholder': '詳細',
            'class': 'w-full p-2 border border-gray-300 rounded-md'
        }


    def clean_updateDate(self):
        # フォームの入力に関係なく、現在時刻を返す
        return datetime.datetime.now()
    
class TagsAddForm(forms.ModelForm):
    class Meta:
        model = Tags
        fields = ["tagName"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["tagName"].widget.attrs = {
            "placeholder": "タグ名",
            "class": "w-full p-2 border border-gray-300 rounded-md"
        }
