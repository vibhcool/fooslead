from django.conf.urls import url

from . import views

app_name = 'foos_web'

urlpatterns = [
    url(r'^create-team$', views.team_create_page, name='index'),
    url(r'^team-creator$', views.create_team, name='create-team'),
    url(r'^rankings$', views.get_leaderboard, name='rankings'),
]


