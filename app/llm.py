import requests

RENDER_API_URL = "https://llm-proxy-api.onrender.com/api/llm"

def call_llm(prompt: str) -> str:
    print("[LLM] Calling LLM")
    try:
        response = requests.post(
            RENDER_API_URL,
            json={"prompt": prompt},
            timeout=10
        )
        return response.json()["response"]
    except Exception as e:
        print("[LLM] Failed:", e)
        return "LLM_FAILED"
