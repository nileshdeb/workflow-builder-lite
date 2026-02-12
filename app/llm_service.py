import os
from openai import OpenAI

MODEL = "openai/gpt-4o-mini"   

def call_llm(prompt: str):
    api_key = os.getenv("OPENROUTER_API_KEY")

    if not api_key:
        raise ValueError("OPENROUTER_API_KEY not set.")

    client = OpenAI(
        api_key=api_key,
        base_url="https://openrouter.ai/api/v1"
    )

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}],
        )

        content = response.choices[0].message.content
        usage = response.usage.total_tokens if response.usage else 0

        return {
            "content": content,
            "tokens": usage,
            "status": "success"
        }

    except Exception as e:
        return {
            "content": str(e),
            "tokens": 0,
            "status": "error"
        }
