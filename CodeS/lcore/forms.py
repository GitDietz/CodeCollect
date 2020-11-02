from django import forms
from django.core.exceptions import ValidationError
# from bootstrap_datepicker_plus import DatePickerInput

from .models import Code, Appfeature

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


class CodeForm(forms.ModelForm):
    class Meta:
        model = Code
        fields = '__all__'


class DateInput(forms.DateInput):
    input_type = 'date'


class AppfeatureForm(forms.ModelForm):
    # last_test = forms.DateField(widget=DatePickerInput(format='%d/%m/%Y'))
    #last_test = forms.DateField(input_formats=['%d/%m/%Y'])
    #last_test = forms.DateField(widget=DateInput)
    class Meta:
        model = Appfeature
        widgets = {'last_test': DateInput}
        fields = '__all__'

