# Use Python 3.12.4 slim image as a base
FROM python:3.12.4-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the local directory into the container
COPY . /app

# Run your Python application
CMD ["python", "main.py"]