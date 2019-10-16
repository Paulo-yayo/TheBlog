from django import forms

class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=30, label='Voornaam')
    last_name = forms.CharField(max_length=30, label='Achternaam')
    organisation = forms.CharField(max_length=20, label='organisation')

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        # Replace 'profile' below with the related_name on the OneToOneField linking back to the User model
        up = user.profile
        up.organisation = self.cleaned_data['organisation']
        user.save()
        up.save()