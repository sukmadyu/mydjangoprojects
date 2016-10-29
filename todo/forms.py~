from django import forms
#import re
#from django.core.exceptions import ObjectDoesNotExist
#from django.forms import ModelForm
#from todo.data.models import *
from .models import User

class SignupForm(forms.ModelForm):
    class Meta:
        model=User
        fields = ('fname', 'password',)
