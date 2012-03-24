from django.contrib.auth.forms import AuthenticationForm
from django import forms
from bootstrap.forms import BootstrapForm, Fieldset

from .models import Post

class BootstrapAuthenticationForm(AuthenticationForm, BootstrapForm):
    class Meta:
        layout = (
            Fieldset("Login", "username", "password"),
        )

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')
