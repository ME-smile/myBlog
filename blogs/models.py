from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    blog_title=models.CharField(max_length=50,verbose_name='标题')
    blog_content=models.TextField('内容')
    author=models.ForeignKey(User,on_delete=models.DO_NOTHING,verbose_name='作者')
    category=models.ForeignKey('Category',on_delete=models.DO_NOTHING,verbose_name='分类')
    posted_time=models.DateTimeField(auto_now_add=True,verbose_name='发布时间')
    last_modified_time=models.DateTimeField(auto_now=True,verbose_name='最近修改时间')

    def __str__(self):
        return self.blog_title

    class Meta:
        ordering=['-posted_time']
        db_table='博客'

class Category(models.Model):
    category_name=models.CharField(max_length=15,verbose_name='分类')
    
    def __str__(self):
        return self.category_name

