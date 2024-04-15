from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
class SignUpForm(UserCreationForm):
    email = forms.EmailField(label='Enter your email', required=True, widget=forms.EmailInput( ))
    dateofbirth = forms.DateField(label='Enter your date of birth', widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    city = forms.ChoiceField(label='Please choose your city', choices=[('Lahore','Lahore'),('Islamabad','Islamabad'),('karachi','karachi')], required=False, widget=forms.Select( ))
    phone_number = forms.CharField(label='Please enter your phone number', required=True, widget=forms.NumberInput( ))

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2', 'dateofbirth', 'city', 'phone_number']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already in use.")
        return email

class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.error_messages = {
            **self.error_messages,
            'invalid_login': 'Please enter a correct username and password. Note that both fields may be case-sensitive.',
        }