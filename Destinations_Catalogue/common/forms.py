from django import forms
from .models import Comment


class SearchForm(forms.Form):
    target = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Type here to search'
            }
        )
    )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
