from django.shortcuts import render
from apiapp.serializers import PostSerializer
from coreapp.models import Post
from rest_framework.views import APIView,Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsAuthorOrReadOnly
from rest_framework import viewsets
# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly,IsAuthorOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer