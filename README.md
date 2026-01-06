# 📚 BookSense: AI-Powered Book Summarizer

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Gradio](https://img.shields.io/badge/Gradio-4.12.0-orange.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

**Transform lengthy PDFs into concise, actionable summaries using cutting-edge AI technology**

[Live Demo](https://huggingface.co/spaces/nikhilesh9ix/BookSense) • [Report Bug](https://github.com/nikhilesh9ix/BookSense-Book-Summarizer/issues) • [Request Feature](https://github.com/nikhilesh9ix/BookSense-Book-Summarizer/issues)

</div>

---

## 🌟 Overview

BookSense is an intelligent book summarization tool that leverages Groq's Llama3 LLM to extract key insights from PDF documents. Whether you're a student, researcher, or professional, BookSense helps you digest lengthy content in minutes, not hours.

### ✨ Key Features

- 📖 **Smart PDF Processing** - Extracts and processes text from any PDF with customizable page ranges
- 🤖 **AI-Powered Summaries** - Utilizes Groq's Llama3-8b-8192 model for intelligent summarization
- 📊 **Real-Time Progress Tracking** - Visual feedback during document processing
- 💾 **Multiple Export Formats** - Download summaries as TXT or PDF files
- 🔊 **Text-to-Speech** - Listen to your summaries on the go with built-in audio generation
- ⚡ **Intelligent Rate Limiting** - Automatic retry logic with exponential backoff
- 🎨 **Intuitive Interface** - Clean, user-friendly Gradio UI

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Groq API Key ([Get yours free](https://console.groq.com/))

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/nikhilesh9ix/BookSense-Book-Summarizer.git
   cd BookSense-Book-Summarizer
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables**
   
   Create a `.env` file in the root directory:
   ```env
   GROQ_API_KEY=your_actual_groq_api_key_here
   ```

4. **Launch the application**
   ```bash
   python app.py
   ```

5. **Access the interface**
   
   Open your browser and navigate to `http://localhost:7860`

## 📖 Usage Guide

1. **Upload PDF** - Click the upload button and select your PDF file
2. **Choose Format** - Select your preferred export format (TXT or PDF)
3. **Generate Summary** - Click submit and watch the progress bar
4. **Review & Export** - Read the summary, download it, or listen to the audio version

### Example Use Cases

- 📚 Summarize academic papers and research articles
- 📊 Extract key points from business reports
- 📖 Get quick insights from technical documentation
- 🎓 Study more efficiently with condensed textbook chapters

## 🛠️ Technical Architecture

### Tech Stack

| Component | Technology |
|-----------|-----------|
| **Frontend** | Gradio 4.12.0 |
| **PDF Processing** | pdfplumber 0.10.3 |
| **AI Model** | Groq Llama3-8b-8192 |
| **Text-to-Speech** | gTTS 2.5.0 |
| **PDF Generation** | FPDF 1.7.2 |
| **NLP** | NLTK 3.8.1 |

### Processing Pipeline

```
PDF Upload → Text Extraction → Text Cleaning → Chunking → AI Summarization → Output Generation
```

### Configuration Parameters

| Parameter | Default Value | Description |
|-----------|---------------|-------------|
| Chunk Size | 2000 words | Text segments for processing |
| Max Tokens | 500 | Tokens per summary chunk |
| Temperature | 0.7 | AI creativity level |
| Model | llama3-8b-8192 | Groq LLM model |

##  Advanced Configuration

### Customization Options

Edit [app.py](app.py) to modify:

| Setting | Location | Default |
|---------|----------|---------|
| Chunk Size | `chunk_text()` | 2000 words |
| Max Tokens | `summarize_text()` | 500 |
| Temperature | `summarize_text()` | 0.7 |
| Model | `summarize_text()` | llama3-8b-8192 |
| Retry Logic | `summarize_text()` | 3 attempts |

### Environment Variables

```env
GROQ_API_KEY=your_groq_api_key_here
GROQ_API_URL=https://api.groq.com/openai/v1/chat/completions  # Optional
```

## 🐛 Troubleshooting

<details>
<summary><b>Rate Limiting (429 Errors)</b></summary>

The application includes automatic retry logic with exponential backoff. If issues persist:
- Check your Groq API rate limits
- Consider upgrading your API plan
- Increase delay between requests in `summarize_text_batched()`

</details>

<details>
<summary><b>Memory Issues with Large PDFs</b></summary>

- Reduce `chunk_size` parameter in `chunk_text()` function
- Process specific page ranges instead of entire documents
- Deploy to platforms with higher memory limits (Railway, GCP)

</details>

<details>
<summary><b>NLTK Data Download Issues</b></summary>

The app automatically downloads required NLTK data. If it fails:
```python
import nltk
nltk.download('punkt')
```

</details>

<details>
<summary><b>PDF Extraction Errors</b></summary>

- Ensure PDF is not password-protected
- Verify PDF contains extractable text (not scanned images)
- Try using OCR preprocessing for scanned documents

</details>

## 📊 Project Structure

```
BookSense-Book-Summarizer/
├── app.py                          # Main application file
├── requirements.txt                # Python dependencies
├── Dockerfile                      # Docker configuration
├── vercel.json                     # Vercel config (not recommended)
├── BookSense_Final_0 (1).ipynb    # Development notebook
└── README.md                       # Project documentation
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

### Areas for Contribution

- 🌍 Multi-language support
- 📊 Support for more file formats (DOCX, EPUB)
- 🎨 UI/UX improvements
- ⚡ Performance optimizations
- 📝 Better summarization prompts
- 🧪 Unit and integration tests

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Nikhilesh**

- GitHub: [@nikhilesh9ix](https://github.com/nikhilesh9ix)
- Project Link: [BookSense-Book-Summarizer](https://github.com/nikhilesh9ix/BookSense-Book-Summarizer)

## 🙏 Acknowledgments

- [Groq](https://groq.com/) for providing fast LLM inference
- [Gradio](https://gradio.app/) for the amazing UI framework
- [pdfplumber](https://github.com/jsvine/pdfplumber) for PDF processing
- [gTTS](https://github.com/pndurette/gTTS) for text-to-speech capabilities

---

<div align="center">

**⭐ Star this repo if you find it helpful!**

Made with ❤️ by [Nikhilesh](https://github.com/nikhilesh9ix)

</div>