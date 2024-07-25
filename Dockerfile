# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY CattleScanner/requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire CattleScanner directory into the container
COPY CattleScanner /app/CattleScanner

## Copy the dist directory into the container
#COPY dist /app/dist

# Create directories for input and output
RUN mkdir -p /app/inputs /app/outputs

# Expose the port the app runs on
EXPOSE 8000

# Set environment variables to indicate production mode
ENV ENV=production

# Command to run the Python script
CMD ["python", "CattleScanner/Cattle_inference.py"]
