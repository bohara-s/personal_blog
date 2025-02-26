from django.http import HttpResponse
from django.shortcuts import render

from django.shortcuts import render
from blog.models import BlogPost  # Import BlogPost model

def home(request):
    latest_posts = BlogPost.objects.all().order_by('-created_at')[:5]  # Get latest 5 posts
    return render(request, 'home.html', {'latest_posts': latest_posts})


def about(request):
    return render(request,'about.html')
