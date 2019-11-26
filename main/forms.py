from datetime import date
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Todo

'''
class TodoForm(forms.Form):
    title = forms.CharField(max_length=255)
    description = forms.CharField(
        widget=forms.Textarea(attrs={"rows":5, "cols":20})
    )
    done = forms.BooleanField(required=False)
    due_date = forms.DateField()
'''

class TodoForm(forms.ModelForm):
    
    class Meta:
        model = Todo
        fields = '__all__' #['title', 'due_date', 'description', 'done']
        labels = {
            'done': 'Is this task done?' 
        }
        help_texts = {
            'due_date': 'Date when task is expected to be done.'
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        words = title.split(' ')
        if len(words) > 5:
            raise forms.ValidationError('The title should be five or less words')
        return title

    def clean_due_date(self):
        due_date = self.cleaned_data['due_date']

        if due_date < date.today():
            raise forms.ValidationError('The due date can not be in the past.')
        return due_date

class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(max_length=255, help_text='eg. name@example.com')

    class Meta:
        model = User
        fields = ('first_name','last_name','username','password1','password2','email')
