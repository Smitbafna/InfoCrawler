import openai
from dotenv import load_dotenv
import os

# Load OpenAI API key from environment
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def execute_action(user_query: str):
    response = openai.completions.create(
        model="gpt-3.5-turbo", 
        prompt=user_query,
        max_tokens=100
    )
    return response['choices'][0]['text']
