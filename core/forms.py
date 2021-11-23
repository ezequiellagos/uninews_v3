from allauth.account.forms import SignupForm, LoginForm
from django import forms
from django.contrib.auth.models import Group

class CustomSignupForm(SignupForm):

    first_name = forms.CharField(max_length=30, label='Nombre', required=True, widget=forms.TextInput(attrs={'placeholder': 'Nombre'}))
    last_name = forms.CharField(max_length=30, label='Apellido', widget=forms.TextInput(attrs={'placeholder': 'Apellido'}))


    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'

        
        
    def save(self, request):
        user = super(CustomSignupForm, self).save(request)

        my_group = Group.objects.get(name='Tier 1') 
        my_group.user_set.add(user)

        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

        return user

class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)

        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['login'].widget.attrs['class'] = 'form-control'
        