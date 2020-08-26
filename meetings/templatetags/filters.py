from django import template

register = template.Library()


@register.filter(name='get_meeting_count')
def get_meeting_count(meetings, status):
    count = 0
    if meetings.model.__name__ == 'Meeting':
        if status != 'All':
            for meeting in meetings:
                if meeting.get_status_display() == status:
                    count = count + 1
        else:
            count = meetings.count()
    return count
