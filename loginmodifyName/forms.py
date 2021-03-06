from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms



class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class MailForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'username')
        labels = {
            'username':'Pseudo',
            'email':'Email'
        }