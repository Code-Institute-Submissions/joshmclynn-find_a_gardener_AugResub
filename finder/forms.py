from django import forms
from .models import business, customer

class business_form(forms.ModelForm):

    class Meta:
        model = business
        fields = ('__all__')
        labels = {
            'company_name':'Company Name',
            'f_name':'First Name',
            'l_name':'Last Name',
            'email':'Email',
            'image':'Company Logo',
            'landscaping':'Landscaping',
            'maintenance':'Garden Maintenance',
            'tree':'Tree Surgery',
            'design':'Garden Design',
            'location':'City',
            'description':'Company Description'
        }



class customer_form(forms.ModelForm):

    class Meta:
        model = customer
        fields = ('__all__')
        labels={
            'f_name':'First Name',
            'l_name':'Last Name',
            'email':'Email',
            'image':'Profile Image',
            'landscaping':'Landscaping',
            'maintenance':'Garden Maintenance',
            'tree':'Tree Surgery',
            'design':'Garden Design',
            'location':'City'
        }