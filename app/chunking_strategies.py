def line_based_chunking(text: str):
    print("\n[CHUNKING] Line-Based Strategy")
    return [line.strip() for line in text.split("\n") if line.strip()]


def paragraph_based_chunking(text: str):
    print("\n[CHUNKING] Paragraph-Based Strategy")
    paragraphs = text.split("\n\n")
    return [p.strip() for p in paragraphs if p.strip()]


def fixed_size_chunking(text: str, size=150):
    print("\n[CHUNKING] Fixed-Size Strategy")
    chunks = []
    for i in range(0, len(text), size):
        chunks.append(text[i:i + size])
    return chunks


def overlapping_chunking(text: str, size=150, overlap=40):
    print("\n[CHUNKING] Overlapping Strategy")
    chunks = []
    step = size - overlap
    for i in range(0, len(text), step):
        chunks.append(text[i:i + size])
    return chunks
