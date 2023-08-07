from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator

from home.models import Worker, Task


class WorkerCreationForm(UserCreationForm):
    username = forms.CharField(
        max_length=83,
        required=True
    )

    first_name = forms.CharField(
        max_length=83,
        required=True
    )

    class Meta(UserCreationForm.Meta):
        model = Worker
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "position",
        )


class WorkerUpdateForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "position"
        ]


class TaskForm(forms.ModelForm):
    assignees = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )
    deadline = forms.DateTimeField(
        input_formats=["%Y-%m-%d %H:%M"],
        widget=forms.TextInput(
            attrs={'placeholder': '2000-01-01 16:00'}
        ),
        required=True
    )

    class Meta:
        model = Task
        fields = "__all__"
