from django import forms

from Destinations_Catalogue.profiles.models import ProfileModel


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['first_name', 'last_name', 'age', 'image']


class EditProfileForm(ProfileBaseForm):
    ...


class DeleteProfileForm(EditProfileForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance

    def __set_disabled_fields(self):
        for field in self.fields.values():
            field.disabled = True
