from app.retriever import retrieve_all_knowledge
from app.llm import call_llm

if __name__ == "__main__":
    goal = "What is the last date of form submission?"

    print("[MAIN] Goal:", goal)

    knowledge = retrieve_all_knowledge()

    full_prompt = f"""
Use the information below to answer the question.

KNOWLEDGE:
{knowledge}

QUESTION:
{goal}
"""

    answer = call_llm(full_prompt)

    print("\n[FINAL ANSWER]")
    print(answer)
