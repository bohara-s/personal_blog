from django.shortcuts import render, get_object_or_404
from .models import BlogPost, Comment
from django.contrib.auth.decorators import login_required


# List all blog posts
def blog_list(request):
    posts = BlogPost.objects.all().order_by('-created_at')  # Fetch posts from DB
    return render(request, 'blog/blog_list.html', {'posts': posts})

# Show single blog post
def blog_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    
    if request.method == "POST":
        content = request.POST.get('comment')
        if content:
            Comment.objects.create(post=post, author=request.user, content=content)
    
    return render(request, 'blog/blog_detail.html', {'post': post})
