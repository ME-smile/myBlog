from django.db import models

# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=20,verbose_name='用户名')
    nick_name=models.CharField(max_length=50,verbose_name='昵称',default='')
    birthday=models.DateField(verbose_name='生日',null=True,blank=True)
    gender=models.CharField(choices=(('female','男'),('male','女')),max_length=1,default='女',verbose_name='性别')
    portrait=models.ImageField(upload_to='image/%Y/%m',default='image/default.png',max_length=100,verbose_name='头像')
 

    def __str__(self):
        return self.username

class EmailVerifyReord(models.Model):
    code=models.CharField(max_length=20,verbose_name='验证码')
    email=models.EmailField(max_length=50,verbose_name='邮箱')
    send_type=models.CharField(choices=(('register','注册'),('find_back_pwd','找回密码')),max_length=20)
    send_time=models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table='邮箱验证码'

class Banner(models.Model):
    title=models.CharField(max_length=50,verbose_name='标题')
    img=models.ImageField(max_length=100,upload_to='Banner/%Y/%m',verbose_name='轮播图')
    url=models.URLField(max_length=200,verbose_name='访问地址')
    index=models.IntegerField(default=100,verbose_name='顺序')
    add_time=models.DateTimeField(auto_now=True,verbose_name='添加时间')

    class Meta:
        db_table='轮播图'