# Dockerfile
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
# Dockerfile
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project
COPY . /app/

# Create necessary directories and set permissions
RUN mkdir -p /app/staticfiles && \
    useradd -m aliada && \
    chown -R aliada:aliada /app
    
USER aliada

# Expose port
EXPOSE 8000

# Default command (Gunicorn for production, can be overridden in compose)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "aliada_root.wsgi:application"]
