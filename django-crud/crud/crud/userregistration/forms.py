from pyexpat import model
from django import forms
from .models import User

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('name', 'password', 'date_of_birth')
        widgets={
            'password' : forms.PasswordInput(render_value=True),
            'date_of_birth': forms.DateInput(),
        }
