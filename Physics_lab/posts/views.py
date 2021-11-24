"""Posts views."""

# Django
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
#  Forms
from posts.forms import PostForm, FilterPostForm
# Models
from posts.models import Post
from groups.models import Group

@login_required
def list_post_view(request):
    user = request.user
    posts = Post.objects.filter(visible=True).filter(public=True).order_by('created_at') 
    if not request.user.groups.filter(name__in=['Docente']):
        groups = Group.objects.filter(students=request.user.student)
    else:
        groups = Group.objects.filter(teacher=request.user.teacher)
    
    form = FilterPostForm()

    return render(request,'posts/list.html',{'posts':posts,'groups':groups,'form':form})

@login_required
def create_post_view(request):
    user = request.user
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
def post_view(request,id):
    user = request.user
    post = Post.objects.get(id=id)
    return render(request,'posts/post.html',{'post':post,'user':user})