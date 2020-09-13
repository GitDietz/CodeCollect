from django import forms
from django.core.exceptions import ValidationError

class ContactForm(forms.Form):
    full_name = forms.CharField(label= "Your name and surname", required=True, widget=forms.TextInput
                           (attrs={'placeholder': 'Your full name'}))
    email = forms.EmailField(required=True, widget= forms.EmailInput
                           (attrs={'placeholder': 'Enter your email'}))
    subject = forms.CharField(label="Subject", required=True, widget=forms.TextInput
                           (attrs={'placeholder': 'Subject'}))
    content = forms.CharField(widget=forms.Textarea(attrs={"rows": 10, "cols": 60,
                                                           'placeholder': 'Please detail your enquiry'}), required=True)

    class Meta:
        fields = ['full_name', 'email', 'subject', 'content']
