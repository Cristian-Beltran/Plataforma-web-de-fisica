"""Users Forms"""
# Django
from django import forms
# Model
from users.models import Student,Teacher,School
from django.contrib.auth.models import User

# User authenticate

from django.contrib.auth import authenticate

class LoginForm(forms.Form):
    """Log in Form"""
    username = forms.CharField()
    password = forms.CharField()
    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        password = cleaned_data.get("password")
        username = cleaned_data.get("username")

        if not User.objects.filter(username=username).exists():
            self.add_error('username','El usuario no existe')
            if not User.objects.filter(username=username,password=password).exists():
                self.add_error('password','Contraseña incorrecta')
        
        return cleaned_data


class SignUpForm(forms.Form):
    """Sign Up Form"""
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    password = forms.CharField()
    password_confirm = forms.CharField()

    def clean(self):
        cleaned_data = super(SignUpForm, self).clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        username = cleaned_data.get("username")

        if password != password_confirm:
            self.add_error('password_confirm','La contraseña no coincide')

        if User.objects.filter(username=username).exists():
            self.add_error('username','El usuario ya existe')

        return cleaned_data

class UpdateTeacherForm(forms.ModelForm):
    """Update teacher form."""
    class Meta:
        model = Teacher
        fields = ['picture','biography','schools']
    schools = forms.ModelMultipleChoiceField(queryset=School.objects.all(),widget=forms.CheckboxSelectMultiple(attrs={'class':'input'}))
    

class UpdateStudentForm(forms.Form):
    """Post model form."""
    school = forms.CharField()
    picture = forms.ImageField()
 
