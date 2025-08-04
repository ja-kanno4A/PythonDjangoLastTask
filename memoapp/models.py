from django.db import models

class Memos(models.Model):
    class Meta:
        db_table = 'memos'
    
    title = models.CharField(verbose_name="タイトル", max_length=100)
    body= models.CharField(verbose_name="本文", max_length=255)
    tags = models.CharField(verbose_name="タグ", max_length=255)
    updateDate = models.DateTimeField(verbose_name="更新日", null=True, blank=True)
    
    def __str__(self): # 管理画面でレコード毎に表示する文字列を指定
        return self.title
    
class Tags(models.Model):
    class Meta:
        db_table = "tags"
    
    tagName = models.CharField(verbose_name="タグ名", max_length=255,unique=True)
    
    def __str__(self): # 管理画面でレコード毎に表示する文字列を指定
        return self.tagName
    