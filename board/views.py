from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from .forms import AnswerForm, QuestionForm
from .models import Question

# Create your views here.

# dev_3
def question_list(request) : 
    question_list = Question.objects.order_by("-create_date")

    context = {"question_list" : question_list}

    return render(request, "board/question_list.html", context)


# dev_3
def question_detail(request, question_id):
    """질문 상세 페이지"""
    question = get_object_or_404(Question, pk=question_id)
    
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect("board:question_detail", question_id=question.id)
    else:
        form = AnswerForm()

    context = {
        "question": question,
        "form": form,
    }
    return render(request, 'board/question_detail.html', context)


# dev_4
def question_create(request) : 
    """질문 등록"""
    if request.method == "POST" : 
        form = QuestionForm(request.POST)

        if form.is_valid() : 
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()

            return redirect("board:question_list")
    else : 
        form = QuestionForm()
    
    context = {"form" : form}
    return render(request, "board/question_form.html", context)
        


# dev_5
def answer_create(request, question_id):
    """답변 등록"""
    question = get_object_or_404(Question, pk=question_id)

    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.create_date = timezone.now()
            answer.save()
            return redirect('board:question_detail', question_id=question.id)
    else:
        form = AnswerForm()

    context = {'question': question, 'form': form}
    return render(request, 'board/question_detail.html', context)