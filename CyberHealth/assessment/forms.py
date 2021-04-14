from django.forms import ModelForm
from django import forms

from assessment.models import Question, Answer


class AnswerForm(ModelForm):

    def __init__(self, *args, **kwargs):
        question = kwargs.pop('question')
        choices = kwargs.pop('choices')
        radio_choices = list(zip(choices,choices))
        super(AnswerForm, self).__init__(*args, **kwargs)
        self.fields['choice'] = forms.ChoiceField(
             label=question, choices=radio_choices, widget=forms.RadioSelect)

    class Meta:
        model = Answer
        fields = ['choice']


# class QuestionForm(forms.Form):

#     def __init__(self, *args, **kwargs):
#         question = kwargs.pop('question')
#         choices = kwargs.pop('choices')
#         radio_choices = list(zip(choices,choices))
#         super(QuestionForm, self).__init__(*args, **kwargs)
#         self.fields['question'] = forms.ChoiceField(
#             label=question, initial='yes', choices=radio_choices, widget=forms.RadioSelect)
