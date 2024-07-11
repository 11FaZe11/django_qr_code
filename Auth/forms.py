from django.forms import ModelForm
from .models import *  # Import specific model instead of *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'  # Removed duplicate fields assignment

class CreateUserForm(UserCreationForm):
    id = forms.IntegerField(label='Your ID', min_value=1, max_value=999999)  # Moved outside Meta

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'id']  # Added 'id' to fields list