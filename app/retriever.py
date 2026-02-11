def keyword_retrieval(chunks: list, question: str):
    print("\n[RETRIEVER] Performing Keyword Search")

    relevant_chunks = []

    for chunk in chunks:
        for word in question.lower().split():
            if word in chunk.lower():
                relevant_chunks.append(chunk)
                break

    return relevant_chunks