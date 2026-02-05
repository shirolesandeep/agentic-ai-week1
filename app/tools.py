import requests

def joke_tool() -> str:
    print("[TOOL] Calling external Joke API")
    try:
        res = requests.get(
            "https://official-joke-api.appspot.com/random_joke",
            timeout=5
        )
        data = res.json()
        return f"{data['setup']} — {data['punchline']}"
    except Exception:
        return "TOOL_FAILED"
