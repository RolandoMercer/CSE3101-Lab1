from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'completed']
        error_messages = {
            'title': {
                'required': 'Title cannot be empty or only spaces.',
                'max_length': 'Title cannot be longer than 150 characters.',
            },
        }

    def clean_title(self):
        title = self.cleaned_data.get('title', '')
        if not title.strip():
            raise forms.ValidationError('Title cannot be empty or only spaces.')
        return title.strip()