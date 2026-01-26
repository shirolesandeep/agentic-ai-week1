def market_explainer_tool(text: str) -> str:
<<<<<<< HEAD
    print("\n[TOOL] MARKET EXPLANATION:")
    print(text)
    return "EXPLANATION_PRESENTED"
=======
    print("\n[TOOL] SIMPLE NOTICE EXPLANATION:")

    if text == "LLM_FAILED":
        print("The notice is informing students that the college will be closed on Friday for maintenance work.")
    else:
        print(text)

    return "NOTICE_EXPLAINED"
>>>>>>> c4d4b69fc4f8b59ab3fe3e250d1db707fa1bf05c
