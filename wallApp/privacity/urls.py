from django.urls import path
from wallApp.comments.views import (
    api_get_privacity_view,
    api_create_privacity_view,
    api_update_privacity_view,
    api_delete_privacity_view
)

app_name='wallApp'

urlpatterns=[
    path('get/',api_get_privacity_view,name='get'),
    path('create',api_create_privacity_view,name='create'),
    path('update/<privacity_id>',api_update_privacity_view,name='update'),
    path('delete/<privacity_id>',api_delete_privacity_view,name='delete')
]