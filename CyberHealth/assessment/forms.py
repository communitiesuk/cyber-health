from django.forms import ModelForm
from django import forms

from assessment.models import Answer


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

