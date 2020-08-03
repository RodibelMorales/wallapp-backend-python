from django.urls import path, include
from wallApp.account import views

app_name='wallApp'

urlpatterns = [
    path('',include('djoser.urls')),
    path('',include('djoser.urls.authtoken')),
]
