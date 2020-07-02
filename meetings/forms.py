from django import forms
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
    date_time2 = forms.DateTimeField(label="Option 2 : Date & Time", required=False)
    duration2 = forms.IntegerField(label="Duration", widget=forms.NumberInput(attrs={'placeholder': 'Minutes'}), required=False)
    date_time3 = forms.DateTimeField(label="Option 3 : Date & Time", required=False)
    duration3 = forms.IntegerField(label="Duration", widget=forms.NumberInput(attrs={'placeholder': 'Minutes'}), required=False)
    otp = forms.CharField(label="OTP", max_length=6, widget=forms.TextInput(attrs={'placeholder': 'Enter OTP', 'size': '6', 'class': 'ml-2'}))


class OTPCaptchaVerification(forms.Form):
    captcha = CaptchaField()
