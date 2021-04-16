from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from assessment.models import Question, Answer, Choice
from .forms import AnswerForm
import logging


logger = logging.getLogger(__name__)


def index(request):

    return render(request, 'assessment/index.html')


def question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    form = AnswerForm(question=question)

    if request.method == 'POST':
        # Retrieve choice from submitted form
        try:
            selected_choice = Choice.objects.get(pk=request.POST['choice'])
            logger.info("Retrieved object from form")
        except:
            logger.warn("Can't retrieve choice object from form")

        # Create a new answer using retrieved question and choice
        try:
            new_answer = Answer(question=question, choice=selected_choice)
            logger.info("Created new answer")
            new_answer.save()
            logger.info("Saved answer to database")
        except:
            logger.warn("Can't create new answer instance")

        
        return redirect('/assessment/')

    context = {
        'form': form,
    }

    return render(request, 'assessment/question.html', context)
