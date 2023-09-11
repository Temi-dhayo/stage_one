from django.http import HttpRequest, JsonResponse
from datetime import datetime,timezone

def index(request:HttpRequest)->JsonResponse:
    slack_name:str = request.GET.get('slack_name','')
    track:str = request.GET.get('track','')
    utc_time:str = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    current_day:str = datetime.now().strftime('%A')
    github_file_url:str = 'https://github.com/Temi-dhayo/stage_one/blob/master/core/view.py'
    github_repo_url:str = 'https://github.com/Temi-dhayo/stage_one'

    response = {
        'slack_name': slack_name,
        'current_day': current_day,
        'utc_time': utc_time,
        'track': track,
        'github_file_url': github_file_url,
        'github_repo_url': github_repo_url,
        'status_code': 200,
    }
    return JsonResponse(response)

