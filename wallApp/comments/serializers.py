from rest_framework import serializers
from django.contrib.auth.models import User
from wallApp.models import Comment
from wallApp.models import Post

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields=[
            'content',
            'likes',
            'created_at',
            'updated_at',
            'deleted_at',
            'post_id',
            'user_id',
        ]