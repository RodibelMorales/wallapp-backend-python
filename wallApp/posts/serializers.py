from rest_framework import serializers
from django.contrib.auth.models import User
from wallApp.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=['content','likes','created_at','updated_at','deleted_at','privacity_id','user_id']