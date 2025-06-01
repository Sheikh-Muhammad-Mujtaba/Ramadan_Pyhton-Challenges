# Use Python base image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    CHAINLIT_FILES_DIR=/tmp/.files \
    CHAINLIT_CONFIG_PATH=/app/.chainlit/config.toml

# Set working directory
WORKDIR /app

# Copy requirements first (to leverage Docker cache)
COPY requirements.txt .

# Install Python dependencies including chainlit
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

RUN chmod -R 777 /app

# Make the Chainlit writable directory
RUN mkdir -p /app/.files && chmod -R 777 /app/.files


# Expose Chainlit port
EXPOSE 7860

# Run Chainlit
CMD ["chainlit", "run", "./main.py", "--host", "0.0.0.0", "--port", "7860"]
