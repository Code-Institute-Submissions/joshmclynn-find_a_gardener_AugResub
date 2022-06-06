from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, CustomUser
from .forms import CustomSignupForm
from django.contrib.auth import get_user_model


# customising Django user model to accomadate new fields
class CustomUserAdmin(UserAdmin):
    add_form = CustomSignupForm
    model = CustomUser

    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        (('Personal info'), {'fields': ('user_type', 'needs', 'location')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                      'groups', 'user_permissions')}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2',
                       'user_type', 'needs', 'location'),
        }),
    )
    list_display = ('username', 'user_type', 'needs', 'location', 'is_staff')
    search_fields = ('username', 'user_type', 'needs', 'location')
    ordering = ('username')

admin.site.register(get_user_model(), CustomUserAdmin)
