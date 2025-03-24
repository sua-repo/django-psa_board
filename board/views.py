from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from board.forms import AnswerForm
from board.models import Question

# Create your views here.

# dev_3
def question_list(request) : 
    question_list = Question.objects.order_by("-create_date")

    context = {"question_list" : question_list}

    return render(request, "board/question_list.html", context)


# dev_3
def question_detail(request, question_id) : 
    question = get_object_or_404(Question, pk=question_id)

    if request.method == "POST" :
        form = AnswerForm(request.POST)
        if form.is_valid() : 
            answer = form.save(commit=False)
            answer.question = question
            answer.create_date = timezone.now()
            answer.save()
            return redirect("board:question_detail", question_id=question.id)
    
    else :
        form = AnswerForm()

    context = {"question" : question, "form" : form}

    return render(request, "board/question_detail.html", context)