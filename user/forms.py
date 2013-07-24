from django import forms
from user.models import Participante
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Participante
        exclude = ('user','esteve_presente')