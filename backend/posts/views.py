from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PostSerializer,Post,CommentSerializer,Comments,LikeSerializer,Likes
from rest_framework.permissions import AllowAny
# Create your views here.

class PostsView(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = PostSerializer
    queryset =Post.objects.all()

class LikeView(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = LikeSerializer
    queryset = Likes.objects.all()

class CommentView(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = CommentSerializer
    queryset = Comments.objects.all()
