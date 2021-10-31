"""Posts views."""

# Django
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
#  Forms
from posts.forms import PostForm
# Models
from posts.models import Post

def list_post_view(request):
    posts = Post.objects.all().order_by('created_at')
    return render(request,'posts/list.html')

@login_required
def create_post_view(request):
    """Create new post"""
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request,'posts/new.html',{'form':form,'teacher':request.user.teacher})

@login_required
def update_post_view(request):
    """Update post"""
    if request.method == 'POST':
        form = PostForm(request.POST,request.FIlES)
        if form.is_valid():
            form.save()
            return redirect('Profile')
    return render(request,'posts/new.html',{'form':form,'user':request.user,'teacher':request.user.teacher})

@login_required
def delete_post_view(request):
    """Delete post"""


def list_post_view(request):
    """List post"""