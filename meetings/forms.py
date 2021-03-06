from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from captcha.fields import CaptchaField
from .models import Employee


class MeetingRequest(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=50, widget=forms.TextInput(attrs={'class': 'personalDetails'}))
    last_name = forms.CharField(label='Last Name', max_length=50, widget=forms.TextInput(attrs={'class': 'personalDetails'}))
    company = forms.CharField(label='Company', max_length=100, widget=forms.TextInput(attrs={'class': 'personalDetails'}))
    designation = forms.CharField(label='Designation', max_length=200, widget=forms.TextInput(attrs={'class': 'personalDetails'}))
    email = forms.EmailField(label='E-Mail', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter Official E-Mail', 'class': 'personalDetails'}))
    contact_no = forms.IntegerField(max_value=9999999999, label="Contact Number", widget=forms.NumberInput(attrs={'placeholder': 'Enter mobile number', 'class': 'personalDetails', 'maxlength': '10'}))
    captcha = CaptchaField()
    subject = forms.CharField(label='Purpose/Subject', max_length=500)
    requested_official = forms.ModelChoiceField(queryset=Employee.objects.all().order_by('order_number'), empty_label='Select Official', label="Requested Official")
    date_time1 = forms.DateTimeField(label="Option 1 : Date & Time", input_formats=['%d-%m-%Y %H:%M'])
    duration1 = forms.IntegerField(label="Duration", widget=forms.NumberInput(attrs={'placeholder': 'Minutes'}))
    date_time2 = forms.DateTimeField(label="Option 2 : Date & Time", required=False, input_formats=['%d-%m-%Y %H:%M'])
    duration2 = forms.IntegerField(label="Duration", widget=forms.NumberInput(attrs={'placeholder': 'Minutes'}), required=False)
    date_time3 = forms.DateTimeField(label="Option 3 : Date & Time", required=False, input_formats=['%d-%m-%Y %H:%M'])
    duration3 = forms.IntegerField(label="Duration", widget=forms.NumberInput(attrs={'placeholder': 'Minutes'}), required=False)
    otp = forms.CharField(label="OTP", max_length=6, widget=forms.TextInput(attrs={'placeholder': 'Enter OTP', 'size': '6', 'class': 'ml-2'}))


class OTPCaptchaVerification(forms.Form):
    captcha = CaptchaField()


class Login(forms.Form):
    username = forms.CharField(label='Username', max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Enter Username'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}))
    captcha = CaptchaField()

    def clean(self):
        cleaned_data = super().clean()
        _username = cleaned_data.get("username")
        _password = cleaned_data.get("password")

        try:
            _user_object = User.objects.get(username=_username)
            _user = authenticate(username=_username, password=_password)
            if _user is None:
                self.add_error("password", "Invalid Password")
        except User.DoesNotExist:
            self.add_error("username", "Invalid Username")
