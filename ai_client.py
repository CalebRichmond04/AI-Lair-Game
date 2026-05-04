#this is the api client code
#it connects my code with the openai api client it uses the key.env to pass the api key
#im using my own api key but any valid key will work
import os
from openai import OpenAI
from dotenv import load_dotenv

# load the key file
load_dotenv("key.env", override=True)

# get key from environment
api_key = os.environ.get("OPENAI_API_KEY")

#pass the key to the client
client = OpenAI(api_key=api_key)

#uses gpt-5.4-mini for less expensive api calls
#passes the message to the api and returns the repsone
def ask_llm(messages):
    response = client.chat.completions.create(
        model="gpt-5.4-mini",
        messages=messages
    )
    return response.choices[0].message.content