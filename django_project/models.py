import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settings")
# django.setup()

from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models


# from polls.models import Choice, Question

class Question(models.Model):
    question = models.TextField()
    option_one = models.CharField(max_length=30)
    option_two = models.CharField(max_length=30)
    option_three = models.CharField(max_length=30)
    option_one_count = models.IntegerField(default=0)
    option_two_count = models.IntegerField(default=0)
    option_three_count = models.IntegerField(default=0)

    def total(self):
        return self.option_one_count + self.option_two_count + self.option_three_count

    # class Question(models.Model):
    #    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    #    question_text = models.CharField(max_length=200)
    #    pub_date = models.DateTimeField(default=timezone.now())
    #    active = models.BooleanField(default=True)

    class Meta:
        app_label = 'django_project'


class Answer(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=django.utils.timezone.now)
    active = models.BooleanField(default=True)
    votes = models.IntegerField(default=0)

    class Meta:
        app_label = 'django_project'


#class Choice(models.Model):
#    question = models.ForeignKey(Question, on_delete=models.CASCADE)
#    choice_text = models.CharField(max_length=200)
#    votes = models.IntegerField(default=0)

#    def __str__(self):
#        return self.choice_text
