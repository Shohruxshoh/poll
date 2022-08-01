from django.forms import ModelForm

from .models import Poll

class CreatePollForm(ModelForm):
    class Meta:
        model = Poll
        fields = ['email', 'question', 'option_one', 'option_two', 'option_three']