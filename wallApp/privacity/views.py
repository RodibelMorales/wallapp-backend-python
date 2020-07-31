from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from wallApp.privacity.serializers import PrivacitySerializer

from wallApp.models import Privacity

@api_view(['GET',])
def api_get_privacity_view():
    try:
        serializer=PrivacitySerializer(Privacity.objects.get())
        return Response(serializer.data,status=status.HTTP_200_OK)
    except Privacity.DoesNotExist: 
        return Response(status=status.HTTP_200_OK)

@api_view(['POST',])
def api_create_privacity_view(request):
    data={}
    try:
        serializer=PrivacitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data['status']='success'
            data['message']='new privacity created'
            return Response(data,status=status.HTTP_201_CREATED)
        except Exception as inst:
            data['status']='error'
            data['message']=inst.args
            return Response(data,status=status.HTTP_400_BAD_REQUEST)

@api_view(['UPDATE',])
def api_update_privacity_view(request,privacity_id):
    data={}
    try:
        privacity=Privacity.objects.get(pk=privacity_id)
        serializer=PrivacitySerializer(privacity,data=request.data)
        if serializer.is_valid():
            serializer.save()
            data["status"]="success"
            data["message"]="Privacity updated"
            return Response(data=data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    except Privacity.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE',])
def api_delete_privacity_view(request,privacity_id):
    data={}
    try:
        privacity=Privacity.objects.get(pk=privacity_id)
        if privacity.delete() :
            data["status"]="success"
            data["message"]="privacity deleted"
        else:
            data["status"]="error"
            data["message"]="can´t delete privacity"
        return Response(data=data,status=status.HTTP_200_OK)
    except Comment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)



