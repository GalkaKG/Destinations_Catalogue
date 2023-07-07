from django import forms

from Destinations_Catalogue.destinations.models import Destination


class DestinationCreateForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = ['name', 'location', 'image', 'hotel', 'price', 'description']
        widgets = {
            'description': forms.Textarea(
             attrs={'rows': 3, 'placeholder': 'Add comment...'}
        )
        }
