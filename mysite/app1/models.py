from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth import forms

# Create your models here.
class Question(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    text = models.TextField()

class Answer(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    text = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

class FormQuestion(ModelForm):
    class Meta:
        model = Question
        fields = ['owner', 'text']