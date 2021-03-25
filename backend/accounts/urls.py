from django.urls import path
from .views import *

urlpatterns=[
    path('',UserDetails.as_view({
        'get':'list'
    })),
    path('<int:pk>/',UserDetails.as_view({
        'get':'retrieve',
        'delete':'destroy'
    })),
    path('address/',Addresses.as_view({
        'get':'list',
        'post':'create'
    })),
    path('address/<int:pk>/',Addresses.as_view({
        'get':'retrieve',
        'put':'update',
        'patch':'partial_update',
        'delete':'destroy'
    })),
    path('profile/',Profile.as_view({
        'get':'list'
    }))
]
# urlpatterns = [
#
#     path('',UserInfo.as_view({
#         'get':'list',
#         'post':'create'
#     })),
#     path('<int:pk>/',UserInfoDetail.as_view({
#         'get':'retrieve',
#         'patch':'partial_update',
#         'delete':'destroy'
#
#     })),
#
#     path('messages/',Messages.as_view()),
#     path('messages/<int:pk>/',MessagesDetails.as_view())
#
#     ]