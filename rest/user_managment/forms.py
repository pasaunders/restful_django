from django import forms

class new(forms.Form):
    name = forms.CharField(label='Name', max_length=60)
    email = forms.EmailField(label='email', max_length=60)


class edit(forms.Form):
    name = forms.CharField(label='Name', max_length=60)
    email = forms.EmailField(label='email', max_length=60)
