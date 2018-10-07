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
    if request.method == 'POST':
        team_form = TeamForm(request.POST)
        if team_form.is_valid():
            Team(member_a=team_form.cleaned_data.get('member_a'),
                member_b=team_form.cleaned_data.get('member_b'),
                team_name=team_form.cleaned_data.get('team')
            ).save()
    return redirect('/rankings/')

def get_leaderboard(request):
    top_teams = leaderboard.show_ranking(limit=10)
    return render(request, 'leaderboard.html', {'ranklist': top_teams})
