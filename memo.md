## Django 설치하기
    pip install django

## Django 프로젝트 시작
    django-admin startproject config .

## 서버 실행 
    python manage.py runserver
    (http://127.0.0.1:8000/)

## 앱 생성하기
    python manage.py startapp board

## 앱 등록하기 (settings.py)
    config/settings.py에서 INSTALLED_APPS에 'board', 추가

##  모델을 생성하거나 변경할 경우
    python manage.py makemigrations
    python manage.py migrate
    
    => db.sqlite3 파일에 board_question / board_answer 테이블이 생김

## 확인해보고 싶으면
    python manage.py shell

    from board.models import Question, Answer
    Question.objects.all()
    Answer.objects.all()

    => 아무것도 없다면 <QuerySet []> 출력

## render()
    render 함수는 Django에서 뷰(view)가 HTML 템플릿을 렌더링할 때 사용하는 함수

    render(request, template_name, context)
    request : 요청 객체 (무조건 넣어야 함)
    template_name : 렌더링할 HTML 경로 (예: 'board/question_list.html')
    context : 템플릿에 넘겨줄 데이터 (딕셔너리 형태)
