from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RigorousRegistrationForm(UserCreationForm):
    # Add a mandatory dropdown menu to let the user select their interface role
    ROLE_CHOICES = [
        ('user', 'Standard User / Customer'),
        ('owner', 'Business Owner / Vendor')
    ]
    role = forms.ChoiceField(choices=ROLE_CHOICES, required=True, label="Account Type")

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email')