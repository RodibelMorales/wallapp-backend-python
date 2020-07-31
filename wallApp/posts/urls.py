from django.urls import path
from wallApp.posts.views import (
    api_get_posts_view,
    api_create_posts_view,
    api_update_posts_view,
    api_delete_posts_view
)

app_name='wallApp'

urlpatterns=[
    path('get/',api_get_posts_view,name='get'),
    path('create',api_create_posts_view,name='create'),
    path('update/<post_id>',api_update_posts_view,name='update'),
    path('delete/<post_id>',api_delete_posts_view,name='delete')
]