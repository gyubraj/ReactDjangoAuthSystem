from django.contrib import admin
from .models import Post,Likes,Comments
# Register your models here.

admin.site.register([Post,Likes,Comments])