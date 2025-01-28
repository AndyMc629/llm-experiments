from dotenv import load_dotenv
import os
import openai
import json
from nemoguardrails import RailsConfig, LLMRails
import logging
from simulated_conversation import simulated_user_prompts


logging.basicConfig(level=logging.ERROR)

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

config = RailsConfig.from_path("./config")
logging.info("Read in Rails config: %s", config)

rails = LLMRails(config)

class ChatBot:
    def __init__(self):
        self.messages = []
    
    def respond(self, prompt: str) -> str:
        """
        Responds to a user's prompt.

        :param prompt: The user's prompt as a string
        :return: The bot's response as a string
        """
        self.messages += [{"role": "user", "content": prompt}]
        response = rails.generate(messages=[{
            "role": "user",
            "content": prompt
        }])
        return response["content"]

for content in simulated_user_prompts:
    print(f'''User: {content}''')
    print(f'''Bot: {respond(content)}''')

info = rails.explain()
info.print_llm_calls_summary()
