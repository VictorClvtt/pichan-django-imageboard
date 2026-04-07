from django import forms
from . import models


class ThreadForm(forms.ModelForm):
    class Meta:
        model = models.Thread
        fields = ["title", "content", "image"]

        widgets = {
            "title": forms.TextInput(attrs={
                "placeholder": "Title (optional)",
                "class": "form-control"
            }),
            "content": forms.Textarea(attrs={
                "placeholder": "Thread content...",
                "class": "form-control",
                "rows": 5
            }),
            "image": forms.ClearableFileInput(attrs={
                "class": "form-control"
            }),
        }

        labels = {
            "title": "",
            "content": ""
        }