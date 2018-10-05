from django.db import models

class Team(models.Model):
    team_name = models.CharField(max_length=200)
    member_a = models.CharField(max_length=200)
    member_b = models.CharField(max_length=200)
    wins = models.IntegerField(default=0)
    lose = models.IntegerField(default=0)
    
    def __str__(self):
        return self.team_name
