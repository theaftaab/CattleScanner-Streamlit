# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Setup basic linux environment tools
RUN apt-get update && \
    apt-get install -y \
      sudo \
      curl \
      vim \
      unzip \
      rsync \
      libgl1-mesa-glx \
      libglib2.0-0 \
      build-essential \
      software-properties-common \
      ssh && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


# Create working directory
RUN mkdir /cattle_app

# Set the working directory in the container
WORKDIR /cattle_app

# Copy local contents to /cattle_app
COPY . /cattle_app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r /cattle_app/CattleScanner/requirements.txt

# Expose the port the app runs on
EXPOSE 8000

# Command to run the flask application
CMD ["gunicorn", "-w", "4", "-b", ":8000", "app:app"]

