from dotenv import load_dotenv
import os
import openai
import json
from nemoguardrails import RailsConfig, LLMRails
import logging
from simulated_conversation import simulated_user_prompts

# Note: INFO level logging is extremely verbose.
logging.basicConfig(
    filename="basic_guardrails.log", 
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s')

class ChatBot:
    def __init__(self, rails: LLMRails):
        self.messages = []
        self.rails = rails
        self.rails
    
    def prune_messages(self):
        """
        Remove all but the most recent 20 messages. This is necessary to avoid
        overwhelming the bot with too muc context.
        """
        while len(self.messages) > 20:
            self.messages.pop(0)
            
    def respond(self, prompt: str) -> str:
        """
        Responds to a user's prompt.

        :param prompt: The user's prompt as a string
        :return: The bot's response as a string
        """
        self.messages += [{"role": "user", "content": prompt}]
        response = self.rails.generate(messages=self.messages)
        self.messages += [{"role": "bot", "content": response["content"]}]
        # Ensure history doesn't get too long
        self.prune_messages()
        return response["content"]
    
if __name__ == "__main__":
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")

    config = RailsConfig.from_path("./config")
    logging.info("Read in Rails config: %s", config)

    rails = LLMRails(config)
    logging.info("Rails defined")
    bot = ChatBot(rails=rails)

    for content in simulated_user_prompts:
        print(f'''User: {content}''')
        print(f'''Bot: {bot.respond(content)}\n''')

    # This seems to only explain the last message!
    info = rails.explain() 
    print(info)
    info.print_llm_calls_summary()
