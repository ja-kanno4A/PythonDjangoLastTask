import datetime
from django.shortcuts import render, redirect
from .forms import MemoAddForm, TagsAddForm
from django.urls import reverse_lazy 
from .models import Memos, Tags
from django.views import View
from django.views.decorators.http import require_POST
from django.utils.decorators import method_decorator


class IndexView(View):
    def get(self, req):
        tag_id = req.GET.get('tag')  # ?tag=1 のようにGETから取得
        tags = Tags.objects.all()

        if tag_id:
            memos = Memos.objects.filter(tags__id=tag_id).order_by('-updateDate')
        else:
            memos = Memos.objects.all().order_by('-updateDate')
        
        return render(req, "memoApp/index.html", {
            "memos": memos,
            "tags": tags,
            "selected_tag": int(tag_id) if tag_id else None,
        })



class AddPageView(View):
    def get(self, req):
        form = MemoAddForm()
        return render(req, "memoApp/addpage.html", {"form": form})

    def post(self, req):
        form = MemoAddForm(req.POST)
        if form.is_valid():
            memo = form.save(commit=False)
            memo.updateDate = datetime.datetime.now()  # ← ここで強制的に上書き
            memo.save()
            form.save_m2m()
            return redirect('index')
        return render(req, "memoApp/addpage.html", {"form": form})
    
class MemoEditView(View):
    def get(self, request, pk):
        memo = Memos.objects.get(pk=pk)
        form = MemoAddForm(instance=memo)
        return render(request, "memoApp/addpage.html", {
            "form": form,
            "is_edit": True,
            "form_action": reverse_lazy("edit_memo", kwargs={"pk": pk})
        })

    def post(self, request, pk):
        memo = Memos.objects.get(pk=pk)
        form = MemoAddForm(request.POST, instance=memo)
        if form.is_valid():
            memo = form.save(commit=False)
            memo.save()
            form.save_m2m()
            return redirect("index")
        return render(request, "memoApp/addpage.html", {
            "form": form,
            "is_edit": True,
            "form_action": reverse_lazy("edit_memo", kwargs={"pk": pk})
        })



class TagAddView(View):
    def get(self, request):
        form = TagsAddForm()
        return render(request, "memoApp/tag_add.html", {"form": form})

    def post(self, request):
        form = TagsAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # 保存後にトップページに戻すなど
        return render(request, "memoApp/tag_add.html", {"form": form})
    
    
@method_decorator(require_POST, name='dispatch')
class MemoDeleteView(View):
    def post(self, request, pk):
        memo = Memos.objects.get(pk=pk)
        memo.delete()
        return redirect("index")





# 関数っぽく使いたいときは下のように設定
memoindex = IndexView.as_view()
add = AddPageView.as_view()
delete_memo = MemoDeleteView.as_view()
edit_memo = MemoEditView.as_view()
