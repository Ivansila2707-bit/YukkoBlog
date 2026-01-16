from django.shortcuts import render, get_object_or_404
from .models import Articles

def about(request):
    return render(request, 'app/about.html')

def posts(request):
    posts = Articles.objects.all()
    return render(request, 'app/posts.html', {'posts': posts})

def mail(request):
    return render(request, 'app/mail.html')

def post_detail(request, post_id):
    post = get_object_or_404(Articles, id=post_id)
    return render(request, 'app/post_detail.html', {'post': post})