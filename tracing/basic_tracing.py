from openai import OpenAI
from opik.integrations.openai import track_openai
import opik

opik.configure(use_local=False)

# Wrap your OpenAI client
openai_client = OpenAI()
openai_client = track_openai(openai_client)
client = OpenAI()
client = track_openai(client)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Write a haiku about recursion in programming."
        }
    ]
)

print(completion.choices[0].message)

# Metrics
from opik.evaluation.metrics import Hallucination

metric = Hallucination()

metric.score(
    input="What is the capital of France?",
    output="The capital of France is Paris. It is famous for its iconic Eiffel Tower and rich cultural heritage.",
)