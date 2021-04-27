from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from assessment.models import Question, Answer, Choice
from basicauth.decorators import basic_auth_required
from django.shortcuts import render
from .forms import AnswerForm
import logging

logger = logging.getLogger(__name__)


@basic_auth_required
def assessment_start_page(request):
    logger.info(request)
    questions = Question.objects.filter()
    logger.info(questions)
    return render(request, 'assessment/index.html', {'questions': questions})


@basic_auth_required
def question_view(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    form = AnswerForm(question=question)

    if request.method == 'POST':
        logger.info(request.POST)
        if 'choice' in request.POST:
            #  Retrieve choice from objects
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
