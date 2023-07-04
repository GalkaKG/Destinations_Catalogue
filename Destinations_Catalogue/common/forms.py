from django import forms


class SearchForm(forms.Form):
    target = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Type here to search'
            }
        )
    )
