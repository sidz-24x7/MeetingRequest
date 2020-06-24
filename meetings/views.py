from django.shortcuts import render
from .forms import MeetingRequest, OTPCaptchaVerification
# Create your views here.


def request_new(request):
    form = MeetingRequest()
    captcha_form = OTPCaptchaVerification()
    return render(request, 'request_new.html', {'form': form, 'captcha_form': captcha_form})


def submitted(request):
    return render(request, 'submitted_request.html')
