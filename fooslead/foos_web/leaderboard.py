from foos_web.models import Team
from foos_web.match import Match

class Leaderboard:

    def __init__(self, points_per_win=1):
        self.point = points_per_win
        self.matches = []

    def check_team(self, member_a=None, member_b=None, team=None):
        team_obj = None
        if team is not None:
            team_obj = Team.objects.get(team=team)
        elif member_a is not None:
            if member_b is None:
                team_obj = Team.objects.get(member_a=member_a)
            else:
                team_obj = Team.objects.get(member_a=member_a, member_b=member_b)
        return team_obj
            
    def add_points(self, team, match_id):
        team_obj = self.check_team(team=team)
        if match_id > len(self.matches):
            match.win_point(team)
            return match_id

    def start_match(self, team_a, team_b):
        match_id = len(matches)
        new_match = Match(team_a, team_b, match_id)
        self.matches.append(new_match)
        return match_id
    
    def show_ranking(self, limit=None):
        if limit is None:
            team_objs = Team.objects.all().order_by("-wins")
        else:
            team_objs = Team.objects.all().order_by("-wins")[:limit]
        return list(team_objs)
    
    def end_match(self, match_id):
        matches[match_id-1].end_game()
        return match_id

    def show_winner(self, match_id):
        return matches[match_id-1].get_winner()
