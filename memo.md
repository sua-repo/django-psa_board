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