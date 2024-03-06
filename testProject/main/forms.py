from django import forms


class CreateNewList(forms.Form):
    title = forms.CharField(label="Title", max_length=200)
    complete = forms.BooleanField(label="Completed", required=False)


