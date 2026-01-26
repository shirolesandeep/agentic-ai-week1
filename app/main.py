from app.agent import run_agent

if __name__ == "__main__":
<<<<<<< HEAD
    goal = "Explain inflation in very simple terms"
    run_agent(goal)
    
=======
    with open("notice.txt", "r") as file:
        notice_text = file.read()

    run_agent(notice_text)
>>>>>>> c4d4b69fc4f8b59ab3fe3e250d1db707fa1bf05c
