# BookSense: The Book Summarizer

An AI-powered book summarization tool that extracts text from PDF files and generates concise summaries using Groq's LLM API. The application features a user-friendly Gradio interface with export options and text-to-speech capabilities.

## Features

- 📚 PDF text extraction with customizable page ranges
- 🤖 AI-powered summarization using Groq's Llama3 model
- 📊 Progress tracking for long documents
- 💾 Export summaries as TXT or PDF
- 🔊 Text-to-speech audio generation
- 🎨 Clean, intuitive Gradio interface

## Prerequisites

- Python 3.8+
- Groq API Key ([Get one here](https://console.groq.com/))

## Local Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/nikhilesh9ix/BookSense-Book-Summarizer.git
   cd BookSense-Book-Summarizer
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   ```bash
   cp .env.example .env
   ```
   Edit `.env` and add your Groq API key:
   ```
   GROQ_API_KEY=your_actual_groq_api_key_here
   ```

4. **Run the application:**
   ```bash
   python app.py
   ```

5. Open your browser to `http://localhost:7860`

## Deployment Options

### ⚠️ Important Note About Vercel
Vercel is **not recommended** for this Gradio application because:
- Vercel serverless functions have timeout limits (10s hobby, 60s pro)
- Gradio requires persistent WebSocket connections
- PDF processing and API calls may exceed time limits

### ✅ Recommended Deployment Platforms

#### 1. **Hugging Face Spaces** (Best Option - Free)

1. Create a new Space at [huggingface.co/spaces](https://huggingface.co/spaces)
2. Select "Gradio" as the SDK
3. Upload these files: `app.py`, `requirements.txt`, `.env.example`
4. Add your `GROQ_API_KEY` in Settings → Repository Secrets
5. Your app will be live at `https://huggingface.co/spaces/YOUR_USERNAME/YOUR_SPACE`

**Create a `README.md` for HF Spaces:**
```yaml
---
title: BookSense Book Summarizer
emoji: 📚
colorFrom: blue
colorTo: green
sdk: gradio
sdk_version: 4.12.0
app_file: app.py
pinned: false
---
```

#### 2. **Railway.app** (Easy, Generous Free Tier)

1. Install Railway CLI: `npm i -g @railway/cli`
2. Login: `railway login`
3. Initialize: `railway init`
4. Add environment variable: `railway variables set GROQ_API_KEY=your_key`
5. Deploy: `railway up`

#### 3. **Render.com** (Free Tier Available)

1. Connect your GitHub repository
2. Create a new Web Service
3. Set build command: `pip install -r requirements.txt`
4. Set start command: `python app.py`
5. Add environment variable `GROQ_API_KEY` in settings

#### 4. **Google Cloud Run** (Pay-as-you-go)

```bash
# Build and deploy
gcloud run deploy booksense \
  --source . \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --set-env-vars GROQ_API_KEY=your_key
```

#### 5. **Docker Deployment**

**Create `Dockerfile`:**
```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 7860

CMD ["python", "app.py"]
```

**Build and run:**
```bash
docker build -t booksense .
docker run -p 7860:7860 -e GROQ_API_KEY=your_key booksense
```

## Usage

1. Upload a PDF file
2. Select export format (TXT or PDF)
3. Wait for the AI to process and summarize
4. Download the summary or listen to the audio version

## Configuration

### API Settings
- **Model:** `llama3-8b-8192` (Groq)
- **Max Tokens:** 500 per chunk
- **Temperature:** 0.7
- **Chunk Size:** 2000 words

### Customization
Edit `app.py` to modify:
- Chunk size for processing
- Model parameters
- UI styling
- Export formats

## Troubleshooting

**Rate Limiting (429 errors):**
- The app includes automatic retry logic with exponential backoff
- Consider upgrading your Groq API plan for higher limits

**Memory Issues:**
- For very large PDFs, consider reducing `chunk_size` in the code
- Deploy to platforms with higher memory limits

**NLTK Data:**
- The app automatically downloads required NLTK data on first run

## Tech Stack

- **Frontend:** Gradio
- **PDF Processing:** pdfplumber
- **AI Model:** Groq Llama3
- **Text-to-Speech:** gTTS
- **PDF Generation:** FPDF

## License

MIT License - feel free to use and modify!

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## Author

**Nikhilesh** - [GitHub](https://github.com/nikhilesh9ix)

---

⭐ Star this repo if you find it helpful!