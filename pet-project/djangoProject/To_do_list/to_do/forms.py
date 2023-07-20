from django import forms

from to_do.models import Tag, Task


class TaskCreationForm(forms.ModelForm):

    class Meta(forms.ModelForm):
        model = Task
        fields = ('content', "datetime", "deadline", "done", "tag")


class TagForm(forms.ModelForm):

    class Meta:
        model = Tag
        fields = "__all__"


class TaskSearchForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search tag"})
    )