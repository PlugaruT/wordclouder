from django import forms

from .models import TextComment


class TextCommentForm(forms.ModelForm):
    class Meta:
        model = TextComment
        fields = ["content"]
