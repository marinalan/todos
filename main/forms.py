from django import forms

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
        fields = ['title', 'due_date', 'description']

