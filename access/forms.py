from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    #Den här jälva UserCreationForm verkar fucking kräva att det finns username, password1 och password2
    

    class Meta:
        model = User
        fields = ['username', 'email', 'password1','password2']