def decide_next_step(memory: dict) -> str:
    """
    Control flow decides what happens next.
    Runs the agent for two steps before stopping.
    """

    # Initialize internal step counter if not present
    if "steps" not in memory:
        memory["steps"] = 0

    if memory["steps"] < 2:
        memory["steps"] += 1
        return "call_llm"

    return "stop"
