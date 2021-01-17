from django import forms
from .models import Image,Profile,Comments
from django.contrib.auth.models import User


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_pic','bio','username')