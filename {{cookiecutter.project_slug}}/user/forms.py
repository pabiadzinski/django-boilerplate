from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms
from django.contrib.auth import authenticate


class UserSignUpForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ('email', 'name')


class UserSignInForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password')
        exclude = ()

    def clean(self):
        username = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)

        if self.is_valid() and not user:
            error_message = "Sorry, that login was invalid. Please try again."
            self.add_error("email", error_message)
            raise forms.ValidationError(error_message)

        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user


class ProfileForm(forms.ModelForm):
    name = forms.CharField(
        label="Name",
        required=True,
        max_length=50,
        widget=forms.TextInput(attrs={
            "placeholder": "Name",
            "class": "form-control",
        })
    )

    # email = forms.CharField(
    #     label="Email",
    #     required=True,
    #     max_length=50,
    #     widget=forms.EmailInput(attrs={
    #         "placeholder": "Email",
    #         "class": "form-control",
    #     })
    # )

    class Meta:
        model = User
        fields = ('name', )

