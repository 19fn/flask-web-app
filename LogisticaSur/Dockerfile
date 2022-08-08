# tagged image as logisticasur-img:1.0
FROM python:3.8-slim-buster

# Dependencies
RUN apt-get update && apt-get install python3-dev default-libmysqlclient-dev build-essential -y

# Working directory
WORKDIR /app

# Copy all files
COPY . .

# Install virtual environment
RUN python3 -m venv /app/venv

# Upgrade pip
RUN python3 -m pip install --upgrade pip

# Enable virtual environment
ENV PATH="/app/venv/bin:$PATH"

# Open port 80 (http)
EXPOSE 80

# Install python dependencies
RUN python3 -m pip install -r requirements.txt

# Set flask environment variable
ENV FLASK_APP="app"
ENV FLASK_ENV="production"

# Run flask --host=0.0.0.0 (This tells operating system to listen on all public IPs.)
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=8080"]
