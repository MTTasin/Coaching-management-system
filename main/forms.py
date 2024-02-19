from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import profile, class_topic, students_attandance
from django.forms import ModelForm
from django.contrib.admin.widgets import FilteredSelectMultiple


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = profile
        fields = ['image']


class topic_dateinput(forms.DateInput):
    input_type = 'date'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.format = '%Y-%m-%d'



class topicForm(forms.ModelForm):
    class Meta:
        model = class_topic
        fields = ['title', 'courses', 'description', 'date']
        widgets = {
            'date': topic_dateinput
        }



class students_attandanceForm(forms.ModelForm):
    class Meta:
        model = students_attandance
        fields = ['name', 'date']
        widgets = {
            'date': topic_dateinput,
            'name': FilteredSelectMultiple('Name', True),
        }

    