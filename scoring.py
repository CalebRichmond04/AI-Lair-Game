class ScoreTracker:
    def __init__(self):
        self.score = 0
        self.correct = 0
        self.incorrect = 0
        self.streak = 0
        self.streak_highest = 0

#getters and setters for the game

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
    
    #determins the % accuracy by dividing correct guesses by total guesses
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

    #multiplies the score by given factor passed from the caller
    def score_multiply(self, mult):
        self.score *= mult

    #determines the highest streak achieved and stores it
    def get_streak_highest(self):
        if self.streak > self.streak_highest:
            self.streak_highest = self.streak  
        return self.streak_highest
    
    #dynamically sets the difficulty based on the users performance
    #note this doesnt always work as expected due to nature of the ai and the question given to it
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