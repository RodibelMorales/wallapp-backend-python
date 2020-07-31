from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from wallApp.models import Post
from wallApp.posts.serializers import PostSerializer
from django.contrib.auth.models import User


@api_view(['GET',])
def api_get_posts_view(request):
    try:
        wallposts=Post.objects.get()
        serializer=PostSerializer(wallposts)
        return Response(serializer.data,status=status.HTTP_200_OK)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST',])
def api_create_posts_view(request):
    data={}
    PostData=Post(
        user_id=int(request.data['user_id']),
        privacity_id=int(request.data['privacity_id'])
    )
    serializer=PostSerializer(PostData,data=request.data)
    try:
        if serializer.is_valid():
            serializer.save()
            data["status"]="success"
            data["message"]="post created"
            data["response"]=serializer.data
            return Response(data,status=status.HTTP_201_CREATED)
    except Exception as inst:
        data["status"]="error"
        data["message"]=inst.args 
        return Response(data,status=status.HTTP_400_BAD_REQUEST)

@api_view(['UPDATE',])
def api_update_posts_view(request,post_id):
    try:
        wallposts=Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer=PostSerializer(wallposts,data=request.data)
    data={}
    if serializer.is_valid():
        serializer.save()
        data["status"]="success"
        data["message"]="POST updated"
        return Response(data=data,status=status.HTTP_200_OK)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE',])
def api_delete_posts_view(request,post_id):
    try:
        wallposts=Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    delete=wallposts.delete()
    data={}
    if delete:
        data["status"]="success"
        data["message"]="post deleted"
    else:
        data["status"]="error"
        data["message"]="can´t delete post"
    return Response(data=data,status=status.HTTP_200_OK)