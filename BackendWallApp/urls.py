
from django.contrib import admin
from django.urls import path

from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),

    #REST API URLS
    path('api/post/',include('wallApp.posts.urls','post_api')),
    path('api/comment/',include('wallApp.comments.urls','comment_api')),
    path('api/account/',include('wallApp.account.urls','account_api'))
]
