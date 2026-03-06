from transformers import pipeline


# Load model once
generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
    device=-1   # CPU
)


def chunk_text(text, max_chunks=5):

    sentences = text.replace("\n", " ").split(".")
    chunks = []

    for sentence in sentences:
        sentence = sentence.strip()

        if len(sentence) > 30:
            chunks.append(sentence)

        if len(chunks) >= max_chunks:
            break

    return chunks

def generate_question(chunk):
    """
    Generate a question from a text chunk
    """
    prompt = f"Generate a question from the following text: {chunk}"

    result = generator(
        prompt,
        max_new_tokens=32,
        do_sample=False
    )

    question = result[0]["generated_text"].strip()

    return question


def generate_qna(text):
    """
    Main QnA generator
    """
    chunks = chunk_text(text)

    qna_pairs = []

    for chunk in chunks:

        question = generate_question(chunk)

        qna_pairs.append({
            "question": question,
            "answer": chunk
        })

    return qna_pairs