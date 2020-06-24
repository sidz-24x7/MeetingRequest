from django.shortcuts import render
from .forms import MeetingRequest
# Create your views here.


def request_new(request):
    form = MeetingRequest()
    return render(request, 'request_new.html', {'form': form})


def submitted(request):
    return render(request, 'submitted_request.html')
