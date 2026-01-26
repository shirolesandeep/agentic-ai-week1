from app.agent import run_agent

if __name__ == "__main__":
    goal = "Explain inflation in very simple terms"
    run_agent(goal)
    
    with open("notice.txt", "r") as file:
        notice_text = file.read()

    run_agent(notice_text)
