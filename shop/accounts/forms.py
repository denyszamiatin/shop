from django import forms

from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    password1 = forms.CharField(
        label='Repeat password',
        widget=forms.PasswordInput()
    )

    def clean_password(self):
        if len(self.cleaned_data['password']) < 3:
            raise forms.ValidationError('Password too short')
        return self.cleaned_data['password']

    def clean(self):
        if 'password' in self.cleaned_data and\
            self.cleaned_data['password'] != self.cleaned_data['password1']:
            raise forms.ValidationError('Passwords are unequal')
        return self.cleaned_data

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class Login(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput())