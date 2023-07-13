from django import forms
from django.forms import FileInput

from Destinations_Catalogue.destinations.models import Destination


class DestinationCreateForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = ['name', 'location', 'image', 'hotel', 'price', 'description']
        widgets = {
            'name': forms.TextInput(
               attrs={'placeholder': 'City, town, resort, landmark...'}
            ),
            'location': forms.TextInput(
                attrs={'placeholder': 'Country'}
            ),
            'hotel': forms.TextInput(
               attrs={'placeholder': 'Not required'}
            ),
            'description': forms.Textarea(
             attrs={'rows': 3, 'placeholder': 'Add comment...'}
            )
        }


class DestinationEditForm(DestinationCreateForm):
    image = forms.ImageField(widget=FileInput)
