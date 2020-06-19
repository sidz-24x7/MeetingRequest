from django.forms import ModelForm
from .models import Meetings


class RequestNewMeeting(ModelForm):
    class Meta:
        model = Meetings
        fields = ['subject', 'company', 'name', 'email',
                  'contact_no', 'requested_official']
