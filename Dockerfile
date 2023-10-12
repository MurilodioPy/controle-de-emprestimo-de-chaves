# Use the official Python image as the base image
FROM python:3.9

# Set environment variables
# app name
ENV FLASK_APP=run
ENV FLASK_ENV=production
ENV FLASK_RUN_HOST=0.0.0.0

# Set the working directory
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Expose the port on which your Flask app will run
EXPOSE 5000

# Copy the rest of your application code into the container
COPY . .

# Start the Flask application
CMD ["flask", "run"]
