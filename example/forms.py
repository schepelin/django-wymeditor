from django import forms
from wymeditor.widgets import WYMEditor


class ExampleForm(forms.Form):
    text = forms.CharField(label="", widget=WYMEditor())
