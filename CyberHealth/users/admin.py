from django.contrib import admin
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import Organisation, OrganisationRegion, OrganisationType, OrganisationUser, UserProfile

class CustomUserAdmin(UserAdmin):
     def get_form(self, request, obj, **kwargs):
        form = super(CustomUserAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['first_name'].label = 'Name'
        form.base_fields['username'].label = 'Email'
        form.base_fields["last_name"].widget = forms.HiddenInput()
        form.base_fields["email"].widget = forms.HiddenInput()
        return form

admin.site.register(Organisation)
admin.site.register(OrganisationRegion)
admin.site.register(OrganisationType)
admin.site.register(OrganisationUser)

admin.site.register(UserProfile)
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
