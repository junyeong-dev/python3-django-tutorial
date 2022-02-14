from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    # 외래키(Foreign Key)를 사용해 부모-자식 관계 설정
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # CharField는 max_length라는 필수 인자를 가짐
    choice_text = models.CharField(max_length=200)
    # default는 선택 인자
    votes = models.IntegerField(default=0)