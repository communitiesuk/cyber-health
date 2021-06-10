from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import password_validation
from django.forms import widgets
from .models import Organisation


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(
        required=True,
        label="Name",
        widget=forms.TextInput(
            attrs={
                'autocomplete': 'name',
                'field_type': 'text'
                }))
    email = forms.EmailField(
            help_text='Must be a .gov.uk local authority email address',
            required=True,
            label="Email",
            widget=forms.TextInput(
                attrs={
                    'autocomplete': 'email',
                    'field_type': 'email'
                    }))
    password1 = forms.CharField(
        help_text='<ul>'
                  '<li>Your password must contain at least 8 characters</li>'
                  '<li>Your password must not be too similar to your other '
                  'personal information</li>'
                  '<li>Your password must not be a commonly used password</li>'
                  '<li>Your password must not be entirely numeric </li>'
                  '</ul>',
        required=True,
        label="Password",
        widget=forms.TextInput(
            attrs={
                'autocomplete': 'new-password',
                'field_type': 'password'
                }))
    password2 = forms.CharField(
        required=True,
        label="Confirm password",
        widget=forms.TextInput(
            attrs={
                'autocomplete': 'new-password',
                'field_type': 'password'
                }))

    class Meta:
        model = User
        fields = ['first_name', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.error_messages = {'required': 'Enter {fieldname}'.format(
                fieldname=field.label).capitalize()}

    def clean_email(self):
        email = self.data['email']
        if not Organisation.objects.filter(
                domain_name=email.split('@')[-1]).exists():
            self.add_error('email', 'Must use a .gov.uk email address related '
                           ' to a council')
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
