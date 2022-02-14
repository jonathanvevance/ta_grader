from django import forms

from .models import Question

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'

        widgets = {
            'assignment': forms.Select(attrs = {"class": 'form-control'}),
            'title': forms.TextInput(attrs = {
                    "class": 'form-control',
                    'placeholder': 'Enter a title for the question...'
                }),
            'tag_line': forms.TextInput(attrs = {
                     "class": 'form-control',
                     'placeholder': 'Enter a brief one-liner about the question...'
                    }),
            'description': forms.Textarea(attrs = {
                    "class": 'form-control',
                    'placeholder': 'Describe the question in detail. Include images, tables, etc for clarity...'
                }),
        }
