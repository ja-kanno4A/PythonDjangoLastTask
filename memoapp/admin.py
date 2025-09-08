from django.contrib import admin
from .models import Memos
from .models import Tags

admin.site.register(Memos)
admin.site.register(Tags)
# Register your models here.
