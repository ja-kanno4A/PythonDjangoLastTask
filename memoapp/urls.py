from django.urls import path
from memoapp import views as mm

urlpatterns = [
    path("", mm.memoindex, name="index"),
    path("add/", mm.add, name="addpage"),
    path("tags/add/", mm.TagAddView.as_view(), name="tag_add"),
    path("edit/<int:pk>/", mm.edit_memo, name="edit_memo"),      # 編集ページ
    path("delete/<int:pk>/", mm.delete_memo, name="delete_memo"),  # 削除処理
]