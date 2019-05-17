from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','is_active','first_name','last_name','password']