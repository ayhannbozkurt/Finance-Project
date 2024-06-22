# Base image
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the script and other necessary files
COPY . .

# Run the script
CMD ["python", "scraping.py"]