from django import forms
from django.forms import ModelForm

from assessment.models import Answer, UploadEvidence


class AnswerForm(ModelForm):

    def __init__(self, *args, **kwargs):
        self.question = kwargs.pop('question')
        super(AnswerForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Answer
        fields = ['response']
        widgets = {
            'response': forms.RadioSelect
        }

class UploadEvidenceForm(ModelForm):   

    def __init__(self, *args, **kwargs):
        self.uploads = kwargs.pop('uploads')
        self.user = kwargs.pop('user')        
        super(UploadEvidenceForm, self).__init__(*args, **kwargs)

    class Meta:
        model = UploadEvidence
        fields = ('upload',)

    def save(self):
        self.instance.user = self.user
        upload = super(UploadEvidenceForm, self).save()
        return upload
