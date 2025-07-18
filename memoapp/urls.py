from django.urls import path
from memoapp import views as mm

urlpatterns = [
    path("", mm.memoindex, name="index"),
    # path("add/", v.add, name="add"),
    # path('<int:pk>/edit/',v.edit, name="edit"),
    # path("<int:pk>/delete",v.Delete,name="delete"),
    # path("update_task_complete/", v.update_task_complete, name="update_task_complete"),
]