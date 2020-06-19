from django import forms


class RequestNewMeeting(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=50)
    last_name = forms.CharField(label='Last Name', max_length=50)
    company = forms.CharField(label='Company', max_length=100)
    designation = forms.CharField(label='Designation', max_length=200)
    email = forms.EmailField(label='Official EMail', max_length=100)
    contact_no = forms.IntegerField(max_value=9999999999, label="Contact Number")
    subject = forms.CharField(label='Purpose/Subject', max_length=500)
    date_time1 = forms.DateTimeField(label="Proposed Date & Time - Option 1")
    duration1 = forms.IntegerField(label="Proposed Duration(minutes) - Option 1")
    date_time2 = forms.DateTimeField(label="Proposed Date & Time - Option 2", required=False)
    duration2 = forms.IntegerField(label="Proposed Duration(minutes) - Option 2", required=False)
    date_time3 = forms.DateTimeField(label="Proposed Date & Time - Option 3", required=False)
    duration3 = forms.IntegerField(label="Proposed Duration(minutes) - Option 3", required=False)
    # requested_official = forms.ForeignKey('Employee', on_delete=forms.SET_NULL, label="Official", null=True)
