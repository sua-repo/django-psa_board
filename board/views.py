from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from .forms import AnswerForm, QuestionForm
from .models import Question
from django.core.paginator import Paginator
from django.db.models import Count

# Create your views here.

# dev_3
def question_list(request) : 
    """질문 목록 (페이징 적용)"""

    # ?page=1
    page = request.GET.get("page", "1")  # URL에서 ?page=1 값을 가져옴

    # question_list = Question.objects.order_by("-create_date")
    question_list = Question.objects.annotate(num_answers=Count('answer')).order_by('-create_date')     # annotate()를 사용하여 각 질문의 답변 수 추가

    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)     # 해당 페이지에 해당하는 데이터 가져옴
    
    # 페이지네이션 범위 계산 (5개씩 끊어서)
    current_page = page_obj.number  # 현재 페이지 번호
    total_pages = paginator.num_pages  # 전체 페이지 개수
    page_range = 5  # 한 번에 보여줄 페이지 개수 (5개씩)

    start_page = ((current_page - 1) // page_range) * page_range + 1
    end_page = start_page + page_range - 1
    if end_page > total_pages:
        end_page = total_pages

    context = {
        "question_list": page_obj,
        "page_range": range(start_page, end_page + 1),  # 5개씩 끊어진 페이지 목록
        "has_previous": page_obj.has_previous(),
        "has_next": page_obj.has_next(),
        "previous_page_number": page_obj.previous_page_number() if page_obj.has_previous() else None,
        "next_page_number": page_obj.next_page_number() if page_obj.has_next() else None,
        "start_page": start_page,
        "end_page": end_page,
        "total_pages": total_pages,
    }
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


