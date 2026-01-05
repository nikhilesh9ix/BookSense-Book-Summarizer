import pdfplumber
import re
import nltk
import requests
import gradio as gr
import time
from fpdf import FPDF
from gtts import gTTS
import os

# Download NLTK data
nltk.download('punkt', quiet=True)

# Groq Cloud API configuration
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
GROQ_API_URL = os.getenv("GROQ_API_URL", "https://api.groq.com/openai/v1/chat/completions")

def extract_text_from_pdf(pdf_path, start_page=0, end_page=100):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages):
            if i < start_page:
                continue
            if i >= end_page:
                break
            text += page.extract_text() or ""
    return text

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^\w\s.]', '', text)
    return text.strip()

def summarize_text(text, retries=3):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "llama3-8b-8192",
        "messages": [
            {"role": "system", "content": "You are a summarization assistant."},
            {"role": "user", "content": f"Summarize the following text:\n\n{text}"}
        ],
        "max_tokens": 500,
        "temperature": 0.7,
        "top_p": 1.0
    }
    for attempt in range(retries):
        try:
            response = requests.post(GROQ_API_URL, json=payload, headers=headers)
            response.raise_for_status()
            result = response.json()
            return result.get("choices", [{}])[0].get("message", {}).get("content", "").strip()
        except requests.exceptions.RequestException as e:
            if e.response and e.response.status_code == 429:
                retry_after = e.response.headers.get("Retry-After", 2)
                print(f"429 error on attempt {attempt + 1}/{retries}. Waiting {retry_after}s...")
                time.sleep(float(retry_after) * (2 ** attempt))
            else:
                error_detail = e.response.text if e.response else "No response body"
                return f"Error calling Groq Cloud API: {str(e)} - Status Code: {e.response.status_code if e.response else 'N/A'} - Detail: {error_detail}"
    return "Failed after retries due to persistent 429 errors"

def chunk_text(text, chunk_size=2000):
    words = text.split()
    chunks = [' '.join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]
    return chunks

def summarize_text_batched(text, progress=gr.Progress()):
    start_time = time.time()
    chunks = chunk_text(text)
    summaries = []
    progress(0, desc="Starting summarization...")
    for i, chunk in enumerate(chunks):
        summary = summarize_text(chunk)
        summaries.append(summary)
        progress((i + 1) / len(chunks), desc=f"Processing chunk {i + 1}/{len(chunks)}")
        if i < len(chunks) - 1:
            time.sleep(2)
    total_time = time.time() - start_time
    print(f"Processed {len(chunks)} chunks in {total_time:.2f} seconds")
    return " ".join(summaries)

def generate_export_file(summary, export_format):
    filename = f"summary_{int(time.time())}.{export_format}"
    if export_format == "txt":
        with open(filename, "w", encoding="utf-8") as f:
            f.write(summary)
    elif export_format == "pdf":
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        for line in summary.split('\n'):
            pdf.multi_cell(0, 10, line.encode('latin-1', 'replace').decode('latin-1'))
        pdf.output(filename)
    return filename

def generate_audio(summary):
    audio_filename = f"summary_audio_{int(time.time())}.mp3"
    tts = gTTS(text=summary, lang='en', slow=False)
    tts.save(audio_filename)
    return audio_filename

def process_pdf(pdf_file, export_format, progress=gr.Progress()):
    if not pdf_file:
        return "Please upload a PDF file.", None, None
    start_time = time.time()
    text = extract_text_from_pdf(pdf_file)
    cleaned_text = clean_text(text)
    summary = summarize_text_batched(cleaned_text, progress)
    total_time = time.time() - start_time
    summary_text = f"Summary (processed in {total_time:.2f} seconds):\n\n{summary}"
    export_file = generate_export_file(summary_text, export_format)
    audio_file = generate_audio(summary_text)
    return summary_text, export_file, audio_file

# Create Gradio interface
interface = gr.Interface(
    fn=process_pdf,
    inputs=[
        gr.File(label="Upload PDF"),
        gr.Dropdown(label="Export Format", choices=["txt", "pdf"], value="txt")
    ],
    outputs=[
        gr.Textbox(label="Summary"),
        gr.File(label="Download Summary"),
        gr.Audio(label="Listen to Summary", type="filepath")
    ],
    title="BookSense: The Book Summarizer",
    description="Upload a PDF to get a quick summary with a progress bar. Choose an export format to download the result and listen to it via text-to-speech."
)

if __name__ == "__main__":
    interface.queue()
    interface.launch()
