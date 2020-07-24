from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from wallApp.models import Post
from wallApp.api.serializers import PostSerializer

@api_view(['GET',])
def api_get_posts_view(request):
    try:
        wallposts=Post.objects.get()
        
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer=PostSerializer(wallposts)
    return Response(serializer.data)