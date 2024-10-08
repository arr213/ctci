# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Set the PYTHONPATH so that Python can find the src module
ENV PYTHONPATH="${PYTHONPATH}:/app/src"

# Install dependencies (as listed in requirements.txt)
RUN pip install --no-cache-dir -r requirements.txt

# Run pytest by default when the container starts
CMD ["pytest"]
