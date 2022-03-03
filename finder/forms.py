from django import forms
from .models import business, customer

class business_form(forms.ModelForm):

    class Meta:
        model = business
        fields = ('__all__')



class customer_form(forms.ModelForm):

    class Meta:
        model = customer
        fields = ('__all__')