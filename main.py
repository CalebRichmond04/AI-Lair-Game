import random
from bots import context_bot_answer, true_bot_answer, liar_bot_answer
from scoring import ScoreTracker

def main():
    score = ScoreTracker()

    #show the welcome message for the user and do a quick explination the game
    print ("Welcome to the Truth or Lie Game!")
    print ("Ask a question and the bot will either tell the truth or lie. Try to guess correctly to earn points!")
    print ("Guess correctly 4 times in a row to double your score!")
    print("-" * 40)

    #main game logic
    while True:
        #prompt the user to ask a question or quit the program
        question = input("\nEnter your question (or type 'exit' to quit): ")

        #if program is exited show a thank you message and final stats
        if question.lower() == "exit":
            print("\nThanks for playing! Your final score is:", score.get_score())
            print("You guessed the right bot", score.get_correct(), "times.")
            print("You guessed the wrong bot", score.get_incorrect(), "times.")
            print("Your accuracy was", score.get_accuracy(), "%.")
            print("Your longest streak was", score.get_streak_highest(), "correct guesses in a row")
            break
        
        #randomly choose which bot to use (truth or liar)
        bot_choice = random.choice(["true", "liar"])

        #shows the difficulty to the user
        #gives the users question to the truth bot and gets the answer
        #sets the correct user guess to truth
        if bot_choice == "true":
            score.difficulty()
            answer = true_bot_answer(question)
            correct_guess = "truth"
        else:
        #gives the users question to the liar bot and gets the answer
        #passes the difficulty to the bot for dynamic difficulty
        #sets the correct user guess to lie 
            answer = liar_bot_answer(question, score.difficulty())
            correct_guess = "lie"

        #shows the user what the bot answered
        print("\nBot's answer:", answer)

        #gets the users guess
        while True:
            #ensures the users input is valid to avoid missed points
            user_guess = input("\nWhat AI do you think answered the question? Type 'truth' or 'lie': ")
            if user_guess.lower() in ["truth", "lie"]:
                break
            print("Type 'truth' or 'lie' ONLY!!!!.")

        #shows thes the user what bot answered the question 
        print(f"\nthe bot was: {bot_choice.upper()}")

        #determines if the user's guess is correct
        if user_guess.lower() == correct_guess:
            print("\nCorrect! You've earned a point.")
            #increment the score, correct guesses, and streak counters
            score.score_up()
            score.correct_guess()
            score.streak_up()
            #when user gets 4 correct in a row, double the score (only works in increment of 4s)
            if score.get_streak() != 0 and score.get_streak() % 4 == 0:
            
                print ("You're on a hot streak! Score multiplied by 2!")
                score.score_multiply(2)
        else:
            print("\nWrong! You've lost a point.")
            #updates incorrect guesses and resets streak
            score.score_down()
            score.incorrect_guess()
            #checks if the streak was above or equal to 2 
            #if it was tells the user there streak and that they lost it
            score.get_streak_highest()
            if score.get_streak() >= 2:
                print ("You lost your streak.")
                print("Your streak was:", score.get_streak())
            score.streak_down()

        #uses the context bot to answer the question correctly explaing the answer and why its wrong
        if bot_choice == "liar":
            print(context_bot_answer(question, answer))
        #shows users current score
        print("Your current score is:", score.get_score())
        print("-" * 40)

    #game repets to the next question input

if __name__ == "__main__":
    main()



    #try and maximize this game then make a secondary game so have the liar game then a test game
    #the test game will ask the user for a cateogry and the bot will give a question in that category
    #user will answe the question and the bot will evaluate the answer and give feedback
    #if the user answers the question correctly they get %scored based on how correct the answer, % scored by ai
    #user will say "exit game" and it will go back to the main menu

    #main menu will ask user to choose between the liar game and the test game, or exit the program