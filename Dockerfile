# Use a small official Python image
FROM python:3.11-slim

# Prevent Python from writing .pyc files and keep stdout/stderr unbuffered
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies (add more if you need them later)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
 && rm -rf /var/lib/apt/lists/*

# Copy only requirements first (better for Docker cache)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Now copy the rest of the project
COPY . .

# If you want to run a web app (FastAPI/Flask/etc.), set the default command here.
# Adjust this to match your actual entrypoint.

# Example 1: FastAPI app in iep_assistant/main.py with "app" object
# CMD ["uvicorn", "iep_assistant.main:app", "--host", "0.0.0.0", "--port", "8000"]

# Example 2: plain Python script as entrypoint
# CMD ["python", "-m", "iep_assistant.main"]

# For now, just default to a generic main module; change this once you decide:
CMD ["python", "-m", "iep_assistant.main"]
