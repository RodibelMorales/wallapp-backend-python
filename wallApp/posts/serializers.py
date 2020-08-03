from rest_framework import serializers
from wallApp.models import Post
from wallApp.models import Comment
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['comment', 'comment_likes', 'created_at']

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model=Post
        fields=['id','content','likes','created_at','updated_at','deleted_at','privacity_id','user_id','comments']