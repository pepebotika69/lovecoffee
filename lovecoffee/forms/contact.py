from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(required=True, max_length=150)
    email_address = forms.EmailField(required=True, max_length=150)
    message = forms.CharField(required=True, widget=forms.Textarea, max_length=2000)
