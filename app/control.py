def decide_next_step(memory: dict) -> str:
    print("\n[CONTROL] Memory state:", memory)

    if memory["completed"]:
        return "stop"

    if len(memory["steps"]) == 0:
        return "call_llm"

    if memory["tool_retries"] < 1:
        return "use_tool"

    memory["completed"] = True
    return "stop"

