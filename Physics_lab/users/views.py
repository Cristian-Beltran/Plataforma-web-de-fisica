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
# forms
from users.forms import LoginForm, SignUpForm
from users.forms import UpdateStudentForm,UpdateTeacherForm

# Forms
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


@login_required
def logout_view(request):
    """Logout a user"""
    logout(request)
    return redirect('index')


@login_required
def perfil_student_view(request):
    """Profile view"""
    user = request.user
    student = request.user.student
    return render(request,'users/student.html',{'user':user,'student':student})

@login_required
def perfil_teacher_view(request):
    """Profile view"""
    user = request.user
    teacher = request.user.teacher
    return render(request,'users/teacher.html',{'user':user,'teacher':teacher})

@login_required
def update_student_view(request):
    """Modify Profile view"""
    user = request.user
    student = request.user.student
    schools = School.objects.all() 
    if request.method == 'POST': 
        form = UpdateStudentForm(request.POST,request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            student.picture = data['picture']
            student.school = School.objects.get(pk=data['school'])
            student.save()
            return redirect('perfil_student')
    else:
        form = UpdateStudentForm()
    return render(request,'users/update_student.html',{'user':user,'student':student,'form':form,'schools':schools})

@login_required()
def update_teacher_view(request):
    """Modify Profile view"""
    user = request.user
    teacher = request.user.teacher

    if request.method == 'POST':
        form = UpdateTeacherForm(request.POST,request.FILES,instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('perfil_teacher')
    else:
        form = UpdateTeacherForm()

    return render(request,'users/update_teacher.html',{'user':user,'teacher':teacher,'form':form})