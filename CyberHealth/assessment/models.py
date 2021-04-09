from django.db import models

class Question(models.Model):
  question_text = models.CharField(max_length=255)

  def __str__(self):
        return self.question_text

class Choice(models.Model):
  choice_text = models.CharField(max_length=255)
  question_id = models.ForeignKey(Question, on_delete=models.CASCADE)

  def __str__(self):
        return self.choice_text

class Answer(models.Model):
  question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
  choice_id = models.ForeignKey(Choice, on_delete=models.CASCADE)