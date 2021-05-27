from django.contrib import admin
from .models import Organisation, OrganisationRegion, OrganisationType, OrganisationUser, UserProfile

admin.site.register(Organisation)
admin.site.register(OrganisationRegion)
admin.site.register(OrganisationType)
admin.site.register(OrganisationUser)

admin.site.register(UserProfile)
