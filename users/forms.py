from django import forms
from django.contrib.auth.models import User
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm


class UserSignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['is_patient','is_doctor','profile_picture', 'address_line1', 'city', 'state', 'pincode']

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match")
        return confirm_password

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name']
        )
        custom_user = super(UserSignupForm, self).save(commit=False)
        custom_user.user = user
        if commit:
            custom_user.save()
        return custom_user

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'] = forms.CharField(max_length=150, required=True)
        self.fields['email'] = forms.EmailField(required=True)
        self.fields['first_name'] = forms.CharField(max_length=30, required=True)
        self.fields['last_name'] = forms.CharField(max_length=150, required=True)

class UserSigninForm(AuthenticationForm):
    username = forms.CharField(max_length=150, label='Username')
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
