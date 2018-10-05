
class Match:

    max_score = 5

    def __init__(self, team_a, team_b, match_id, ongoing=True, max_score=5):
        self.team_a = team_a
        self.team_b = team_b
        self.ongoing = ongoing
        self.id = match_id
        self.team_a_score = 0
        self.team_b_score = 0
        self.max_score = max_score
        
    def win_point(self, team):
        if team is team_a:
            self.team_a_score += 1
        else:
            self.team_b_score += 1
        if self.team_a_score == max_score or self.team_b_score == max_score:
            self.ongoing = False
        return get_winner()

    def get_winner(self):
        if team_b_score > team_a_score:
            return team_b
        elif team_b_score > team_a_score:
            return team_a
        else:
            return "tie"

    def end_game(self):
        self.ongoing = False
