from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    email=models.EmailField(verbose_name='email',max_length=200,unique=True)
    phone=models.CharField(null=True,max_length=30)
    REQUIRED_FIELDS=['username','first_name','last_name','phone']
    USERNAME_FIELD='email'
    
    def get_username(self):
        return self.email

class Privacity(models.Model):
    name=models.CharField(max_length=45)
    created_at=models.DateTimeField(default=timezone.now)
    updated_at=models.DateTimeField(null=True)
    deleted_at=models.DateTimeField(null=True)

class Post(models.Model):
    content=models.CharField(max_length=255)
    likes=models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='post_owner', on_delete=models.CASCADE)
    privacity = models.ForeignKey(Privacity,related_name='privacity', on_delete=models.CASCADE)
    created_at=models.DateTimeField(default=timezone.now)
    updated_at=models.DateTimeField(null=True)
    deleted_at=models.DateTimeField(null=True)

class Comment(models.Model):
    comment=models.CharField(max_length=255)
    comment_likes=models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='comment_owner',on_delete=models.CASCADE)
    post = models.ForeignKey(Post,related_name='comments', on_delete=models.CASCADE)
    created_at=models.DateTimeField(default=timezone.now)
    updated_at=models.DateTimeField(null=True)
    deleted_at=models.DateTimeField(null=True)

class Photo(models.Model):
    src=models.URLField()
    privacity = models.ForeignKey(Privacity, on_delete=models.CASCADE)
    created_at=models.DateTimeField(default=timezone.now)
    updated_at=models.DateTimeField(null=True)
    deleted_at=models.DateTimeField(null=True)
    user= models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='photo_owner')
    post = models.ManyToManyField(Post,related_name='photos')
    comment = models.ManyToManyField(Comment)

