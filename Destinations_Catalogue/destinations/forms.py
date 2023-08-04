from django import forms

from Destinations_Catalogue.destinations.models import Destination


class DestinationCreateForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = ['name', 'location', 'image', 'description']
        widgets = {
            'name': forms.TextInput(
               attrs={'placeholder': 'City, town, resort, landmark...'}
            ),
            'location': forms.TextInput(
                attrs={'placeholder': 'Country'}
            ),
            'description': forms.Textarea(
             attrs={'rows': 3, 'placeholder': 'Add comment...'}
            )
        }


class DestinationEditForm(DestinationCreateForm):
    ...
