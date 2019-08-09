from django.db import models
import datetime
# Create your models here.
class Question(models.Model):
    question_text =models.CharField(max_length=200)
    pub_date = models.DateTimeField('data published')

class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Student(models.Model):
    name = models.CharField(max_length=30)
    add_date = models.DateTimeField('date')
    is_delete=models.BooleanField(default=False)