from django.contrib import admin

from assessment.models import Organisation, OrganisationRegion, OrganisationType

admin.site.register(Organisation)
admin.site.register(OrganisationRegion)
admin.site.register(OrganisationType)

