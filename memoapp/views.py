from django.shortcuts import render,redirect
from .forms import MemoAddForm,TagsAddForm
from django.urls import reverse_lazy 
from .models import Memos,Tags
from django.views import View

class IndexView(View):
    def get(self,req):
        return render(req,"memoApp/index.html")
    
class AddPageView(View):
    def get(self,req):
        form = MemoAddForm()
        return render(req,"memoApp/addpage.html",{"form":form})

class TagAddView(View):
    def get(self,req):
        return render(req,"")
    
memoindex = IndexView.as_view()
add = AddPageView.as_view()