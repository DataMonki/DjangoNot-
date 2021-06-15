from django import forms 
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('firstname','surname','email','message')

        widgets = {
            'firstname':forms.TextInput(attrs={'class':'form-control'}),
            'surname':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'message':forms.TextInput(attrs={'class':'form-control'}),
            
        }