# Use an official Python runtime as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project code to the working directory
COPY . .

# Set environment variables (if needed)
# ENV MY_VARIABLE=my_value

# Expose the port your Django app will run on (default is 8000)
EXPOSE 8000

# Define the command to run your Django app
CMD ["python", "manage.py", "runserver", "127.0.0.1:8000"]
