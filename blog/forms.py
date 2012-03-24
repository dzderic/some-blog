from django.contrib.auth.forms import AuthenticationForm
from bootstrap.forms import BootstrapForm, Fieldset

class BootstrapAuthenticationForm(AuthenticationForm, BootstrapForm):
    class Meta:
        layout = (
            Fieldset("Login", "username", "password"),
        )
