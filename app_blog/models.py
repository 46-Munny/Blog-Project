from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class blog(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='post_author')
    blog_title=models.CharField(max_length=264, verbose_name='put a title')
    slug=models.SlugField(max_length=264,unique=True)
    blog_content=models.TextField(verbose_name="What's your name")
    blog_image=models.ImageField(upload_to='blog_images',verbose_name="Image")
    publish_date=models.DateTimeField(auto_now_add=True)
    update_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.blog_title


class comment(models.Model):
        blogc=models.ForeignKey(blog,on_delete=models.CASCADE,related_name='blog_comment')
        user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_comment')
        comments=models.TextField()
        comment_date=models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return self.comments


class likes(models.Model):
    blogc=models.ForeignKey(blog,on_delete=models.CASCADE,related_name='blog_like')
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_like')
    def __str__(self):
        return self.user + " likes " + self.blog
