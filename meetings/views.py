import json
# from datetime import datetime
from django.shortcuts import render
from django.core.exceptions import SuspiciousOperation
from django.http import HttpResponse  # , HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url
from .forms import MeetingRequest, OTPCaptchaVerification
from .models import Meetings
# Create your views here.


def request_new(request):
    error_field_list = ["captcha", "date_time1", "date_time2", "date_time3"]
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MeetingRequest(request.POST)
        context = {'form': form}
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            new_meeting = Meetings(subject=form.cleaned_data['subject'], company=form.cleaned_data['company'],
                                   designation=form.cleaned_data['designation'], name=form.cleaned_data['first_name'] + form.cleaned_data['last_name'],
                                   email=form.cleaned_data['email'], contact_no=form.cleaned_data['contact_no'], date_time1=form.cleaned_data['date_time1'],
                                   duration1=form.cleaned_data['duration1'], date_time2=form.cleaned_data['date_time2'], duration2=form.cleaned_data['duration2'],
                                   date_time3=form.cleaned_data['date_time2'], duration3=form.cleaned_data['duration2'],
                                   requested_official=form.cleaned_data['requested_official'])
            meeting_count = 1
            meeting_id = "TEST"
            employee_code = form.cleaned_data['requested_official'].designation.code
            while True:
                meeting_id = "MEET/" + new_meeting.date_time1.strftime("%d-%m-%Y") + "/" + employee_code + "/" + str(meeting_count)
                if not Meetings.objects.filter(id=meeting_id).exists():
                    break
                else:
                    meeting_count = meeting_count+1
            new_meeting.id = meeting_id
            new_meeting.save()
            context['meeting_id'] = meeting_id
            context['employee_name'] = form.cleaned_data['requested_official'].__str__
            context['status'] = "Submitted"
            # redirect to a new URL:
            return render(request, 'status.html', context)
            # return HttpResponseRedirect('/status/')
        display = "block"
    # if a GET (or any other method) we'll create a blank form
    else:
        display = "none"
        form = MeetingRequest()

    context = {'form': form, 'display': display, 'error_field_list': error_field_list}
    return render(request, 'request_new.html', context)


@ csrf_exempt
def verify_captcha(request):
    if request.POST and request.is_ajax():
        form = OTPCaptchaVerification(request.POST)
        to_json_response = dict()
        if form.is_valid():
            to_json_response['status'] = 1

        else:
            to_json_response['status'] = 0
            to_json_response['form_errors'] = form.errors

        to_json_response['new_captcha_key'] = CaptchaStore.generate_key()
        to_json_response['new_captcha_image'] = captcha_image_url(to_json_response['new_captcha_key'])

        return HttpResponse(json.dumps(to_json_response), content_type='application/json')
    else:
        raise SuspiciousOperation


def status(request):
    # Temp Code
    context = {'meeting_id': "MEET/10-07-2020/DG/4", 'employee_name': "Shri S.C.L. DAS, Director General, DGH",
               'status': "Pending Approval"}
    return render(request, 'status.html', context)


def login(request):
    return render(request, 'login.html')
