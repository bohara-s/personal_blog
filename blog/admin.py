from django.contrib import admin
from .models import BlogPost  # Import your model
from blog.models import Comment


admin.site.register(BlogPost)
admin.site.register(Comment)
