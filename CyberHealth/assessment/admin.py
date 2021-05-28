from django.forms import Textarea
from django.contrib import admin
from assessment.models import (
    Organisation, OrganisationRegion, OrganisationType, Answer, Question,
    PathwayGroup, Pathway, Control, SubControl
)
                                


class PathwayGroupAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class PathwayAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": (
        "short_name",)}
    filter_horizontal = ('controls',)

    def get_form(self, request, obj=None, **kwargs):
        kwargs['widgets'] = {'intro_text': Textarea}
        return super().get_form(request, obj, **kwargs)

class SubControlInline(admin.TabularInline):
    model = SubControl
    fields = ('sort_order', 'title',)
    extra = 0

class ControlAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": (
        "title",)}
    inlines=(SubControlInline,)


class QuestionInline(admin.TabularInline):
    model = Question
    fields = ('sort_order', 'question_text')
    extra = 0

class SubControlAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": (
        "title",)}
    inlines = (QuestionInline,)


admin.site.register(Answer)
admin.site.register(Question)

admin.site.register(Control, ControlAdmin)
admin.site.register(SubControl, SubControlAdmin)

admin.site.register(PathwayGroup, PathwayGroupAdmin)
admin.site.register(Pathway, PathwayAdmin)

admin.site.register(Organisation)
admin.site.register(OrganisationRegion)
admin.site.register(OrganisationType)
