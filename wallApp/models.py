from django.db import models
from django.contrib.auth.models import User

class Privacity(models.Model):
    name=models.CharField(max_length=45)
    created_at=models.DateTimeField()
    updated_at=models.DateTimeField()
    deleted_at=models.DateTimeField()

class Post(models.Model):
    content=models.CharField(max_length=255)
    likes=models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    privacity_id = models.ForeignKey(Privacity, on_delete=models.CASCADE)
    created_at=models.DateTimeField()
    updated_at=models.DateTimeField()
    deleted_at=models.DateTimeField()

class Comment(models.Model):
    content=models.CharField(max_length=255)
    likes=models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at=models.DateTimeField()
    updated_at=models.DateTimeField()
    deleted_at=models.DateTimeField()

class Photo(models.Model):
    src=models.URLField()
    privacity = models.ForeignKey(Privacity, on_delete=models.CASCADE)
    created_at=models.DateTimeField()
    updated_at=models.DateTimeField()
    deleted_at=models.DateTimeField()
    user= models.ManyToManyField(User)
    post = models.ManyToManyField(Post)
    comment = models.ManyToManyField(Comment)

