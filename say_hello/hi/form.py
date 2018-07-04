from django import forms
from .models import FaveRest
from .validation import email_valid


class RestcreateForm(forms.Form):
    name = forms.CharField(required = True)
    locat = forms.CharField(required =False)

class NewRestCreateForm(forms.ModelForm):
    class Meta :
        model =FaveRest
        fields = ["name","locat","email"]

class RestEditForm(forms.Form):
    name = forms.CharField(required = True)
    locat = forms.CharField(required =False)
    email = forms.EmailField(required =True ,  validators= [email_valid])
    