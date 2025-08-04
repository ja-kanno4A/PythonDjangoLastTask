
from django import forms
from django.utils import timezone
from django.core.exceptions import ValidationError
from .models import Memos,Tags
import datetime


class MemoAddForm(forms.ModelForm):
    class Meta:
        model = Memos
        fields = ('title', 'body', 'tags', 'updateDate')
        widgets = {
            'updatetime': forms.DateTimeInput(attrs={"type":"datetime-local"})
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].widget.attrs = {'placeholder': 'タスク名'}
        self.fields["body"].widget.attrs = {'placeholder': '詳細'}
        
    def clean_updateDate(self):
        updateDate = self.cleaned_data.get('updateDate')
        updateDate = datetime.datetime.now()
        return updateDate
    
class TagsAddForm(forms.ModelForm):
    class Meta:
        model = Tags
        fields = {"tagName"}
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["TagName"].widget.attrs = {"placeholder" : "タグ名(カンマ(,)は使用しないでください))"}