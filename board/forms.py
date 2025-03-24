from django import forms
from board.models import Answer, Question


class QuestionForm(forms.ModelForm) : 
    class Meta : 
        model = Question
        
        # create_date는 현재 시간을 자동으로 넣을 거라 폼에서 입력받지 않아도 됨
        fields = ['title', 'content']

    
    # 만약 추가 검증이 필요하다면 clean 메서드 오버라이드 가능
    def clean(self) : 
        cleaned_data = super().clean()

        return cleaned_data
    

class AnswerForm(forms.ModelForm) : 
    class Meta : 
        model = Answer

        fields = ['content']

    
    def clean(self) : 
        cleaned_data = super().clean()

        return cleaned_data