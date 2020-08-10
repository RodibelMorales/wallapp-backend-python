import json

from django.urls import reverse;
from rest_framework import status;
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase,APIRequestFactory,RequestsClient,APIClient

from wallApp.posts.serializers import PostSerializer
from wallApp.models import Post

class PostTestCase(APITestCase):
    def test_create_post(self):
        factory = APIRequestFactory()
        data={"content":"test insert","likes":0,"privacity_id":1,"user_id":13}
        factory.post('/api/post/create',data)

class CommentTestCase(APITestCase):
    def test_create_comment(self):
        factory = APIRequestFactory()
        data={"comment":"test insert comment","comment_likes":0,"post_id":3,"user_id":13}
        factory.post('/api/comment/create',data)
class UserTestCase(APITestCase):
    def test_create_user(self):
        factory=APIRequestFactory()
        data={"username":"rmorales@wall.com","first_name":"Rodibel","last_name":"Morales","phone":9841883666,"email":"demo@wall.com","password":"medalofhonor1993","re_password":"medalofhonor1993"}
        factory.post('/api/account/users/',data)
class UserLoginTestCase(APITestCase):
    def test_login_user(self):
        client = APIClient()
        client.login(username='demo@wall.com', password='medalofhonor1993')

    def test_logout_user(self):
        client = APIClient()
        client.logout()

class GetPosts():
    
    def test_get_posts(self):
        client = RequestsClient()
        response = client.get('http://127.0.0.1:8000/api/post/get/')
        assert response.status_code == 200

    