from django import forms

from .models import Question

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'

        widgets = {
            'assignment': forms.Select(attrs={"class": 'form-control'}),
            'title': forms.TextInput(attrs={ "class": 'form-control'}),
            'tag_line': forms.TextInput(attrs={ "class": 'form-control'}),
            'description': forms.Textarea(attrs={"class": 'form-control'}),
        }
