# Use an official Python base image
FROM python:3.9-slim

#This line tells Docker to use the official 
# Python image with version 3.9 as the base. The -slim tag indicates 
# that it is a lightweight version of the full Python image, 
# containing only the essentials needed to run Python. This helps reduce the overall image size, 
# which is beneficial for faster downloads and deployments.


# Set environment variables to prevent Python buffering and bytecode generation
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose port 5000 for the Flask app
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
