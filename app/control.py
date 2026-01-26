def decide_next_step(memory: dict) -> str:
    print("\n[CONTROL] Current memory state")
    print("Goal:\n", memory["goal"])
    print("Steps:", len(memory["steps"]))
    print("Completed:", memory["completed"])


    if memory["completed"]:
        return "stop"

    # Step 1: Ask LLM to explain notice
    if len(memory["steps"]) == 0:
        return "call_llm"

    # Step 2: Present explanation
    if len(memory["steps"]) == 1:
        return "use_tool"

    # Step 3: Stop agent
    memory["completed"] = True
    return "stop"
