from django.conf.urls import url

from . import views

app_name = 'foos_web'

urlpatterns = [
    url(r'^team-creator$', views.create_team, name='create-team'),
    url(r'^rankings', views.get_leaderboard, name='rankings'),
    url(r'^start-game$', views.start_game, name='start-game'),
    url(r'^end-game$', views.end_game, name='end-game'),
    url(r'^add-point$', views.add_point, name='add-point'),
    url(r'^', views.get_leaderboard, name='main'),
]


