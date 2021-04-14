from django import forms
from assessment.models import Question


class QuestionForm(forms.Form):

    def __init__(self, *args, **kwargs):
        question = kwargs.pop('question')
        choices = kwargs.pop('choices')
        radio_choices = list(zip(choices,choices))
        super(QuestionForm, self).__init__(*args, **kwargs)
        self.fields['question'] = forms.ChoiceField(
            label=question, choices=radio_choices, widget=forms.RadioSelect)
