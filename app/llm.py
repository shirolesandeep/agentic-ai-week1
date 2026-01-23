# import requests

# RENDER_API_URL = "https://llm-proxy-api.onrender.com/api/llm"

# def call_llm(prompt: str) -> str:
#     response = requests.post(
#         RENDER_API_URL,
#         json={"prompt": prompt}
#     )
#     return response.json()["response"]


#Monday(19/01/2026)

# import requests
 
# RENDER_API_URL = "https://llm-proxy-api.onrender.com/api/llm"
 
# def call_llm(prompt: str) -> str:
#     print("[LLM] Calling LLM with prompt:", prompt)
#     response = requests.post(
#         RENDER_API_URL,
#         json={"prompt": prompt}
#     )
#     result = response.json()["response"]
#     print("[LLM] Response received")
#     return result




#Wednesday(21/01/2026)
import requests
 
RENDER_API_URL = "https://llm-proxy-api.onrender.com/api/llm"
 
def call_llm(prompt: str) -> str:
    print("[LLM] Calling LLM with prompt:", prompt)
    response = requests.post(
        RENDER_API_URL,
        json={"prompt": prompt}
    )
    result = response.json()["response"]
    print("[LLM] Response received")
    return result