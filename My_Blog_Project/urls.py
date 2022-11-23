from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/',include('app_login.urls')),
    path('blog/',include('app_blog.urls')),
    path('',views.index,name="index" ),
]
