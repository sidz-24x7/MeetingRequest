import json
from django.shortcuts import render
from django.core.exceptions import SuspiciousOperation
from django.http import HttpResponse  # , HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url
from .forms import MeetingRequest, OTPCaptchaVerification
# Create your views here.


def request_new(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MeetingRequest(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
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
