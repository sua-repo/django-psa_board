from django.db import models

# Create your models here.

# dev_2
class Question(models.Model) : 
    title = content = models.CharField(max_length=200)      # 글 제목
    content = models.TextField()                            # 글 내용
    create_date = models.DateTimeField()                    # 작성 시간


    def __str__(self) : 
        return self.title
    

class Answer(models.Model) : 
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    # create_date = models.DateField()  # 시간 안 나옴
    create_date = models.DateTimeField()

    def __str__(self) : 
        return f"Answer to : {self.question.title}"
    
    