from django.shortcuts import render
from .models import Posts

def all_blogs(request):
  posts = Posts.objects.order_by('-date')[:5]
  return render(request, 'blog/all_blogs.html', {'posts': posts})
