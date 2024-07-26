# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY CattleScanner/requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . ./

RUN chmod +x run.sh


## Expose the port the app runs on
EXPOSE 8000

# Command to run the Python script
CMD ["/app/run.sh"]
