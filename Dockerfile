# Use an official Python runtime as a parent image
FROM python:3.9-slim

COPY . /app
# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY CattleScanner/requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt


RUN echo pwd

RUN echo ls

RUN chmod +x run.sh


## Expose the port the app runs on
EXPOSE 8000
RUN echo "$PWD"
# Command to run the Python script
CMD ["/app/run.sh"]
#ENTRYPOINT ["/app/run.sh"]