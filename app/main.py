from app.agent import run_agent

if __name__ == "__main__":
    with open("notice.txt", "r") as file:
        notice_text = file.read()

    run_agent(notice_text)
