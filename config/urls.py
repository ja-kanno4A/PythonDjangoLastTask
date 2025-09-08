from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("memoapp.urls")),
    path('accounts/', include('django.contrib.auth.urls')),     # ユーザー認証用のビューを呼び出す
    
]
