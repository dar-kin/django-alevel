from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from django.http import Http404


SEX = [(1, "female"), (2, "male"), (3, "unknown")]
ENGLISH_LEVEL = [(1, "A1"), (2, "A2"), (3, "B1"), (4, "B2"), (5, "C1"), (6, "C2")]


class Task1Form(forms.Form):
    name = forms.CharField(max_length=100, label="name")
    sex = forms.ChoiceField(choices=SEX)
    age = forms.IntegerField(min_value=18, max_value=100)
    english_level = forms.ChoiceField(choices=ENGLISH_LEVEL)

    def clean(self):
        cleaned_data = super().clean()
        sex = cleaned_data.get("sex")
        age = cleaned_data.get("age")
        english_level = cleaned_data.get("english_level")
        condition1 = all([int(sex) == 1, age > 22, int(english_level) > 3])
        condition2 = all([int(sex) == 2, age >= 20, int(english_level) > 3])
        print(condition1, condition2)
        if not condition1 and not condition2:
            raise ValidationError("Message")


class Task2LoginForm(forms.Form):
    username = forms.CharField(max_length=100, min_length=5, label="username")
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        if username and password:
            self.user = authenticate(username=username, password=password)
            if not self.user:
                raise ValidationError("Incorrect user or password")


class Task3RegistrationForm(forms.Form):
    username = forms.CharField(max_length=100, min_length=5, label="username")
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")
        if User.objects.filter(username=username).exists():
            self.add_error("username", "Username already exists")
        if password != password2:
            self.add_error("password", "New passwords don't match")


class Task4PasswordChangeForm(forms.Form):
    current_password = forms.CharField(widget=forms.PasswordInput)
    current_password2 = forms.CharField(widget=forms.PasswordInput)
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        current_password = cleaned_data.get("current_password")
        current_password2 = cleaned_data.get("current_password2")
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")
        if current_password != current_password2:
            self.add_error("current_password2", "Old passwords don't match")
        if password != password2:
            self.add_error("password2", "New passwords don't match")


class Task56CommentSearchForm(forms.Form):
    text = forms.CharField(max_length=100, required=False)
    is_user = forms.BooleanField(required=False)



