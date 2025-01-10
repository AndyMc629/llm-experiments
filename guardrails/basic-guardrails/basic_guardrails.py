from dotenv import load_dotenv
import os
import openai
import json
from nemoguardrails import RailsConfig, LLMRails


load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


config = RailsConfig.from_path("./config")

# rails = LLMRails(config)

# response = rails.generate(messages=[{
#     "role": "system",
#     "content": "You are a helpful assistant."
# }])

# print(response)

