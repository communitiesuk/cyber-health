from django.contrib import admin
from assessment.models import Organisation, OrganisationRegion, OrganisationType, Answer, Question, Choice, PathwayGroup, Pathway


class PathwayGroupAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class PathwayAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": (
        "short_name",)}


admin.site.register(Answer)
admin.site.register(Question)
admin.site.register(Choice)

admin.site.register(PathwayGroup, PathwayGroupAdmin)
admin.site.register(Pathway, PathwayAdmin)


admin.site.register(Organisation)
admin.site.register(OrganisationRegion)
admin.site.register(OrganisationType)
