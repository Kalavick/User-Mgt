
from django import forms
from .models import CustomUser

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['email', 'full_name', 'mobile_number', 'password']

#We define the password and confirm_password fields as CharFields with a widget of PasswordInput to ensure they are masked on the form.
#We specify the model as CustomUser and include the fields email, full_name, mobile_number, and password.
#We add a clean method to validate that the password and confirm password fields match.


    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match")

#We override the save method to hash the password before saving the user object.
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

