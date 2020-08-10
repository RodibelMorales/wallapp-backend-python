from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from wallApp.models import Post
from wallApp.models import Comment
from django.contrib.auth.models import User

from wallApp.comments.serializers import CommentSerializer

@api_view(['GET',])
def api_get_comments_view(request):
    try:
        postComments=Comment.objects.get()
        serializer = CommentSerializer(postComments)
        return Response(serializer.data,status=status.HTTP_200_OK)
    except Comment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST',])
@permission_classes([IsAuthenticated])
def api_create_comment_view(request):
    data={}
    CommentData=Comment(
        post_id=int(request.data['post_id']),
        user_id=int(request.data['user_id'])
    )
    serializer=CommentSerializer(CommentData,data=request.data)
    try:
        if serializer.is_valid():
            serializer.save()
            data["status"]="success"
            data["message"]="comment created"
            data["response"]=serializer.data
            return Response(data,status=status.HTTP_201_CREATED)
    except Exception as inst:
        data["status"]="error"
        data["message"]=inst.args
        return Response(data,status=status.HTTP_400_BAD_REQUEST)

@api_view(['UPDATE',])
@permission_classes([IsAuthenticated])
def api_update_comment_view(request,comment_id):
    data={}
    try:
        comment=Comment.objects.get(pk=comment_id)
        serializer=CommentSerializer(comment,data=request.data)
        if serializer.is_valid():
            serializer.save()
            data["status"]="success"
            data["message"]="Comment updated"
            return Response(data=data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    except Comment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
@api_view(['DELETE',])
@permission_classes([IsAuthenticated])
def api_delete_comment_view(request,comment_id):
    data={}
    try:
        delcomment=Comment.objects.get(pk=comment_id)
        if delcomment.delete() :
            data["status"]="success"
            data["message"]="comment deleted"
        else:
            data["status"]="error"
            data["message"]="can´t delete comment"
        return Response(data=data,status=status.HTTP_200_OK)
    except Comment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
