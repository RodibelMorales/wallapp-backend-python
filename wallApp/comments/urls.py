from django.urls import path
from wallApp.comments.views import (
    api_get_comments_view,
    api_create_comment_view,
    api_update_comment_view,
    api_delete_comment_view
)

app_name='wallApp'

urlpatterns=[
    path('get/',api_get_comments_view,name='get'),
    path('create',api_create_comment_view,name='create'),
    path('update/<comment_id>',api_update_comment_view,name='update'),
    path('delete/<comment_id>',api_delete_comment_view,name='delete')
]