from django.shortcuts import render
from django.http import HttpResponse

from foos_web.forms import TeamForm
from foos_web.models import Team

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
