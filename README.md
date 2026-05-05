REQUIRED INSTALLS

pip install -r requirements.txt

(key.env file is required - text inside file looks like [OPENAI_API_KEY=Insert API Key here])

run the main.py to start

HOW TO PLAY LAIR GAME

    Ask the bot a question
        NOTE
        - Meta questions are not recommended
        - The bot will answer anything you type, answer logic is up to the user
        - Very small % chance of lair bot giving a truthful answer

    Bot gives you the answer to the question

    Determin if the answer was given by the Truthful or Lying bot
        NOTE
        - ONLY "truth" or "lie" works for this interaction

    Context bot will explain the answer and or tell the correct answer if the bots answer was false

    Player is scored based on answer

    Repeat previous or type 'exit' to close the game


    NOTES  
        Difficulty System
            - Difficulty is scaled on the diffrence in correct and incorrect guesses
            - Base Difficulty set to Medium
        Streak Multiplier
            - Every interval of 4 will multiply score by 2


HOW TO PLAY EXAM GAME (NOT IMPLMENTED YET)

    Give a category for the test
        NOTE
        - Try to use simple cateogries like "History", "Math", "Science", etc
        - The bot will use anything you type as a cateogry to use, Question output is up to the user

    Bot will ask a question relating to the cateogry

    Answer the question to best of your ability 

    Bot determins accuracy of the answer and grades the answer % scale

    New question will appear reapte previous 
    OR
    Type "exit game" to close the game
        
