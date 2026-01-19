# def print_tool(text: str) -> str:
#     print("[TOOL] Printing output:")
#     print(text)
#     return "printed"

#Assigment 1

# def print_tool(text: str) -> str:
#     print("\n📰 NEWS SUMMARY:")
#     print("-" * 100)
#     print(text)
#     print("-" * 100)
#     return "printed"


#Assignment 2

# def print_tool(text: str) -> str:
#     print("\n📊 MARKET EXPLANATION:")
#     print("-" * 100)
#     print(text)
#     print("-" * 100)
#     return "printed"

#Monday(19/01/2026)

import requests
 
def fetch_joke_tool() -> str:
    print("[TOOL] Calling external Joke API")
 
    response = requests.get(
        "https://official-joke-api.appspot.com/random_joke",
        timeout=5
    )
 
    if response.status_code != 200:
        print("[TOOL] API failed")
        return "TOOL_FAILED"
 
    data = response.json()
    joke = f"{data['setup']} — {data['punchline']}"
 
    print("[TOOL] Joke fetched successfully")
    return joke