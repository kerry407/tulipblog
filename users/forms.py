from django import forms 
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from .models import Profile


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=30,  help_text='username')
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        if self.is_valid():
            email = self.cleaned_data.get('email')
            try:
                account = User.objects.exclude(pk=self.instance.pk).get(email=email)
            except User.DoesNotExist:
                return email 
            raise forms.ValidationError('Email {} is already in use'.format(email))
    
    def clean_username(self):
        if self.is_valid():
            username = self.cleaned_data.get('username')
            try:
                account = User.objects.exclude(pk=self.instance.pk).get(username=username)
            except User.DoesNotExist:
                return username 
            raise forms.ValidationError('Username {} is already in use. Try a different one.'.format(username))




class ProfileUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name','city', 'bio', 'profile_image']