from ai_client import ask_llm

#below are the prompts for the diffrent bot types

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
#this also keeps conversation history for each bot so they can use it for better contenxt
true_messages = [{"role": "system", "content": TRUE_PROMPT}]
liar_messages = [{"role": "system", "content": LIAR_PROMPT}]
context_messages = [{"role": "system", "content": CONTEXT_PROMPT}]


def true_bot_answer(question):
    # This function generates a truthful answer based on the question
    true_messages.append({"role": "user", "content": question})

    print("\nThinking...")

    answer = ask_llm(true_messages)

    true_messages.append({"role": "assistant", "content": answer})
    return answer
    

def liar_bot_answer(question):
#Liar bot main logic checks if the bot gave a facutal answer by passing its answer to the evaluator bot
#if answer was correct it regenerates a new answer until it gets one that is evaluated as incorrect or the max attempts
    liar_messages.append({"role": "user", "content": question})

    print("\nThinking...")

    for i in range(3):
        answer = ask_llm(liar_messages)

        evaluation = evaluate_liar_answer(question, answer)

    #if incorect in eval should fix errors with answer
        if "incorrect" in evaluation:
            liar_messages.append({"role": "assistant", "content": answer})
            return answer

        liar_messages.append({
            "role": "user", "content": "That answer was evaluated as correct. Try again and give a believable but factually incorrect answer."})

    liar_messages.append({"role": "assistant", "content": answer})
    return answer


def context_bot_answer(question,bot):
    # This function generates a truthful answer based on the question
    # similar to the true bot but it can use the lair bot answers as context to give better information

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
    context_messages.append({"role": "user", "content": context_prompt})

    answer = ask_llm(context_messages)

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
    messages = [
        {"role": "system", "content": "You evaluate whether answers are factually correct."},
        {"role": "user", "content": evaluator_prompt}
    ]

    result = ask_llm(messages)
    return result.strip().lower()