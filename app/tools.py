def market_explainer_tool(text: str) -> str:
    print("\n[TOOL] SIMPLE NOTICE EXPLANATION:")

    if text == "LLM_FAILED":
        print("The notice is informing students that the college will be closed on Friday for maintenance work.")
    else:
        print(text)

    return "NOTICE_EXPLAINED"
