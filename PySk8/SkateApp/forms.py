from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(label='password', max_length=64, widget=forms.PasswordInput)
    re_password = forms.CharField(label='re_password', max_length=64, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 're_password']


class LoggingInForm(forms.Form):
    login = forms.CharField(max_length=64)
    password = forms.CharField(max_length=64, widget=forms.PasswordInput)


class EditProfileForm(forms.Form):
    avatar = forms.ImageField()


class AddPostForm(forms.Form):
    RATING = (
        (1, "1.0"),
        (2, "2.0"),
        (3, "3.0"),
        (4, "4.0"),
        (5, "5.0"),
    )
    title = forms.CharField(max_length=64)
    rating = forms.ChoiceField(choices=RATING)
    description = forms.CharField(max_length=400)
    image = forms.ImageField()


class EditPostForm(forms.Form):
    RATING = (
        (1, "1.0"),
        (2, "2.0"),
        (3, "3.0"),
        (4, "4.0"),
        (5, "5.0"),
    )
    title = forms.CharField(max_length=64)
    rating = forms.ChoiceField(choices=RATING)
    description = forms.CharField(max_length=400)
    image = forms.ImageField()
