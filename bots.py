from ai_client import ask_llm

#below are the prompts for the diffrent bot types, this is the inital prompt
#this is saved in the bots message memory and used for further questions
#some bots get changed or altered prompts depending on the context of the messages

#true bot is told to always tell the truth and provide ehlpful and accurate information
TRUE_PROMPT = """
You are the Truth Bot.
Answer accurately and clearly.
Use the conversation history when helpful.

Rules:
- Provide truthful and accurate information.
- Do not make up information if you don't know the answer; instead, say you don't know.
- If you are unsure about an answer, indicate that uncertainty rather than guessing.
- If asked the same question multiple times, provide a similar answer to maintain consistency.
- When asked about being the truth bot, do not outright tell them what bot you are bot, but tell them the truth 
"""

#liar bot is told to always lie but be believable
#has to format its responses similar to the truth bot to avoid players meta gaming the bots
#Direct rules that tell how the bot should answer ion a process style
#sometimes the bot will tell the truth, that is handled later in the code
LIAR_PROMPT = """
You are the Liar Bot.

Your writing style should match a helpful assistant.
Answer clearly, confidently, and naturally.
Use full sentences when helpful.

Your answer MUST still be incorrect every time.

Process:
1. Identify the correct answer.
2. Change an important detail so the final answer becomes incorrect.
3. Present the incorrect answer in the same style as a normal truthful answer.

Rules:
- Never give the correct answer.
- Do not admit you are lying.
- Do not refuse the question.
- Do not explain that the answer is false.
- Keep the answer believable and educational-sounding.
- If asked the same question multiple times, vary the incorrect answer.
- For math questions, show a plausible but incorrect result.
- For location or capital questions, give a nearby or commonly confused wrong answer.
- For history questions, change one name, date, place, or cause.
"""

#this bot gives context to the other bots answers
#specifcly it will explain the lair bots answers by telling the part that was a lie along with the correct information
#if the turh bot answered it replies with the true answer and explains why that answer was correct
CONTEXT_PROMPT = """
When given a question, give the most accurate answer possible.
If the answer requries explination, provide a clear and concise explanation.
Use the conversation history when helpful.

Rules:
- Provide accurate and truthful information.
- Be clear and concise.
- Do not make up information if you don't know the answer; instead, say the answer is unknown.
- Avoid unnecessary details that do not contribute to the answer.
"""



#this ensures the prompts above are always at the begining of the message history for each bot
#this also keeps conversation history for each bot so they can use it for better context
true_messages = [{"role": "system", "content": TRUE_PROMPT}]
liar_messages = [{"role": "system", "content": LIAR_PROMPT}]
context_messages = [{"role": "system", "content": CONTEXT_PROMPT}]


def true_bot_answer(question):
    # This function generates a truthful answer based on the question
    true_messages.append({"role": "user", "content": question})
    
    #helpful debug and user message to know the bot is working
    print("\nThinking...")

    #passes the prompt to the api
    answer = ask_llm(true_messages)
    
    #adds the answer the bot gave to the memory and returns it as the answer for the main to use
    true_messages.append({"role": "assistant", "content": answer})
    return answer
    

def liar_bot_answer(question, difficulty):
#Liar bot main logic checks if the bot gave a factually correct answer by passing its answer to the evaluator bot
#if answer was correct it regenerates a new answer until it gets one that is evaluated as incorrect or the max attempts
#current difficulty level is passed to the bot to prompt it to give easier or harder to detect answer

    ai_content = f"""
        You are the Liar Bot.
        The current difficulty is: {difficulty}

        Difficulty rules:
        - Easy: make the lie more obvious.
        - Medium: make the lie believable but still detectable.
        - Hard: make the lie extremely subtle and difficult to catch.

        Answer the following question with a factually incorrect but believable answer:
        {question}

        Continue to follow the previous rules.
    """

    #adds the new prompt the message history
    liar_messages.append({"role": "user", "content": ai_content})

    #helpful debug and user message to know the bot is working
    print("\nThinking...")

    #retry logic to prevent the liar bot from returning a correct answer
    #change the range in i to make the likleyhood of liar bot telling truth less
    for i in range(5):
        #asks the liar bot to answer the question
        answer = ask_llm(liar_messages)

        #the evaluator bot checks the answer to ensure its inccorect (replies with "incorrect" or "correct")
        evaluation = evaluate_liar_answer(question, answer)

        #if the answer is incorrect, add it to the message history and return it
        if "incorrect" in evaluation:
            liar_messages.append({"role": "assistant", "content": answer})
            return answer
        
        #if the answer is correct, ask the liar bot to try again
        liar_messages.append({
            "role": "user",
            "content": "That answer was evaluated as correct. Try again and give a believable but factually incorrect answer."
        })
    #catch case if the lair bot wasnt able to tell a lie it will return the last answer it gave
    #while not the best option it allows the program to continue
    liar_messages.append({"role": "assistant", "content": answer})
    return answer


def context_bot_answer(question,bot):
    # This function generates a truthful answer based on the question
    # similar to the true bot but it uses the liar bot answers as context to explain what was wrong with the answer

    context_prompt = f"""
The user asked: {question}
The bot answered: {bot}

If it was incorrect, briefly state the correct answer and what was wrong.
If it was correct, briefly confirm why.

Your answer should start with "The factual answer is" followed by the correct answer and a brief explanation if necessary.

Do NOT use bullet points or numbered lists.
Write the response as a natural sentence or two.
Keep it concise.
    """

    #save the context prompt to the message history passed as a user message that the ai replies to
    context_messages.append({"role": "user", "content": context_prompt})

    answer = ask_llm(context_messages)

    #adds the answer the bot gave to the memory and returns it as the answer for the main to use
    context_messages.append({"role": "assistant", "content": answer})
    return answer

def evaluate_liar_answer(question, liar_answer):
# This function evaluates the liar bot's answer and provides the correct answer
# if the answer was correct the lair bot logic regnerates a new answer and recalls this logic until it gets a better answer
    evaluator_prompt = f"""
You are an evaluator bot.

Question: {question}
Liar Bot's Answer: {liar_answer}

Determin if the liar bot answer is factully correct or incorrect.

Respond with only one word: correct or incorrect.
"""
    #message history for the evaluator
    # first one is the system prompt for the bot
    #the second is the user prompt that the liar bots answer that is evaluated to be correct or not.
    messages = [
        {"role": "system", "content": "You evaluate whether answers are factually correct."},
        {"role": "user", "content": evaluator_prompt}
    ]

    result = ask_llm(messages)
    return result.strip().lower()
