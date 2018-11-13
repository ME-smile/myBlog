from django.db import models
from blogs.models import Blog
from users.models import User

# Create your models here.
# 用户收藏
# 
class UserOperation(models.Model):
    user=models.ForeignKey(User,on_delete=models.DO_NOTHING,verbose_name='用户')

    class Meta:
        abstract=True

class UserFavor(UserOperation):
    blog=models.ForeignKey(Blog,on_delete=models.DO_NOTHING,verbose_name='博客')
    favor_nums=models.IntegerField(verbose_name='收藏量')
    favor_created_time=models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table='用户收藏'

###用户消息
class UserMessage(UserOperation):
    message_content=models.CharField(max_length=500,verbose_name='消息内容')
    message_send_time=models.DateTimeField(auto_now_add=True,verbose_name='发送时间')
    message_nums=models.IntegerField(verbose_name='消息量')
    has_read=models.BooleanField(default=False,verbose_name='是否已读')

    class Meta:
        db_table='用户消息'

###用户评论
class UserComment(UserOperation):
    comments_content=models.CharField(max_length=200,verbose_name='用户评论')
    comment_nums=models.IntegerField(verbose_name='评论量')
    comment_time=models.DateTimeField(auto_now_add=True,verbose_name='评论时间')

    class Meta:
        db_table='用户评论'

###用户访问
class UserVisit(UserOperation):
    click_nums=models.IntegerField(verbose_name='阅读')