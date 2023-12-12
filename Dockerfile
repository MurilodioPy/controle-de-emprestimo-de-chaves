# Use the official Python image as the base image
FROM python:3.10

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

COPY ./run.py .
COPY ./app /app

# Copie o script de inicialização para o diretório do docker-entrypoint-initdb.d/
ADD ./dump/init.sql /docker-entrypoint-initdb.d

# Expose the port on which your Flask app will run
EXPOSE 8080

# Copy the rest of your application code into the container
COPY . .

# Start the Flask application
CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]
