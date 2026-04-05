from django import forms
from . import models


class ThreadForm(forms.ModelForm):
    class Meta:
        model = models.Thread
        fields = ["title", "content"]

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
        }

        labels = {
            "title": "",
            "content": ""
        }