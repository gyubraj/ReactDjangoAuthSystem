#
from django.contrib import admin
from django.urls import path,include,re_path
from django.views.generic import TemplateView
from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title='Date App')
urlpatterns = [
    path('swagger/',schema_view),
    path('admin/', admin.site.urls),
    path('auth/',include('djoser.urls')),
    path('auth/',include('djoser.urls.jwt')),
    path('auth/',include('djoser.social.urls')),


    path('accounts/',include('accounts.urls')),

    path('posts/',include('posts.urls')),

]

urlpatterns +=[
    re_path(r'^.*',TemplateView.as_view(template_name='index.html'))
]

