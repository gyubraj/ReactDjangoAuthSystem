from django.contrib import admin
from .models import UserAccount,Address,Profile

# Register your models here.

admin.site.register([UserAccount,Address,Profile])