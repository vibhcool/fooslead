from django.shortcuts import render
from django.http import HttpResponse

from foos_web.forms import TeamForm
from foos_web.models import Team
from foos_web.leaderboard import Leaderboard

leaderboard = Leaderboard()

def team_create_page(request):
    return render(request, 'create_team.html')

def create_team(request):
    if request.method == 'POST':
        team_form = TeamForm(request.POST)
        if team_form.is_valid():
            Team(member_a=team_form.cleaned_data.get('member_a'),
                member_b=team_form.cleaned_data.get('member_b'),
                team_name=team_form.cleaned_data.get('team')
            ).save()
            return HttpResponse("Team created")
        return HttpResponse("Team")

def get_leaderboard(request):
    print(str(leaderboard.show_ranking(limit=10)))
    return HttpResponse({'ranklist': str(leaderboard.show_ranking(limit=10))})
   
'''
def add_point(request):
    match_id = request.GET.get('match-id')
    team = request.GET.get('team')
    leaderboard.matches[match_id].win_point()

def start_match(request):
    team_a = request.GET.get('team-a')
    team_b = request.GET.get('team-b')
    if match_id == -1:
        match_id = leaderboard.start_match(team_a, team_b)


 
'''
