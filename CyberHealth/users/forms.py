from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    # Temp fix until user model field gets changed 
    # from username to email 
    username = forms.CharField(required=True, label="Email")

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.error_messages['invalid_login'] = "Enter a valid email \
        and password combination. You will be locked out if you enter \
        the wrong details 5 times."

        for field in self.fields.values():
            field.error_messages = {'required': 'Enter {fieldname}'.format(
                fieldname=field.label).capitalize()}
