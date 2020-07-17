from django.shortcuts import render
from django.core.exceptions import SuspiciousOperation
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url
from .forms import MeetingRequest, OTPCaptchaVerification, Login
from .models import Meeting
# Create your views here.


def request_new(request):
    # Identify fields rendered via plugins so that their errors can be manually rendered
    error_field_list = ["captcha", "date_time1", "date_time2", "date_time3"]
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request
        form = MeetingRequest(request.POST)
        context = {'form': form}
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            new_meeting = Meeting(subject=form.cleaned_data['subject'], company=form.cleaned_data['company'],
                                  designation=form.cleaned_data['designation'], name=form.cleaned_data['first_name'] + form.cleaned_data['last_name'],
                                  email=form.cleaned_data['email'], contact_no=form.cleaned_data['contact_no'], date_time1=form.cleaned_data['date_time1'],
                                  duration1=form.cleaned_data['duration1'], date_time2=form.cleaned_data['date_time2'], duration2=form.cleaned_data['duration2'],
                                  date_time3=form.cleaned_data['date_time2'], duration3=form.cleaned_data['duration2'],
                                  requested_official=form.cleaned_data['requested_official'], status=Meeting.SUBMITTED)
            # Manually assign a Meeting ID
            meeting_count = 1
            meeting_id = "TEST"
            employee_code = form.cleaned_data['requested_official'].designation.code
            # Loop over to auto-increment till unique ID is found
            while True:
                meeting_id = "MEET/" + new_meeting.date_time1.strftime("%d-%m-%Y") + "/" + employee_code + "/" + str(meeting_count)
                if not Meeting.objects.filter(id=meeting_id).exists():
                    break
                else:
                    meeting_count = meeting_count+1
            new_meeting.id = meeting_id
            new_meeting.save()
            # Pass Meeting object to show on status page
            context['meeting'] = new_meeting
            # redirect to a new URL:
            return render(request, 'status.html', context)
        display = "block"
    # if a GET (or any other method) we'll create a blank form
    else:
        display = "none"
        form = MeetingRequest()

    context = {'form': form, 'display': display, 'error_field_list': error_field_list}
    return render(request, 'request_new.html', context)


@ csrf_exempt
def verify_captcha(request):
    # if this is a POST & AJAX request we need to process the form data
    if request.POST and request.is_ajax():
        # create a form instance and populate it with data from the request
        form = OTPCaptchaVerification(request.POST)
        to_json_response = dict()
        if form.is_valid():
            # Captcha verification successfull
            to_json_response['status'] = 1

        else:
            to_json_response['status'] = 0
            to_json_response['form_errors'] = form.errors
        # Change captcha values once checked to avoid re-verification
        to_json_response['new_captcha_key'] = CaptchaStore.generate_key()
        to_json_response['new_captcha_image'] = captcha_image_url(to_json_response['new_captcha_key'])

        return JsonResponse(to_json_response)
    else:
        raise SuspiciousOperation


def status(request):
    # Temp Code to manually assign Meeting ID to check page, create form later
    context = {'meeting': Meeting.objects.get(id="MEET/10-07-2020/DG/4")}
    return render(request, 'status.html', context)


def login_user(request):
    form = Login()
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request
        form = Login(request.POST)
        if form.is_valid():
            # Although authentication is checked in form validation as well, we retrieve user object for login
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                # Temp code, to be redirected to home page once login is successfull
                return HttpResponse("Login Successful!")
            print("Valid Form")
    context = {'form': form}
    return render(request, 'login.html', context)


def manage(request):
    return render(request, 'manage.html')
