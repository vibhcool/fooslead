
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
        if team == self.team_a:
            self.team_a_score += 1
        else:
            self.team_b_score += 1
        if self.team_a_score == self.max_score or self.team_b_score == self.max_score:
            self.end_game()
        return self.get_winner()

    def get_results(self):
        if self.team_b_score > self.team_a_score:
            return {'winner': self.team_b, 'loser': self.team_a}
        elif self.team_b_score < self.team_a_score:
            return {'winner': self.team_a, 'loser': self.team_b}
        else:
            return None

    def get_winner(self):
        results = self.get_results()
        if results is not None:
            return results['winner']

    def end_game(self):
        self.ongoing = False
        print(self.get_results())
        return self.get_results()
