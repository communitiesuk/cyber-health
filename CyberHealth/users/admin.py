from django.contrib import admin
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import Organisation, OrganisationRegion, OrganisationType, OrganisationUser, UserProfile


def admin_method_attributes(**outer_kwargs):
    """ Wrap an admin method with passed arguments as attributes and values.
    DRY way of extremely common admin manipulation such as setting short_description, allow_tags, etc.
    """
    def method_decorator(func):
        for kw, arg in outer_kwargs.items():
            setattr(func, kw, arg)
        return func
    return method_decorator

class CustomUserAdmin(UserAdmin):
    list_display = ("_email", "_name", "is_staff")
    readonly_fields = ('_email', )     

    def _email(self, obj):
        return obj.get_username()
    _email.short_description = 'Email'
    _email.admin_order_field = 'email'
    
    def _name(self, obj):
        return obj.get_short_name()
    _name.short_description = 'Name'
    _name.admin_order_field = 'name'
    
    def get_form(self, request, obj, **kwargs):
        form = super(CustomUserAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['first_name'].label = 'Name'
        form.base_fields['username'].label = 'Email'
        form.base_fields["last_name"].widget = forms.HiddenInput()
        form.base_fields["email"].widget = forms.HiddenInput()
        return form

            # fieldsets = (
    #     ('Personal info', {'fields': ('first_name', 'email', 'password')}),
    #     ('Important dates', {'fields': ('last_login', 'date_joined')}),
    #     ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    # )

admin.site.register(Organisation)
admin.site.register(OrganisationRegion)
admin.site.register(OrganisationType)
admin.site.register(OrganisationUser)

admin.site.register(UserProfile)
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
