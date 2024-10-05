from rest_framework.serializers import ModelSerializer
from coreapp.models import Post
from django.contrib.auth.models import User

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['name'] = user.first_name
        token['username'] = user.username
        return token
    

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["username","email"]

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','author','title','body','created','updated','cat_type','photo','age']
        