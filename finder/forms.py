from allauth.account.forms import SignupForm
from django.contrib.auth import get_user_model
from .models import CustomUser




CHOICES = [('customer','Customer'),('business','Business')]
NEEDS = [('garden-maintenance','Garden-Maintenance'),('garden-design','Garden-Design'),('landscaping','Landscaping'),('tree-surgery','Tree-Surgery')]
class CustomSignupForm(SignupForm):
        model = CustomUser()
        field = ('user_type','needs','location')
   
        user_type = forms.MultipleChoiceField(
                                                widget = forms.CheckboxSelectMultiple,
                                                choices = CHOICES
        
                                                )
        needs = forms.MultipleChoiceField(
                                          widget = forms.CheckboxSelectMultiple,
                                          choices = NEEDS
                                          )
        location = forms.CharField(max_length=30)
    
    
        
        
        def signup(self, request, user):
            
            user.user_type = self.cleaned_data['Business_or_Customer']
            user.needs = self.cleaned_data['What_are_you_interested_in']
            user.location = self.cleaned_data['Location']
            user.save()
            return user


        
