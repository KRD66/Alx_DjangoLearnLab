from django import forms
from .models import Book  # Assuming you have a Book model

class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book  # Use your existing model
        fields = ['title', 'author']  # Adjust fields based on your Book model

    # Additional customization if needed
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 3:
            raise forms.ValidationError("Title must be at least 3 characters long.")
        return title