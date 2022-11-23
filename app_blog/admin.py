from django.contrib import admin
from app_blog.models import blog,comment,likes
# Register your models here.
admin.site.register(blog)
admin.site.register(comment)
admin.site.register(likes)
