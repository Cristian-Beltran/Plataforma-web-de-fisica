"""Users views"""

# Django
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout

# Models
from django.contrib.auth.models import User
from users.models import Student,School
from groups.models import Group
# Exception
from django.db.utils import IntegrityError

# Forms
from users.forms import LoginForm, SignUpForm

def login_view(request):
    """Login view."""
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            username = data['username']
            password = data['password']
            user = authenticate(request,username=username,password=password)
            login(request,user)
            return redirect('index')
    else:
        form = LoginForm() 
    return render(request,'users/login.html',{'form':form})

def signup_view(request):
    """Sign up view"""
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            username = data['username']
            password = data['password']
            user = User.objects.create_user(username=username, password=password)
            user.first_name = data['first_name']
            user.last_name = data['last_name'] 
            user.email = data['email']
            
            user.save()

            student = Student(user=user)
            student.save()

            return redirect('login')

    else:
        form = SignUpForm()
    return render(request,'users/signup.html',{'form':form})



def perfil_student_view(request):
    """Profile view"""
    user = request.user
    student = request.user.student
    groups = Group.objects.filter(students__pk=student.pk)
    return render(request,'users/student.html',{'user':user,'student':student,'groups':groups})

def perfil_teacher_view(request):
    """Profile view"""
    user = request.user
    teacher = request.user.teacher
    groups = Group.objects.filter(teacher=teacher.pk)
    return render(request,'users/teacher.html',{'user':user,'teacher':teacher,'groups':groups})

@login_required
def update_student_view(request):
    """Modify Profile view"""
    user =request.user.student
    if request.method == 'POST':
        form = UpdateStudentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect()

@login_required()
def update_teacher_view(request):
    """Modify Profile view"""
    user =request.user.teacher



@login_required
def logout_view(request):
    """Logout a user"""
    logout(request)
    return redirect('index')
