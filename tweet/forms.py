from django import forms


class CreateTweetForm(forms.Form):
    body = forms.CharField(widget=forms.Textarea)