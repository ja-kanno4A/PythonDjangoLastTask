
from django import forms
from django.utils import timezone
from django.core.exceptions import ValidationError
from .models import Memos
import datetime


# Memosモデル用の入力フォーム
class MemosForm(forms.ModelForm):
    class Meta: # 構成・設定を指定できる（どのモデルと連携する、どのフィールドを使う、フォームの構成設定など）
        model = Memos
        fields = ('title', 'body', 'tags', 'updateDate') # フォームに表示するフィールドを指定
        widgets = { # 特定のフィールドの見た目を指定 datetime-localによりHTMLにて日付＋時刻入力フィールドになる
            'tags': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'updateDate': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
        #print(f"models:{model}\n-----------\nfields:{fields}\n----------\nwidgets{widgets}\n------------")

    def __init__(self, *args, **kwargs): # フォームが生成されるときの初期化処理
        super().__init__(*args, **kwargs)

        self.fields["title"].widget.attrs = {'placeholder': 'タスク名'} # プレースホルダー（薄い説明文）を設定する
        self.fields["body"].widget.attrs = {'placeholder': '詳細'}
        #print(f"self:{self}\n----------------\n*args:{args}\n-------------\nkwargs:{kwargs}")

    # 項目別にバリデーションを追加する場合はclean_<項目名>とする
    def clean_tags(self):
        tags = self.cleaned_data.get('tags') # フォームの入力値を安全に取得（バリデーション済みの値（形式ミス、日付の不正などがない））
        # if tags and tags < timezone.now(): # tagsが存在し、今の時間未満だった場合
        #     raise ValidationError("開始日を過去に設定することはできません。") # バリデーションエラー

        return tags

    def clean_updateDate(self):
        updateDate = self.cleaned_data.get('updateDate')
        updateDate = datetime.datetime.now()
        return updateDate


class Editors(forms.ModelForm):
    class Meta: # 構成・設定を指定できる（どのモデルと連携する、どのフィールドを使う、フォームの構成設定など）
        model = Memos
        fields = ('title', 'body', 'tags', 'updateDate') # フォームに表示するフィールドを指定
        widgets = { # 特定のフィールドの見た目を指定 datetime-localによりHTMLにて日付＋時刻入力フィールドになる
            'tags': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'updateDate': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
        
    def __init__(self, *args, **kwargs): # フォームが生成されるときの初期化処理
        super().__init__(*args, **kwargs)

        self.fields["title"].widget.attrs = {'placeholder': 'title'} # プレースホルダー（薄い説明文）を設定する
        self.fields["body"].widget.attrs = {'placeholder': '詳細'}