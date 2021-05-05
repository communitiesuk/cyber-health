from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from assessment.models import Question, Answer, Choice, Pathway, PathwayGroup
from basicauth.decorators import basic_auth_required
from django.shortcuts import render
from .forms import AnswerForm
import logging

logger = logging.getLogger(__name__)


@basic_auth_required
def assessment_overview(request):
    logger.info(request)
    pathway_groups_dict = PathwayGroup.objects.values()

    pathway_groups = []
    for group in pathway_groups_dict:
        current_group = group
        related_pathways = Pathway.objects.filter(pathway_group=group['id'])
        current_group['pathways'] = related_pathways
        pathway_groups.append(current_group)
    return render(request, 'assessment/assessment-overview.html', {'pathway_groups': pathway_groups})


@basic_auth_required
def assessment_all_questions_page(request):
    logger.info(request)
    questions = Question.objects.filter()
    for question in questions:
        if question.answer_set.all().last() is None:
            question.chosen_answer = "None"
            question.answer_colour = "blue"
        else:
            question.chosen_answer = question.answer_set.all().last().choice.choice_text
            if question.chosen_answer == "yes":
                question.answer_colour = "green"
            else:
                question.answer_colour = "red"

    return render(request, 'assessment/all-questions.html', {'questions': questions})


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
