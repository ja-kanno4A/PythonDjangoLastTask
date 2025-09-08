from django.db import models
import datetime

class Tags(models.Model):
    class Meta:
        db_table = "tags"
    
    tagName = models.CharField(verbose_name="タグ名", max_length=255, unique=True)

    def __str__(self):
        return self.tagName


class Memos(models.Model):
    class Meta:
        db_table = 'memos'
    
    title = models.CharField(verbose_name="タイトル", max_length=100 ,default="タイトルなし")
    body = models.TextField(verbose_name="本文", max_length=255, default="なし")
    tags = models.ManyToManyField(Tags, verbose_name="タグ")  # ✅ ここをManyToManyに変更
    updateDate = models.DateTimeField(verbose_name="更新日", null=True, default=datetime.datetime.now)

    def __str__(self):
        return self.title
