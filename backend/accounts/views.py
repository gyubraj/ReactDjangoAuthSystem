from django.contrib.auth import get_user_model
from rest_framework import viewsets
from .serializers import UserSerializer,AddressSerializer,ProfileSerializer
from rest_framework.permissions import BasePermission, SAFE_METHODS, AllowAny
from .models import Address,Profile
User=get_user_model()


class CustomUserPermission(BasePermission):

    messasge="Looks are you don't have permission dude"
    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True
        else:
            return request.user==User.objects.get(id=obj.id)

class NewCustomPermission(BasePermission):
    message="Hell no"
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        else:
            return obj.user==request.user


class UserDetails(viewsets.ModelViewSet,CustomUserPermission):
    permission_classes = [CustomUserPermission]
    serializer_class = UserSerializer
    queryset =User.objects.all()

class Addresses(viewsets.ModelViewSet,NewCustomPermission):
    permission_classes = [NewCustomPermission]
    serializer_class = AddressSerializer
    queryset = Address.objects.all()

class Profile(viewsets.ModelViewSet,NewCustomPermission):
    permission_classes = [NewCustomPermission]
    serializer_class = ProfileSerializer
    queryset = Profile.publicprofiles.all()




























# from django.shortcuts import render
# from rest_framework import viewsets
# from .models import Messages as Message
# from .serializers import UserSerializer,MessageSerializer
# from django.contrib.auth import get_user_model
# from rest_framework import generics
# from rest_framework.permissions import SAFE_METHODS,BasePermission,IsAuthenticated
# from rest_framework.authentication import TokenAuthentication
# User=get_user_model()
#
# # Create your views here.
# class CustomPermission(BasePermission):
#     message='I think you are not authenticated for this dude'
#
#     def has_object_permission(self, request, view, obj):
#         if request.method in SAFE_METHODS:
#             return True
#         return obj.user==request.user
#
# class MyPermission(BasePermission):
#
#     def has_object_permission(self, request, view, obj):
#         if request.method == 'GET':
#             return False
#         return True
#
#
# class UserInfo(viewsets.ModelViewSet):
#     serializer_class = UserSerializer
#     queryset = User.objects.all()
#
# class UserInfoDetail(viewsets.ModelViewSet):
#     serializer_class = UserSerializer
#     queryset = User.objects.all()
#
# class Messages(generics.ListCreateAPIView,MyPermission):
#     permission_classes = [MyPermission]
#     serializer_class = MessageSerializer
#     queryset = Message.objects.all()
#
# class MessagesDetails(generics.RetrieveUpdateDestroyAPIView,CustomPermission):
#     permission_classes = [CustomPermission]
#     queryset = Message.objects.all()
#     serializer_class = MessageSerializer

