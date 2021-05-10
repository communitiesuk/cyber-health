from django.forms import ModelForm
from django import forms

from assessment.models import Question, Answer, Choice


class AnswerForm(ModelForm):

    def __init__(self, *args, **kwargs):
        self.question = kwargs.pop('question')
        super(AnswerForm, self).__init__(*args, **kwargs)
        self.fields['choice'] = forms.ModelChoiceField(
            label=self.question, queryset=self.question.choice_set.all(), widget=forms.RadioSelect)

    class Meta:
        model = Answer
        fields = ['choice']



