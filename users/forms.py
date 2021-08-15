from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        # class meta gives us a nested namespace for configurations and
        # keeps the configurationsin one space. so whitin the configuration we are saying
        #model will be affected assagidaki user madel and fields be llike this
        model = User
        fields = ['username', 'email', 'password1', 'password2']
