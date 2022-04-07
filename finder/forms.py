from allauth.account.forms import SignupForm
from django import forms


CHOICES = [('customer','Customer'),('business','Business')]
NEEDS = [('garden-maintenance','Garden-Maintenance'),('garden-design','Garden-Design'),('landscaping','Landscaping'),('tree-surgery','Tree-Surgery')]
class newSignUpForm(SignupForm):
    
    
    are_you_a_business = forms.MultipleChoiceField(
                                                widget = forms.CheckboxSelectMultiple,
                                                choices = CHOICES
        
                                                )
    userNeeds = forms.MultipleChoiceField(
                                          widget = forms.CheckboxSelectMultiple,
                                          choices = NEEDS
                                          )
    Location = forms.CharField(max_length=30)
    




        
