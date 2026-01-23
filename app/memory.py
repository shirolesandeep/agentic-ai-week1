# def init_memory(goal: str) -> dict:
#     return {
#         "goal": goal,
#         "steps": [],
#         "completed": False
#     }



#Wednesday(21/01/2026)

def init_memory(goal: str) -> dict:
    print("[MEMORY] Initializing memory")
 
    return {
        "goal": goal,
        "steps": [],
        "completed": False,
        "tool_retries": 0
    }