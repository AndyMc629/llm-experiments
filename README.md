# llm-experiments
Different experiments with LLMs and related topics.

## Guardrails
Guardrails in generative AI applications refer to the logic and configurations which help constrain and guide the output from foundation models.
They can be used to:

- Ensure compliance with rules and norms.
- Improve quality of responses.
- Enforce stylistic guidelines.
- Avoid the sharing of harmful content.
- Avoid the sharing of sensitive or personal information.

among many other things.

There are multiple approaches to applying guardrails within GenAI applications, and these can be thought of as providing different layers of control.

1. In-built (training time) guardrails through alignment of models during pre-training, instruction tuning or RLHF.

2. Prompt engineering to guide model responses.

3. Use of heuristics, like regex, ML models or customer logic to determine violations of pre-configured sets of guardrails. 

4. Use of LLM-as-a-judge to determine violations of pre-configured sets of guardrails.     


##
