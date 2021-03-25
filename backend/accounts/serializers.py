from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers
# from .models import Messages
User=get_user_model()
from .models import Address,Profile

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model=User
        fields=('id','email','first_name','last_name','password')

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model=Address
        fields='__all__'
        fields='__all__'


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields='__all__'


class UserSerializer(serializers.ModelSerializer):
    address=AddressSerializer()
    profile=ProfileSerializer()
    class Meta:
        model=User
        fields=['id','email','first_name','last_name','deactivate','address','profile']

# testing

# class UserSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model=User
#         fields='__all__'
#
# class MessageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model= Messages
#         fields= '__all__'
#         depth=1