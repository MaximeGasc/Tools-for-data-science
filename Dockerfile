# Dockerfile for your app
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

# Clone your app repository from GitHub
RUN git clone https://github.com/MaximeGasc/Tools-for-data-science.git .

# Install Python dependencies for your app
RUN pip install -r requirements.txt

# Expose port 8501 (the default port for Streamlit)
EXPOSE 8501

# Healthcheck to ensure the app is running
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Set the entry point for running the Streamlit app
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
