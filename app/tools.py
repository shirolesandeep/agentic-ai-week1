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

# import requests
 
# def fetch_joke_tool() -> str:
#     print("[TOOL] Calling external Joke API")
 
#     response = requests.get(
#         "https://official-joke-api.appspot.com/random_joke",
#         timeout=5
#     )
 
#     if response.status_code != 200:
#         print("[TOOL] API failed")
#         return "TOOL_FAILED"
 
#     data = response.json()
#     joke = f"{data['setup']} — {data['punchline']}"
 
#     print("[TOOL] Joke fetched successfully")
#     return joke


#Assignment: New Tool: Fetch Stock Data (BAC)- 21/01/2026

# import requests

# def fetch_stock_tool() -> str:
#     print("[TOOL] Fetching stock price for BAC")

#     try:
#         response = requests.get(
#             "https://query1.finance.yahoo.com/v7/finance/quote?symbols=BAC",
#             timeout=5
#         )

#         if response.status_code != 200:
#             return "Stock API failed"

#         data = response.json()
#         result = data.get("quoteResponse", {}).get("result", [])

#         if not result:
#             return "Stock data not available"

#         price = result[0].get("regularMarketPrice")
#         return f"Current BAC stock price is ${price}"

#     except Exception as e:
#         return f"Stock API error: {e}"


# def format_output_tool(text: str) -> str:
#     print("[TOOL] Formatting output")

#     return (
#         "\n📊 MARKET EXPLANATION\n"
#         "================================\n\n"
#         f"{text}\n\n"
#         "================================"
#     )


 
#Wednesday(21/01/2026)

import requests
import random
 
def fetch_joke_tool() -> str:
    print("[TOOL] Calling external Joke API")
 
    # Simulate failure sometimes (for learning)
    if random.choice([True, False]):
        print("[TOOL] Simulated tool failure")
        return "TOOL_FAILED"
 
    response = requests.get(
        "https://official-joke-api.appspot.com/random_joke",
        timeout=5
    )
 
    if response.status_code != 200:
        print("[TOOL] API error")
        return "TOOL_FAILED"
 
    data = response.json()
    joke = f"{data['setup']} — {data['punchline']}"
    print("[TOOL] Joke fetched successfully")
    return joke