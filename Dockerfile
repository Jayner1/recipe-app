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

# Expose the desired TCP port
EXPOSE 8000

# Set the command to run your application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
