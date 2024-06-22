# Base image
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the script and other necessary files
COPY . .

# Download the model beforehand to ensure it's available
RUN python -c "from transformers import pipeline; pipeline('sentiment-analysis', model='soleimanian/financial-roberta-large-sentiment')"

# Run the script
CMD ["python", "scraping.py"]
