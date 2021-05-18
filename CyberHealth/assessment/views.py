from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from assessment.models import Question, Answer, Choice, Pathway, PathwayGroup
from django.shortcuts import render
from .forms import AnswerForm
import logging

logger = logging.getLogger(__name__)


@login_required
def assessment_overview(request):
    logger.info(request)
    pathway_groups_dict = PathwayGroup.objects.values()

    pathway_groups = []
    for group in pathway_groups_dict:
        group['pathways'] = Pathway.objects.filter(pathway_group=group['id'])
        pathway_groups.append(group)
    return render(request, 'assessment/assessment-overview.html',
                  {'pathway_groups': pathway_groups})


@login_required
def assessment_all_questions_page(request):
    logger.info(request)
    questions = Question.objects.filter()
    for question in questions:
        if question.answer_set.all().last() is None:
            question.chosen_answer = "None"
            question.answer_colour = "blue"
        else:
            question.chosen_answer = question. \
                answer_set.all().last().choice.choice_text
            if question.chosen_answer == "yes":
                question.answer_colour = "green"
            else:
                question.answer_colour = "red"

    return render(request, 'assessment/all-questions.html',
                  {'questions': questions})


@login_required
def question_view(request, pathway_slug, question_id):
    question = get_object_or_404(Question, pk=question_id)
    pathway = get_object_or_404(Pathway, slug=pathway_slug)
    form = AnswerForm(question=question)

    if request.method == 'POST':
        logger.info(request.POST)
        if 'choice' in request.POST:
            #  Retrieve choice from objects
            try:
                selected_choice = Choice.objects.get(pk=request.POST['choice'])
                logger.info("Retrieved object from form")
            except Exception as e:
                logger.warn("Can't retrieve choice object from form",
                            Exception)

            # Create a new answer using retrieved question and choice
            try:
                new_answer = Answer(question=question, choice=selected_choice)
                logger.info("Created new answer")
                new_answer.save()
                logger.info("Saved answer to database")
            except Exception as e:
                logger.warn("Can't create new answer instance", Exception)

        return redirect('/assessment/')

    context = {
        'form': form,
    }

    return render(request, 'assessment/question.html', context)


@login_required
def pathway_view(request, pathway_slug):
    pathway = get_object_or_404(Pathway, slug=pathway_slug)

    logger.info("Viewing pathway: %s", pathway_slug)

    context = {"pathway": pathway, "breadcrumbs": []}

    return render(request, 'assessment/pathway.html', context)
