FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Download NLTK data
RUN python -c "import nltk; nltk.download('punkt')"

# Copy application files
COPY . .

# Expose Gradio default port
EXPOSE 7860

# Set environment variable for Gradio to run on all interfaces
ENV GRADIO_SERVER_NAME="0.0.0.0"

# Run the application
CMD ["python", "app.py"]
