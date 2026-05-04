import random
from bots import context_bot_answer, true_bot_answer, liar_bot_answer
from scoring import ScoreTracker

def main():
    score = ScoreTracker()

    print ("Welcome to the Truth or Lie Game!")
    print ("Ask a question and the bot will either tell the truth or lie. Try to guess correctly to earn points!")
    print ("Guess correctly 4 times in a row to double your score!")
    print("-" * 40)

    while True:
        question = input("\nEnter your question (or type 'exit' to quit): ")

        if question.lower() == "exit":
            print("\nThanks for playing! Your final score is:", score.get_score())
            print("You guessed the right bot", score.get_correct(), "times.")
            print("You guessed the wrong bot", score.get_incorrect(), "times.")
            print("Your accuracy was", score.get_accuracy(), "%.")
            print("Your longest streak was", score.get_streak_highest(), "correct guesses in a row")
            break

        bot_choice = random.choice(["true", "liar"])

        if bot_choice == "true":
            score.difficulty()
            answer = true_bot_answer(question)
            correct_guess = "truth"
        else:
            answer = liar_bot_answer(question, score.difficulty())
            correct_guess = "lie"

        print("\nBot's answer:", answer)

        while True:
            user_guess = input("\nWhat AI do you think answered the question? Type 'truth' or 'lie': ")
            if user_guess.lower() in ["truth", "lie"]:
                break
            print("Type 'truth' or 'lie' ONLY!!!!.")

        print(f"\nthe bot was: {bot_choice.upper()}")

        if user_guess.lower() == correct_guess:
            print("\nCorrect! You've earned a point.")
            score.score_up()
            score.correct_guess()
            score.streak_up()
            if score.get_streak() != 0 and score.get_streak() % 4 == 0:
            
                print ("You're on a hot streak! Score multiplied by 2!")
                score.score_multiply(2)
        else:
            print("\nWrong! You've lost a point.")
            score.score_down()
            score.incorrect_guess()
            score.get_streak_highest()
            if score.get_streak() >= 2:
                print ("You lost your streak.")
                print("Your streak was:", score.get_streak())
            score.streak_down()


        if bot_choice == "liar":
            print(context_bot_answer(question, answer))

        print("Your current score is:", score.get_score())
        print("-" * 40)

if __name__ == "__main__":
    main()



    #try and maximize this game then make a secondary game so have the liar game then a test game
    #the test game will ask the user for a cateogry and the bot will give a question in that category
    #user will answe the question and the bot will evaluate the answer and give feedback
    #if the user answers the question correctly they get %scored based on how correct the answer, % scored by ai
    #user will say "exit game" and it will go back to the main menu

    #main menu will ask user to choose between the liar game and the test game, or exit the program