def retrieve_all_knowledge():
    print("[RETRIEVER] Reading full knowledge file")

    with open("app/knowledge.txt", "r", encoding="utf-8") as f:
        return f.read()
