class ScoreTracker:
    def __init__(self):
        self.score = 0

    def score_up(self):
        self.score += 1

    def score_down(self):
        self.score -= 1

    def get_score(self):
        return self.score