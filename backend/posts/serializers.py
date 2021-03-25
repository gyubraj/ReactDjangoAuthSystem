from rest_framework import serializers
from .models import Post,Likes,Comments

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Likes
        fields='__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comments
        fields='__all__'


class PostSerializer(serializers.ModelSerializer):
    like=LikeSerializer(many=True)
    comment=CommentSerializer(many=True)
    class Meta:
        model=Post
        fields=['id','description','user','created_at','public','comment','like']

