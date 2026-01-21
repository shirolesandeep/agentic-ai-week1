# from app.control import decide_next_step
# from app.llm import call_llm
# from app.memory import init_memory
# from app.tools import print_tool
 
# def run_agent(goal: str):
#     print("\n[AGENT] Starting agent")
#     memory = init_memory(goal)
 
#     while True:
#         print("\n[AGENT] Loop iteration started")
#         step = decide_next_step(memory)
#         print("[AGENT] Control decided:", step)
 
#         if step == "call_llm":
#             print("[AGENT] Calling LLM")
#             response = call_llm(goal)
#             memory["steps"].append(response)
 
#         elif step == "use_tool":
#             print("[AGENT] Using tool")
#             result = print_tool(memory["steps"][-1])
#             memory["steps"].append(result)
 
#         elif step == "stop":
#             print("[AGENT] STOP → exiting loop")
#             break
 
#     print("[AGENT] Agent finished")


#Monday(19/01/2026)

# from app.control import decide_next_step
# from app.llm import call_llm
# from app.memory import init_memory
# from app.tools import fetch_joke_tool
 
# def run_agent(goal: str):
#     memory = init_memory(goal)
 
#     print("\n[AGENT] Starting agent")
#     print("[AGENT] Goal:", goal)
 
#     while True:
#         print("\n[AGENT] Loop iteration started")
#         step = decide_next_step(memory)
#         print("[AGENT] Control decided:", step)
 
#         if step == "call_llm":
#             response = call_llm(goal)
#             memory["steps"].append(response)
#             print("[AGENT] LLM Response:", response)
 
#         elif step == "use_tool":
#             result = fetch_joke_tool()
#             memory["steps"].append(result)
#             print("[AGENT] Tool Result:", result)
 
#         elif step == "stop":
#             print("[AGENT] Agent stopped cleanly")
#             break
 



# Just Updated from app.tools import fetch_joke_tool to from app.tools import fetch_stock_tool, format_output_tool

from app.control import decide_next_step
from app.llm import call_llm
from app.memory import init_memory
from app.tools import fetch_stock_tool, format_output_tool

def run_agent(goal: str):
    memory = init_memory(goal)

    print("\n[AGENT] Starting agent")
    print("[AGENT] Goal:", goal)

    while True:
        print("\n[AGENT] Loop iteration started")
        step = decide_next_step(memory)
        print("[AGENT] Control decided:", step)

        if step == "call_llm":
            response = call_llm(goal)
            memory["steps"].append(response)
            print("[AGENT] LLM Response:", response)

        elif step == "use_tool":
            stock_info = fetch_stock_tool()
            memory["steps"].append(stock_info)

            formatted_output = format_output_tool(stock_info)
            print(formatted_output)

        elif step == "stop":
            print("[AGENT] Agent stopped cleanly")
            break
