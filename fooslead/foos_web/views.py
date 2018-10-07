from django.shortcuts import render, redirect
from django.http import HttpResponse

import json

from foos_web.forms import TeamForm
from foos_web.models import Team
from foos_web.leaderboard import Leaderboard

leaderboard = Leaderboard()

def start_game(request):
    response = {}
    response['status'] = False
    if request.method == 'GET':
        team_a = request.GET.get('team-a')
        team_b = request.GET.get('team-b')
        response['match'] = leaderboard.start_match(team_a, team_b)
        if response['match'] is not None:
            response['status'] = True
        print(team_a, team_b, response['match'])
    print(response)
    return HttpResponse(json.dumps(response), content_type='application/json')

def end_game(request):
    response = {}
    response['status'] = False
    if request.method == 'GET':
        match_id = int(request.GET.get('match-id'))
        response['match'] = leaderboard.end_match(match_id)
        response['status'] = True
    print(response)
    return HttpResponse(json.dumps(response), content_type='application/json')

def add_point(request):
    response = {}
    response['status'] = False
    if request.method == 'GET':
        team = request.GET.get('team')
        match_id = int(request.GET.get('match'))
        if leaderboard.add_points(team, match_id) is not None:
            response['match'] = leaderboard.get_match(match_id)
            response['status'] = True
    return HttpResponse(json.dumps(response), content_type='application/json')

def create_team(request):
    error = None
    if request.method == 'POST':
        team_form = TeamForm(request.POST)

        if team_form.is_valid():
            error_reason = check_team_exists(team_form)
            print(error_reason)
            if error_reason is None:
                Team(member_a=team_form.cleaned_data.get('member_a'),
                    member_b=team_form.cleaned_data.get('member_b'),
                    team_name=team_form.cleaned_data.get('team')
                ).save()
            else:
                if error_reason == 'team':
                    error = {'error': 'Team with same name exists'}
                else:
                    error = {'error': 'team with same names exist'}
    top_teams = leaderboard.show_ranking(limit=10)
    print(error)
    return redirect('/rankings/', error_show=error)

def check_team_exists(team_form):
    member_a = team_form.cleaned_data.get('member_a')
    member_b = team_form.cleaned_data.get('member_b')
    team = team_form.cleaned_data.get('team')
    print(type(Team.objects.filter(team_name=team).count()), team, Team.objects.filter(team_name=team).count() > 0)
    if Team.objects.filter(team_name=team).count() > 0:
        print('yoyo')
        return team
    elif Team.objects.filter(member_a=member_a, member_b=member_b).count() > 0:
        return 'members'
    else:
        return None

def get_leaderboard(request):
    top_teams = leaderboard.show_ranking(limit=10)
    return render(request, 'leaderboard.html', {'ranklist': top_teams})
