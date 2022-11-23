
from django.urls import path
from app_blog import views


app_name='app_blog'

urlpatterns = [
    path('',views.BlogList.as_view(),name="blogList" ),
    path('write/',views.CreateBlog.as_view(),name="create_blog" ),
    path('details/<int:id>',views.blog_details,name="blog_details" ),
    path('liked/<pk>/', views.liked, name='liked_post'),
    path('unliked/<pk>/', views.unliked, name='unliked_post'),
    ]
