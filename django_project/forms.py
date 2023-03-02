import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from django.forms import ModelForm
from django_project.models import Question

class CreatePollForm(ModelForm):
    class Meta:
        model = Question
        fields = ['question', 'option_one', 'option_two', 'option_three']
