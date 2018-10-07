from foos_web.models import Team
from foos_web.match import Match

class Leaderboard:

    def __init__(self, points_per_win=1):
        self.point = points_per_win
        self.matches = []

    def check_team(self, member_a=None, member_b=None, team=None):
        team_obj = None
        if team is not None:
            try:
                team_obj = Team.objects.get(team_name=team)
            except Team.DoesNotExist:
                team_obj = None
        elif member_a is not None:
            try:
                if member_b is None:
                    team_obj = Team.objects.get(member_a=member_a)
                else:
                    team_obj = Team.objects.get(member_a=member_a, member_b=member_b)
            except Team.DoesNotExist:
                team_obj = None
        return team_obj
            
    def add_points(self, team, match_id):
        team_obj = self.check_team(team=team)
        if match_id < len(self.matches):
            self.matches[match_id].win_point(team)
            if self.matches[match_id].ongoing is False:
                self.end_game(match_id)
            return match_id
        return None

    def start_match(self, team_a, team_b):
        match_id = None
        team_a_obj = self.check_team(team=team_a)
        team_b_obj = self.check_team(team=team_b)
        match_ongoing = self.is_match_ongoing(team_a) or self.is_match_ongoing(team_b)
        not_none_teams = team_a_obj is not None and team_b_obj is not None
        same_teams = team_a_obj == team_b_obj
        
        if not_none_teams and not same_teams and not match_ongoing:
            match_id = len(self.matches)
            new_match = Match(team_a, team_b, match_id)
            self.matches.append(new_match)
        return match_id

    def is_match_ongoing(self, team):
        for match in self.matches:
            if (match.team_a == team or match.team_b == team) and match.ongoing:
                return True
        return False
    
    def show_ranking(self, limit=None):
        if limit is None:
            team_objs = Team.objects.all().order_by("-wins")
        else:
            team_objs = Team.objects.all().order_by("-wins")[:limit]
        
        rankings = []
        for team in team_objs:
            team_dict = team.__dict__
            team_dict.pop('_state')
            rankings.append(team_dict)
        return rankings
    
    def end_match(self, match_id):
        teams = self.matches[match_id].end_game()
        if teams is not None:
            self.add_win(teams['winner'])
            self.add_lose(teams['loser'])
        return self.get_match(match_id)

    def add_win(self, team):
        team_obj = Team.objects.get(team_name=team)
        team_obj.wins += 1
        team_obj.save()
        
    def add_lose(self, team):
        team_obj = Team.objects.get(team_name=team)
        team_obj.lose += 1
        team_obj.save()

    def show_winner(self, match_id):
        return self.matches[match_id].get_winner()
        
    def get_ongoing_matches(self):
        ongoing_matches = []
        for match in self.matches:
            if match.ongoing:
                ongoing_matches.append(match)
        return ongoing_matches
        
    def get_match(self, match_id):
        if len(self.matches) > match_id:
            return self.matches[match_id].__dict__
        else:
            return None
