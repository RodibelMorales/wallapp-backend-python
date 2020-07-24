from django.urls import path

from wallApp.api.views import api_get_posts_view

app_name='wallApp'

urlpatterns=[
    path('all/',api_get_posts_view,name='all'),
]