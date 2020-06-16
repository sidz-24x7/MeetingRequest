from django.shortcuts import render
from .forms import RequestNewMeeting
# Create your views here.


def request_new(request):
    form = RequestNewMeeting()
    return render(request, 'request_new.html', {'form': form})


def submitted(request):
    return render(request, 'submitted_request.html')
