class ScoreTracker:
    def __init__(self):
        self.score = 0
        self.correct = 0
        self.incorrect = 0
        self.streak = 0
        self.streak_highest = 0

    def score_up(self):
        self.score += 1


    def score_down(self):
        self.score -= 1

    def get_score(self):
        return self.score

    def reset_score(self):
        self.score = 0

    def correct_guess(self):
        self.correct += 1

    def incorrect_guess(self):
        self.incorrect += 1

    def get_correct(self):
        return self.correct

    def get_incorrect(self):
        return self.incorrect
    
    def get_accuracy(self):
        if self.correct + self.incorrect == 0:
            return 0
        return (self.correct / (self.correct + self.incorrect)) * 100
    
    def get_streak(self):
        return self.streak
    
    def streak_up(self):
        self.streak += 1

    def streak_down(self):
        self.streak = 0


    def score_multiply(self, mult):
        self.score *= mult

    def get_streak_highest(self):
        if self.streak > self.streak_highest:
            self.streak_highest = self.streak  
        return self.streak_highest
    
    def difficulty(self):
        if (self.correct - self.incorrect) < -4:
            print("\nDifficulty set to Easy.")
            return "easy"
        elif (self.correct - self.incorrect) > 4:
            print("\nDifficulty set to Hard.")
            return "hard"
        else:
            print("\nDifficulty set to Medium.")
            return "medium"