from django.contrib import admin
from assessment.models import *


class PathwayGroupAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class PathwayAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": (
        "short_name",)}
    filter_horizontal = ('controls',)


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

# class SubControlForm(forms.ModelForm):
#     class Meta:
#         model = SubControl
#         fields = '__all__'

#     questions = forms.ModelMultipleChoiceField(
#                     queryset=Question.objects.filter(sub_control__isnull=True),
#                     widget=forms.CheckboxSelectMultiple
#                 )

#     def __init__(self, *args, **kwargs):
#         super(SubControlForm, self).__init__(*args, **kwargs)
#         if self.instance:
#             if self.instance.in_sub_control:
#                 self.fields['questions'].initial = self.instance.in_sub_control.all()
#             else:
#                 self.fields['questions'].initial = []

#     def save(self, *args, **kwargs):
#         instance = super(SubControlForm, self).save(commit=False)
#         self.fields['questions'].initial.update(sub_control=None)
#         self.cleaned_data['questions'].update(sub_control=instance)
#         return instance

class SubControlAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": (
        "title",)}
    # form = SubControlForm
    inlines = (QuestionInline,)


admin.site.register(Answer)
admin.site.register(Question)
admin.site.register(Choice)

admin.site.register(Control, ControlAdmin)
admin.site.register(SubControl, SubControlAdmin)

admin.site.register(PathwayGroup, PathwayGroupAdmin)
admin.site.register(Pathway, PathwayAdmin)

admin.site.register(Organisation)
admin.site.register(OrganisationRegion)
admin.site.register(OrganisationType)
