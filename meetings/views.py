import json
import random
from datetime import date, datetime
from django.shortcuts import render
from django.core.exceptions import SuspiciousOperation
from django.http import HttpResponse  # , HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url
from .forms import MeetingRequest, OTPCaptchaVerification
from .models import Meetings, Employee
# Create your views here.


def request_new(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MeetingRequest(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            id = "MEET/"
            meeting = Meetings(subject=form.cleaned_data['subject'], company=form.cleaned_data['company'],
                               designation=form.cleaned_data['designation'], name=form.cleaned_data['first_name'] + form.cleaned_data['last_name'],
                               email=form.cleaned_data['email'], contact_no=form.cleaned_data['contact_no'], date_time1=form.cleaned_data['date_time1'],
                               duration1=form.cleaned_data['duration1'], date_time2=form.cleaned_data['date_time2'], duration2=form.cleaned_data['duration2'],
                               date_time3=form.cleaned_data['date_time2'], duration3=form.cleaned_data['duration2'],
                               requested_official=form.cleaned_data['requested_official'])
            id = "MEET/"+meeting.date_time1.strftime("%d-%m-%Y")+random.randint(1, 30)
            meeting.id = id
            meeting.save()
            # ...
            # redirect to a new URL:
            return HttpResponse("Success")
            # return HttpResponseRedirect('/status/')
        display = "block"
    # if a GET (or any other method) we'll create a blank form
    else:
        display = "none"
        form = MeetingRequest()

    return render(request, 'request_new.html', {'form': form, 'display': display})


@csrf_exempt
def verify_captcha(request):
    if request.POST and request.is_ajax():
        form = OTPCaptchaVerification(request.POST)
        to_json_response = dict()
        if form.is_valid():
            to_json_response['status'] = 1

            to_json_response['new_captcha_key'] = CaptchaStore.generate_key()
            to_json_response['new_captcha_image'] = captcha_image_url(to_json_response['new_captcha_key'])

        else:
            to_json_response['status'] = 0
            to_json_response['form_errors'] = form.errors

            to_json_response['new_captcha_key'] = CaptchaStore.generate_key()
            to_json_response['new_captcha_image'] = captcha_image_url(to_json_response['new_captcha_key'])

        return HttpResponse(json.dumps(to_json_response), content_type='application/json')
    else:
        raise SuspiciousOperation


def submitted(request):
    return render(request, 'submitted_request.html')
