from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()
# Create your models here.

class Post(models.Model):
    class PublicPosts(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(public=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    description=models.TextField(max_length=255,null=True,blank=True)
    public=models.BooleanField(default=True)

    created_at=models.DateTimeField(auto_now_add=True)

    objects=models.Manager()
    publicPosts=PublicPosts()

    @property
    def like(self):
        return self.likes_set.all()

    @property
    def comment(self):
        return self.comments_set.all()

    def __str__(self):
        return str(self.id)+self.description[:10]

class Likes(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)

    @property
    def likers(self):
        return self.user.first_name

    def __str__(self):
        return self.user.first_name+self.post.description[:5]

class Comments(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    comment=models.TextField(max_length=255)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.post.id)+self.comment




