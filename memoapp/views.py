from django.shortcuts import render,redirect
from django.views import View # クラスベースビューを継承するのに必要
from django.urls import reverse_lazy 
class IndexView(View):
    def get(self,req):
        return render(req,"memoApp/index.html")
    
memoindex = IndexView.as_view()