from django.urls import path
from .views import *
urlpatterns=[
    path('',PostsView.as_view({
        'get':'list'
    })),
    path('<int:pk>/',PostsView.as_view({
        'get':'retrieve'
    })),

    path('likes/',LikeView.as_view({
        'get':'list'
    })),
    path('comments/',CommentView.as_view({
        'get':'list'
    }))
]