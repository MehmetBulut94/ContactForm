from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={"placeholder": "İsim"}),
            "email": forms.EmailInput(attrs={"palceholder": "Email adresiniz"}),
            "message": forms.Textarea(attrs={"palceholder": "Mesajınız"}),

        }
