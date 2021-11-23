"""Labs views."""

# Django
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
#  Forms
from labs.forms import LabForm, FilterLabForm
# Models
from labs.models import Lab 
from groups.models import Group




@login_required
def list_lab_view(request):
    user = request.user
    labs = Lab.objects.filter(visible=True).filter(public=True).order_by('created_at') 
    if not request.user.groups.filter(name__in=['Docente']):
        groups = Group.objects.filter(students=request.user.student)
    else:
        groups = Group.objects.filter(teacher=request.user.teacher) 
        
    form = FilterLabForm()

    return render(request,'labs/list.html',{'labs':labs,'groups':groups,'form':form})

@login_required
def create_lab_view(request):
    user = request.user
    """Create new post"""
    if request.method == 'POST':
        form = LabForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = LabForm()
    return render(request,'labs/new.html',{'form':form,'teacher':request.user.teacher})