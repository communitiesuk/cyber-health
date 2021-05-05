from django.contrib import admin
from .models import *


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
