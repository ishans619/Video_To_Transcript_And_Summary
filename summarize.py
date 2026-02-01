from transformers import pipeline

def summarize_text(text, output_path):
    summarizer = pipeline(
        "summarization",
        model="facebook/bart-large-cnn",
        device=-1  # CPU
    )

    # Chunk text safely
    chunks = [text[i:i+1000] for i in range(0, len(text), 1000)]
    summary = ""

    for chunk in chunks:
        result = summarizer(
            chunk,
            max_length=150,
            min_length=60,
            do_sample=False
        )
        summary += result[0]["summary_text"] + "\n\n"

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(summary)
