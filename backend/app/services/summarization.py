from transformers import pipeline
summary_pipeline = pipeline("summarization")

def generate_summary(text):
    return summary_pipeline(text, max_length=150, min_length=50, do_sample=False)[0]['summary_text']