from rest_framework import serializers
from wallApp.models import Post
from wallApp.models import Comment
from wallApp.models import User
from drf_extra_fields.relations import PresentablePrimaryKeyRelatedField
from datetime import date
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','first_name','last_name')

class CommentSerializer(serializers.ModelSerializer):
    user = PresentablePrimaryKeyRelatedField(
        queryset=User.objects.all(),
        presentation_serializer=UserSerializer
    )
    class Meta:
        model = Comment
        fields = ['comment', 'comment_likes', 'created_at','user']

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    post_owner=UserSerializer(source='user',read_only=True)
    class Meta:
        model=Post
        fields=['id','content','likes','created_at','updated_at','deleted_at','privacity_id','user_id','comments','post_owner']

