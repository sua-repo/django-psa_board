from django.urls import path
from . import views     # 현재 폴더의 views.py를 가져옴

app_name = "board"

urlpatterns = [
    path('', views.question_list, name="question_list"),    # dev_3
    path('<int:question_id>/', views.question_detail, name="question_detail"),   # dev_3
    path("question/create/", views.question_create, name="question_create"),   # dev_4
    path("answer/create/<int:question_id>/", views.answer_create, name="answer_create"),    # dev_5
]
