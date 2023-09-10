from django.http import JsonResponse
from django.utils import timezone
import pytz
import os

def get_info(request):
    """A function to get requests"""
    # Getting the query parameters
    slack_name = request.GET.get('Oluwasegun Babalola')
    slack_track = request.GET.get('backend')

    # Getting the current day of the week
    current_day = timezone.now().astimezone(pytz.timezone('UTC+2')).strftime('%A')

    # Getting current UTC time with validation of +/-2
    current_utc_time = timezone.now()
    valid_time_range = (timezone.now().astimezone(pytz.timezone('UTC-2')),timezone.now().astimezone(pytz.timezone('UTC+2')))
    time_validity = valid_time_range[0] <= current_utc_time <= valid_time_range[1]

    # Getting GitHub URL of the file being run
    github_file_url = 'https://github.com/Officialbabs/learning_with_HNG/blob/main/myproject/myapp/views.py'  

    # Getting GitHub URL of the full source code
    github_source_url = 'https://github.com/Officialbabs/learning_with_HNG'

    # The response JSON
    response_data = {
        'slack_name': slack_name,
        'current_day': current_day,
        'current_utc_time': current_utc_time.strftime('%Y-%m-%d %H:%M:%S %Z'),
        'track': slack_track,
        'github_file_url': github_file_url,
        'github_source_url': github_source_url,
        'status_code': 'Success' if time_validity else 'Error - Time out of range'
    }

    return JsonResponse(response_data)
