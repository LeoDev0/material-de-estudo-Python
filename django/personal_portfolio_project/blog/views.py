from django.shortcuts import render, get_object_or_404
from .models import Posts

def all_blogs(request):
  posts = Posts.objects.order_by('-date')[:5]
  return render(request, 'blog/all_blogs.html', {'posts': posts})

def detail(request, blog_id):
  blog = get_object_or_404(Posts, pk=blog_id)
  return render(request, 'blog/detail.html', {'id': blog})