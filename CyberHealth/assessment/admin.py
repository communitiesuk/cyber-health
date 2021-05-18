from django.contrib import admin
from assessment.models import *


class PathwayGroupAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class PathwayAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": (
        "short_name",)}
    filter_horizontal = ('controls',)


class ControlAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": (
        "title",)}


admin.site.register(Answer)
admin.site.register(Question)
admin.site.register(Choice)

admin.site.register(Control, ControlAdmin)

admin.site.register(PathwayGroup, PathwayGroupAdmin)
admin.site.register(Pathway, PathwayAdmin)

admin.site.register(Organisation)
admin.site.register(OrganisationRegion)
admin.site.register(OrganisationType)
