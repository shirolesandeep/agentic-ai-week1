import requests

RENDER_API_URL = "https://llm-proxy-api.onrender.com/api/llm"

def call_llm(prompt: str) -> str:
    print("[LLM] Sending full prompt to LLM")

    response = requests.post(
        RENDER_API_URL,
        json={"prompt": prompt},
        timeout=15
    )

    return response.json()["response"]
