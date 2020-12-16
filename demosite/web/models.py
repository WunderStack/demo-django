from django.db import models

class Question(models.Model):
    question_text = models.CharField('question', max_length=200)
    pub_date = models.DateTimeField('date published')
