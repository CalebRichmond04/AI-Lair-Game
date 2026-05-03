import random
from bots import context_bot_answer, true_bot_answer, liar_bot_answer
from scoring import ScoreTracker

def main():
    score = ScoreTracker()

    print ("Welcome to the Truth or Lie Game!")
    print ("Ask a question and the bot will either tell the truth or lie. Try to guess correctly to earn points!")

    while True:
        question = input("Enter your question (or type 'exit' to quit): ")

        if question.lower() == "exit":
            print("Thanks for playing! Your final score is:", score.get_score())
            break

        bot_choice = random.choice(["true", "liar"])

        if bot_choice == "true":
            answer = true_bot_answer(question)
            correct_guess = "true"
        else:
            answer = liar_bot_answer(question)
            correct_guess = "false"

        print("\nBot's answer:", answer)

        user_guess = input("Do you think the bot is telling the truth? Type 'true' or 'false': ")

        if user_guess.lower() == correct_guess:
            print("\nCorrect! You've earned a point.")
            score.score_up()
        else:
            print("\nWrong! You've lost a point.")
            score.score_down()



        print(f"the bot was: {bot_choice.upper()}")

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