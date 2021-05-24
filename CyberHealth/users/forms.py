from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import password_validation
from .models import Organisation


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(required=True, label="First name")
    last_name = forms.CharField(required=True, label="Last name")
    email = forms.EmailField(required=True, label="Email", help_text='Must be a .gov.uk local authority email address')
    password1 = forms.CharField(required=True, label="Password", error_messages={'password_too_short': 'My error message for too short passwords'})
    password2 = forms.CharField(required=True, label="Confirm password")

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)   
        for field in self.fields.values():
            field.error_messages = {'required': 'Enter {fieldname}'.format(
                fieldname=field.label).capitalize()}

    def clean_email(self):
        email = self.data['email']
        if not Organisation.objects.filter(domain_name=email.split('@')[-1]).exists():
            self.add_error('email', 'Must use a .gov.uk email address related to a council')
        return email


    def _post_clean(self):
        super(UserRegisterForm, self)._post_clean()
        password = self.cleaned_data.get('password1')

        # Ensures password1 has the same validation errors as password2
        if password:
            try:
                password_validation.validate_password(password, self.instance)
            except forms.ValidationError as error:
                self.add_error('password1', error)



class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)       
        self.error_messages['invalid_login'] = "Enter a valid email \
        and password combination. You will be locked out if you enter \
        the wrong details 5 times."

        for field in self.fields.values():
            field.error_messages = {'required': 'Enter {fieldname}'.format(
                fieldname=field.label).capitalize()}
